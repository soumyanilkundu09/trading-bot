"""
strategy_scorer.py — The Malkan GFS 12-parameter scoring engine.

Given a ticker, this:
  1. Pulls full technical analysis from market_data.analyze_ticker().
  2. Pulls sector ETF strength.
  3. Evaluates the mandatory P1 global gate (macro outlook + VIX).
  4. Scores P2..P12 (weighted, total 108).
  5. Runs the Part 7 instant-disqualifier checks.
  6. Computes entry / stop-loss / targets / position size per Part 6 + 8B.

Returns a structured dict the agent prompts consume to decide and place trades.
The agent still makes the final call; this gives it deterministic, rule-faithful numbers.

Usage:
    python tools/strategy_scorer.py --ticker AAPL --sector Technology
    python tools/strategy_scorer.py --ticker NVDA   # auto sector lookup skipped
"""

from __future__ import annotations

import argparse
import json
import math
import os
import sys
from dataclasses import dataclass, field

import market_data as md

CONFIG_DIR = os.path.join(os.path.dirname(__file__), "..", "config")


def load_config() -> dict:
    with open(os.path.join(CONFIG_DIR, "market_config.json")) as f:
        market = json.load(f)
    with open(os.path.join(CONFIG_DIR, "trading_config.json")) as f:
        trading = json.load(f)
    return {"market": market, "trading": trading}


# Parameter weights (Part 9). P1 is a gate (no score), P8 is implicit (required, not scored).
WEIGHTS = {
    "P2": 12,   # Sector Strong
    "P3": 12,   # Weekly RSI > 60
    "P4": 10,   # Weekly RSI > 40
    "P5": 6,    # Weekly Range Shift / Support @ 40
    "P6": 8,    # High Green Volume Weekly
    "P7": 12,   # Daily at Support / CIP / Gap
    "P9": 14,   # Not Near Resistance
    "P10": 10,  # Daily Prev Candle Red, Low Volume
    "P11": 12,  # Daily RSI @ 40
    "P12": 12,  # Bullish Range Shift / Divergence
}
MAX_SCORE = sum(WEIGHTS.values())  # 108


# --------------------------------------------------------------------------
# Global gate (P1) + macro outlook
# --------------------------------------------------------------------------
def evaluate_global_outlook(cfg: dict, macro: dict | None = None) -> dict:
    """Part 3 decision rule. Returns POSITIVE / NEGATIVE / INDECISIVE + detail."""
    if macro is None:
        macro = md.macro_snapshot()

    vix_danger = cfg["market"]["volatility_index"]["danger_above"]
    vix_caution = cfg["market"]["volatility_index"]["caution_band"][0]

    checks = {}
    bearish_flags = 0

    spx_m = macro.get("sp500_monthly_rsi", 0)
    spx_w = macro.get("sp500_weekly_rsi", 0)
    vix = macro.get("vix", 99)
    dxy_chg = macro.get("dxy_20d_change_pct", 0)

    checks["sp500_monthly_rsi_gt_60"] = spx_m > 60
    if spx_m <= 60:
        bearish_flags += 1

    checks["sp500_weekly_rsi_gt_50"] = spx_w > 50
    if spx_w <= 50:
        bearish_flags += 1

    checks["vix_ok"] = vix < vix_danger
    if vix >= vix_danger:
        bearish_flags += 1
    checks["vix_not_elevated"] = vix < vix_caution

    checks["dxy_not_spiking"] = dxy_chg < 3.0
    if dxy_chg >= 3.0:
        bearish_flags += 1

    if bearish_flags == 0 and checks["sp500_monthly_rsi_gt_60"] and checks["vix_ok"]:
        outlook = "POSITIVE"
    elif bearish_flags >= 2:
        outlook = "NEGATIVE"
    else:
        outlook = "INDECISIVE"

    return {
        "outlook": outlook,
        "macro": macro,
        "checks": checks,
        "bearish_flags": bearish_flags,
        "gate_passed": outlook == "POSITIVE",
    }


# --------------------------------------------------------------------------
# Per-parameter scoring
# --------------------------------------------------------------------------
@dataclass
class ScoreResult:
    symbol: str
    ok: bool
    gate_passed: bool = False
    outlook: str = ""
    score: int = 0
    max_score: int = MAX_SCORE
    decision: str = "SKIP"
    passed: dict = field(default_factory=dict)
    failed: dict = field(default_factory=dict)
    param_detail: dict = field(default_factory=dict)
    disqualifiers: list = field(default_factory=list)
    p8_entry_ok: bool = False
    trade_plan: dict = field(default_factory=dict)
    error: str = ""


