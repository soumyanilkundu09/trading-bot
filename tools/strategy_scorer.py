"""
strategy_scorer.py — Malkan GFS 5-parameter entry scorer.

Applies to all three RSI tiers produced by rsi_scan.py:
  EXTREMELY_BULLISH_PULLBACK, EXTREMELY_BULLISH_MOMENTUM, BULLISH

Parameters (max 10 pts):
  P2  — Sector Strong             (2 pts)
  P7  — Daily at Support/CIP/Gap  (2 pts) — skipped for EB Momentum (max becomes 8)
  P8  — High Green Volume Daily   (1 pt)
  P9  — Not Near Resistance ≥5%  (4 pts)
  P10 — Recent Red Volume Low     (1 pt)

Decision: score ≥ 6 → ENTER, else SKIP.

Usage:
    python tools/strategy_scorer.py --ticker AAPL --sector Technology --tier EXTREMELY_BULLISH_PULLBACK
    python tools/strategy_scorer.py --ticker FTNT --sector Technology --tier EXTREMELY_BULLISH_MOMENTUM --live
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

WEIGHTS = {
    "P2":  2,   # Sector Strong (weekly RSI > 60)
    "P7":  2,   # Daily at Support / CIP / Gap  [skipped for EB Momentum]
    "P8":  1,   # High Green Volume Daily (last 6-7 green candles vs 20-day avg)
    "P9":  4,   # Not Near Resistance (≥5% upside to nearest resistance)
    "P10": 1,   # Recent Red Candles Low Volume (last 3-4 red candles vs 20-day avg)
}
MAX_SCORE = sum(WEIGHTS.values())   # 10
ENTER_THRESHOLD = 6                 # score must be >= this to enter


def load_config() -> dict:
    with open(os.path.join(CONFIG_DIR, "market_config.json")) as f:
        market = json.load(f)
    with open(os.path.join(CONFIG_DIR, "trading_config.json")) as f:
        trading = json.load(f)
    return {"market": market, "trading": trading}


# --------------------------------------------------------------------------
# Dataclass
# --------------------------------------------------------------------------
@dataclass
class ScoreResult:
    symbol: str
    ok: bool
    tier: str = ""
    score: int = 0
    max_score: int = MAX_SCORE
    decision: str = "SKIP"
    passed: dict = field(default_factory=dict)
    failed: dict = field(default_factory=dict)
    param_detail: dict = field(default_factory=dict)
    trade_plan: dict = field(default_factory=dict)
    error: str = ""


# --------------------------------------------------------------------------
# Parameter evaluation
# --------------------------------------------------------------------------
def score_parameters(a: md.TickerAnalysis, sector: dict | None, tier: str) -> dict:
    """
    Evaluate P2, P7, P8, P9, P10 for the given tier.
    P7 is skipped (0 pts, not counted against max) for EXTREMELY_BULLISH_MOMENTUM.
    Returns {param: (passed_bool, points, detail_str)}.
    """
    res = {}
    is_momentum = (tier == "EXTREMELY_BULLISH_MOMENTUM")

    # P2 — Sector Strong: sector ETF weekly RSI > 60
    if sector and sector.get("ok"):
        p2 = sector["weekly_rsi"] > 60
        res["P2"] = (p2, WEIGHTS["P2"] if p2 else 0,
                     f"sector_W-RSI={sector['weekly_rsi']}")
    else:
        res["P2"] = (False, 0, "sector data unavailable")

    # P7 — Daily at Support / CIP / Gap (within ~2.5% of nearest support, or in CIP, or at gap)
    # Skipped entirely for EB Momentum (stock is not expected to be at a support zone).
    if is_momentum:
        res["P7"] = (None, 0, "skipped for EB_MOMENTUM tier")
    else:
        sr = a.support_resistance
        near_support = sr.get("dist_to_support_pct", 99) <= 2.5
        in_cip = a.cip.get("is_consolidating", False)
        in_gap = any(
            g.get("is_support") and abs(a.price - g["gap_top"]) / a.price < 0.02
            for g in a.gaps
        )
        p7 = near_support or in_cip or in_gap
        res["P7"] = (p7, WEIGHTS["P7"] if p7 else 0,
                     f"dist_support={sr.get('dist_to_support_pct')}% cip={in_cip} gap={in_gap}")

    # P8 — High Green Volume Daily: last 6-7 green candles avg > 20-day avg
    vol = a.volume
    green_cluster = vol.get("recent_green", {})
    p8 = (
        green_cluster.get("count", 0) > 0
        and green_cluster.get("mean_vol_vs_avg", 0) >= 1.0
    )
    res["P8"] = (p8, WEIGHTS["P8"] if p8 else 0,
                 f"last_{green_cluster.get('count')}green_vol_vs_avg={green_cluster.get('mean_vol_vs_avg')}")

    # P9 — Not Near Resistance: ≥5% upside to nearest resistance
    sr = a.support_resistance
    p9 = sr.get("dist_to_resistance_pct", 0) >= 5.0
    res["P9"] = (p9, WEIGHTS["P9"] if p9 else 0,
                 f"dist_resistance={sr.get('dist_to_resistance_pct')}%")

    # P10 — Recent Red Candles Low Volume: last 3-4 red candles avg < 20-day avg
    red = vol.get("recent_red", {})
    red_ratio = red.get("mean_vol_vs_avg", 99)
    p10 = red.get("count", 0) > 0 and red_ratio < 1.0
    res["P10"] = (p10, WEIGHTS["P10"] if p10 else 0,
                  f"last_{red.get('count')}red_vol_vs_avg={red_ratio}")

    return res


# --------------------------------------------------------------------------
# Trade plan: entry / stop / targets / position size
# --------------------------------------------------------------------------
def build_trade_plan(a: md.TickerAnalysis, cfg: dict, capital: float, tier: str,
                     live_price: float | None = None) -> dict:
    """
    Compute entry, stop-loss, T1, and position size.

    For EB_MOMENTUM: T1 is None — position is managed via 3-bar trailing stop
    in the midday-scan job; no fixed bracket target is set.

    For EB_PULLBACK and BULLISH: T1 = nearest resistance above entry.
    """
    rc = cfg["market"]["risk_controls"]
    entry = float(live_price) if live_price else a.price

    # Stop-loss: low of trigger candle approximated as max(support−0.5%, entry−3%)
    sr = a.support_resistance
    trigger_low = entry * (1 - 0.03)
    sl_support = sr.get("nearest_support", entry * 0.95) * 0.995
    stop_loss = max(sl_support, trigger_low)
    max_sl = entry * (1 - rc["max_stop_loss_pct"] / 100)
    stop_loss = max(stop_loss, max_sl)
    stop_loss = round(min(stop_loss, entry * 0.999), 2)

    risk_per_share = max(entry - stop_loss, 0.01)

    risk_amount = capital * rc["risk_per_trade_pct"] / 100
    raw_shares = risk_amount / risk_per_share

    max_position_value = capital * rc["max_position_pct"] / 100
    cap_shares = math.floor(max_position_value / entry) if entry else 0
    shares = int(min(math.floor(raw_shares), cap_shares))

    is_momentum = (tier == "EXTREMELY_BULLISH_MOMENTUM")

    if is_momentum:
        # No fixed target — trailing stop only (managed in midday scan)
        t1 = None
        t2 = None
        reward_risk = None
    else:
        resistance = sr.get("nearest_resistance", entry * 1.1)
        t1 = round(max(resistance, entry + 2 * risk_per_share), 2)
        if t1 <= entry:
            t1 = round(entry + 2 * risk_per_share, 2)
        t2 = round(entry + 3 * risk_per_share, 2)
        reward_risk = round((t1 - entry) / risk_per_share, 2) if risk_per_share else None

    return {
        "entry": round(entry, 2),
        "stop_loss": stop_loss,
        "risk_per_share": round(risk_per_share, 2),
        "stop_loss_pct": round((entry - stop_loss) / entry * 100, 2),
        "target1": t1,
        "target2": t2,
        "shares": shares,
        "position_value": round(shares * entry, 2),
        "position_pct_of_capital": round(shares * entry / capital * 100, 2) if capital else 0,
        "risk_amount": round(shares * risk_per_share, 2),
        "reward_risk_t1": reward_risk,
        "trailing_stop_only": is_momentum,
    }


# --------------------------------------------------------------------------
# Orchestration
# --------------------------------------------------------------------------
def score_ticker(symbol: str, tier: str = "EXTREMELY_BULLISH_PULLBACK",
                 sector_name: str | None = None,
                 macro: dict | None = None,
                 capital: float | None = None,
                 live_price: float | None = None) -> ScoreResult:
    cfg = load_config()
    if capital is None:
        capital = float(cfg["trading"].get("total_capital", 10000))

    a = md.analyze_ticker(symbol)
    if not a.ok:
        return ScoreResult(symbol=symbol, ok=False, error=a.error)

    # Sector lookup for P2
    sector = None
    if sector_name and sector_name in cfg["market"]["sector_etfs"]:
        etf = cfg["market"]["sector_etfs"][sector_name]
        sector = md.get_sector_rsi(etf)

    params = score_parameters(a, sector, tier)

    # Separate skipped params (P7 for momentum) from scored ones
    passed = {k: v[2] for k, v in params.items() if v[0] is True}
    failed = {k: v[2] for k, v in params.items() if v[0] is False}
    detail = {k: {"passed": v[0], "points": v[1], "detail": v[2]} for k, v in params.items()}
    total = sum(v[1] for v in params.values())

    is_momentum = (tier == "EXTREMELY_BULLISH_MOMENTUM")
    effective_max = MAX_SCORE - (WEIGHTS["P7"] if is_momentum else 0)

    decision = "ENTER" if total >= ENTER_THRESHOLD else "SKIP"

    plan = (
        build_trade_plan(a, cfg, capital, tier, live_price=live_price)
        if decision == "ENTER"
        else {}
    )

    return ScoreResult(
        symbol=symbol,
        ok=True,
        tier=tier,
        score=total,
        max_score=effective_max,
        decision=decision,
        passed=passed,
        failed=failed,
        param_detail=detail,
        trade_plan=plan,
    )


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser(description="Malkan 5-parameter entry scorer")
    ap.add_argument("--ticker", required=True)
    ap.add_argument("--tier", required=True,
                    choices=["EXTREMELY_BULLISH_PULLBACK", "EXTREMELY_BULLISH_MOMENTUM", "BULLISH"],
                    help="RSI tier from the pre-market scan")
    ap.add_argument("--sector", default=None, help="Sector name (e.g. Technology) for P2")
    ap.add_argument("--capital", type=float, default=None)
    ap.add_argument("--live-price", type=float, default=None,
                    help="Override entry with a live execution price")
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
    r = score_ticker(
        args.ticker.upper(),
        tier=args.tier,
        sector_name=args.sector,
        capital=args.capital,
        live_price=live_price,
    )
    print(json.dumps(asdict(r), indent=2, default=str))


if __name__ == "__main__":
    main()