def score_parameters(a: md.TickerAnalysis, sector: dict | None) -> dict:
    """Score P2..P12. Returns {param: (passed_bool, points, detail)}."""
    res = {}

    # P2 — Sector Strong: sector ETF weekly RSI > 60
    if sector and sector.get("ok"):
        p2 = sector["weekly_rsi"] > 60 and sector["monthly_rsi"] > 55
        res["P2"] = (p2, WEIGHTS["P2"] if p2 else 0,
                     f"sector W-RSI={sector['weekly_rsi']} M-RSI={sector['monthly_rsi']}")
    else:
        res["P2"] = (False, 0, "sector data unavailable")

    # P3 — Weekly RSI > 60
    p3 = a.weekly_rsi >= 60
    res["P3"] = (p3, WEIGHTS["P3"] if p3 else 0, f"weekly_rsi={a.weekly_rsi}")

    # P4 — Weekly RSI > 40 (Bearish Range Shift guard)
    p4 = a.weekly_rsi >= 40
    res["P4"] = (p4, WEIGHTS["P4"] if p4 else 0, f"weekly_rsi={a.weekly_rsi}")

    # P5 — Weekly Range Shift / Support @ 40
    rsw = a.range_shift_weekly
    p5 = bool(rsw.get("bullish_range_shift")) or (a.weekly_rsi >= 60 and not rsw.get("bearish_range_shift"))
    res["P5"] = (p5, WEIGHTS["P5"] if p5 else 0, f"weekly_brs={rsw.get('bullish_range_shift')}")

    # P6 — High Green Volume Weekly (proxy: any recent strong green weekly candle).
    # We approximate using daily volume strength on the dominant up-moves.
    vol = a.volume
    last = vol.get("last_candle", {})
    p6 = last.get("vol_vs_avg", 0) >= 1.3 and last.get("green", False)
    res["P6"] = (p6, WEIGHTS["P6"] if p6 else 0,
                 f"last_vol_vs_avg={last.get('vol_vs_avg')} green={last.get('green')}")

    # P7 — Daily at Support / CIP / Gap (within 2%)
    sr = a.support_resistance
    near_support = sr.get("dist_to_support_pct", 99) <= 2.5
    in_cip = a.cip.get("is_consolidating", False)
    in_gap = any(g.get("is_support") and abs(a.price - g["gap_top"]) / a.price < 0.02 for g in a.gaps)
    p7 = near_support or in_cip or in_gap
    res["P7"] = (p7, WEIGHTS["P7"] if p7 else 0,
                 f"dist_support={sr.get('dist_to_support_pct')}% cip={in_cip} gap={in_gap}")

    # P9 — Not Near Previous Resistance (>= 8% upside)
    p9 = sr.get("dist_to_resistance_pct", 0) >= 8.0
    res["P9"] = (p9, WEIGHTS["P9"] if p9 else 0, f"dist_resistance={sr.get('dist_to_resistance_pct')}%")

    # P10 — Daily Prev Candle Red with Low Volume (Adverse Low Move)
    prev = vol.get("prev_candle", {})
    p10 = (not prev.get("green", True)) and prev.get("vol_vs_avg", 99) < 1.0
    res["P10"] = (p10, WEIGHTS["P10"] if p10 else 0,
                  f"prev_red={not prev.get('green')} prev_vol_vs_avg={prev.get('vol_vs_avg')}")

    # P11 — Daily RSI @ 40 (38–45 zone)
    p11 = 38 <= a.daily_rsi <= 45
    res["P11"] = (p11, WEIGHTS["P11"] if p11 else 0, f"daily_rsi={a.daily_rsi}")

    # P12 — Bullish Range Shift / Daily Divergence
    rsd = a.range_shift_daily
    div = a.divergence_daily
    p12 = bool(rsd.get("bullish_range_shift")) or div.get("regular_bullish") or div.get("hidden_bullish")
    res["P12"] = (p12, WEIGHTS["P12"] if p12 else 0,
                  f"daily_brs={rsd.get('bullish_range_shift')} reg_div={div.get('regular_bullish')} hid_div={div.get('hidden_bullish')}")

    return res


# --------------------------------------------------------------------------
# Disqualifiers (Part 7)
# --------------------------------------------------------------------------
def check_disqualifiers(a: md.TickerAnalysis, outlook: dict, cfg: dict) -> list:
    dq = []
    vix_danger = cfg["market"]["volatility_index"]["danger_above"]

    if outlook["macro"].get("vix", 0) > vix_danger:
        dq.append(f"VIX {outlook['macro'].get('vix')} > {vix_danger} (fear zone)")

    if a.range_shift_weekly.get("bearish_range_shift"):
        dq.append("Bearish Range Shift on Weekly (macro structure broken)")

    if a.divergence_daily.get("bearish"):
        dq.append("Bearish Divergence on Daily near resistance")

    last = a.volume.get("last_candle", {})
    if (not last.get("green", True)) and last.get("vol_vs_avg", 0) >= 1.5:
        dq.append("Red daily candle with HIGH volume (Bearish Loud Move)")

    if a.weekly_rsi >= 80 and a.support_resistance.get("dist_to_resistance_pct", 99) < 3:
        dq.append("Extended near 52-wk high with RSI > 80")

    if a.daily_rsi < 38 and not (
        a.range_shift_daily.get("bullish_range_shift")
        or a.divergence_daily.get("regular_bullish")
        or a.divergence_daily.get("hidden_bullish")
    ):
        dq.append("Daily RSI < 38 with no BRS/divergence (falling through 40)")

    return dq


# --------------------------------------------------------------------------
# Trade plan: entry / SL / targets / position size (Part 6 + 8B)
# --------------------------------------------------------------------------
def build_trade_plan(a: md.TickerAnalysis, cfg: dict, capital: float, half: bool,
                     live_price: float | None = None) -> dict:
    rc = cfg["market"]["risk_controls"]
    # Size off the REAL execution price when available (Alpaca live), not the
    # prior-session yfinance close. Stops/targets are anchored to chart structure,
    # so they stay valid; only the entry reference changes.
    entry = float(live_price) if live_price else a.price
    planned_entry = a.price

    # Stop-loss: low of trigger (last) candle, fall back to support - 0.5%
    sr = a.support_resistance
    trigger_low = entry * (1 - 0.03)  # conservative default if low not surfaced
    sl_support = sr.get("nearest_support", entry * 0.95) * 0.995
    stop_loss = max(sl_support, trigger_low)
    # Enforce max stop distance
    max_sl = entry * (1 - rc["max_stop_loss_pct"] / 100)
    stop_loss = max(stop_loss, max_sl)
    stop_loss = round(min(stop_loss, entry * 0.999), 2)

    risk_per_share = max(entry - stop_loss, 0.01)

    risk_pct = rc["half_position_risk_pct"] if half else rc["risk_per_trade_pct"]
    risk_amount = capital * risk_pct / 100
    raw_shares = risk_amount / risk_per_share

    max_position_value = capital * rc["max_position_pct"] / 100
    cap_shares = math.floor(max_position_value / entry) if entry else 0
    shares = int(min(math.floor(raw_shares), cap_shares))

    # Targets: T1 = nearest resistance or +2R, whichever is closer — but always above entry
    # (if live price already broke above the old resistance, fall back to +2R).
    resistance = sr.get("nearest_resistance", entry * 1.1)
    t1 = min(resistance, entry + 2 * risk_per_share)
    if t1 <= entry:
        t1 = entry + 2 * risk_per_share
    t1 = round(t1, 2)
    t2 = round(max(resistance, entry + 3 * risk_per_share), 2)

    chase_pct = round((entry - planned_entry) / planned_entry * 100, 2) if planned_entry else 0.0
    max_chase = rc.get("max_chase_pct", 3.0)

    return {
        "entry": round(entry, 2),
        "planned_entry": round(planned_entry, 2),
        "chase_pct": chase_pct,
        "is_chasing": bool(chase_pct > max_chase),
        "stop_loss": stop_loss,
        "risk_per_share": round(risk_per_share, 2),
        "stop_loss_pct": round((entry - stop_loss) / entry * 100, 2),
        "target1": t1,
        "target2": t2,
        "shares": shares,
        "position_value": round(shares * entry, 2),
        "position_pct_of_capital": round(shares * entry / capital * 100, 2) if capital else 0,
        "risk_amount": round(shares * risk_per_share, 2),
        "risk_pct_used": risk_pct,
        "reward_risk_t1": round((t1 - entry) / risk_per_share, 2) if risk_per_share else 0,
    }


# --------------------------------------------------------------------------
# Orchestration
# --------------------------------------------------------------------------
def score_ticker(symbol: str, sector_name: str | None = None,
                 macro: dict | None = None, capital: float | None = None,
                 live_price: float | None = None) -> ScoreResult:
    cfg = load_config()
    if capital is None:
        capital = float(cfg["trading"].get("total_capital", 10000))

    a = md.analyze_ticker(symbol)
    if not a.ok:
        return ScoreResult(symbol=symbol, ok=False, error=a.error)

    outlook = evaluate_global_outlook(cfg, macro)

    # Sector lookup
    sector = None
    if sector_name and sector_name in cfg["market"]["sector_etfs"]:
        etf = cfg["market"]["sector_etfs"][sector_name]
        sector = md.get_sector_rsi(etf)

    params = score_parameters(a, sector)
    passed = {k: v[2] for k, v in params.items() if v[0]}
    failed = {k: v[2] for k, v in params.items() if not v[0]}
    detail = {k: {"passed": v[0], "points": v[1], "detail": v[2]} for k, v in params.items()}
    total = sum(v[1] for v in params.values())

    disq = check_disqualifiers(a, outlook, cfg)

    # P8 implicit: entry candle green + above-avg volume
    last = a.volume.get("last_candle", {})
    p8_ok = bool(last.get("green") and last.get("vol_vs_avg", 0) >= 1.0)

    # Decision
    thr = cfg["market"]["scoring_thresholds"]
    if not outlook["gate_passed"]:
        decision = "NO_TRADE_GATE"
    elif disq:
        decision = "DISQUALIFIED"
    elif total >= thr["full_position_min"]:
        decision = "ENTER_FULL"
    elif total >= thr["watchlist_min"]:
        decision = "WATCHLIST_HALF"
    else:
        decision = "SKIP"

    half = decision == "WATCHLIST_HALF"
    plan = (
        build_trade_plan(a, cfg, capital, half, live_price=live_price)
        if decision in ("ENTER_FULL", "WATCHLIST_HALF")
        else {}
    )

    # Avoid-chasing gate (only meaningful when a live price is supplied at execution time):
    # if the live price has run > max_chase_pct above the planned (prior-session) entry
    # zone, downgrade an otherwise-enterable setup to watchlist — never chase.
    if plan.get("is_chasing"):
        if decision == "ENTER_FULL":
            decision = "WATCHLIST_CHASE"
        elif decision == "WATCHLIST_HALF":
            decision = "WATCHLIST_CHASE"

    return ScoreResult(
        symbol=symbol,
        ok=True,
        gate_passed=outlook["gate_passed"],
        outlook=outlook["outlook"],
        score=total,
        decision=decision,
        passed=passed,
        failed=failed,
        param_detail=detail,
        disqualifiers=disq,
        p8_entry_ok=p8_ok,
        trade_plan=plan,
    )


def main():
    ap = argparse.ArgumentParser(description="Malkan 12-parameter scorer")
    ap.add_argument("--ticker", required=True)
    ap.add_argument("--sector", default=None, help="Sector name (e.g. Technology) for P2")
    ap.add_argument("--capital", type=float, default=None)
    ap.add_argument("--live-price", type=float, default=None,
                    help="Override entry with a live execution price (enables avoid-chasing gate)")
    ap.add_argument("--live", action="store_true",
                    help="Fetch the live price from Alpaca automatically")
    args = ap.parse_args()

    live_price = args.live_price
    if args.live and live_price is None:
        try:
            from alpaca_client import AlpacaClient
            live_price = AlpacaClient().get_latest_price(args.ticker.upper())
        except Exception as e:
            sys.stderr.write(f"[live] could not fetch live price: {e}\n")

    from dataclasses import asdict
    r = score_ticker(args.ticker.upper(), args.sector, capital=args.capital, live_price=live_price)
    print(json.dumps(asdict(r), indent=2, default=str))


if __name__ == "__main__":
    main()
