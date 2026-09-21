"""
rsi_scan.py — Three-tier RSI pre-market scanner (Malkan GFS simplified entry screen).

Classifies every ticker in the expanded universe into three tiers:

  EXTREMELY_BULLISH_PULLBACK:
    - Monthly RSI > 60
    - Weekly RSI > 60 AND <= 65  (trending but not extended)
    - Daily RSI 39–45  OR  daily Bullish Range Shift

  EXTREMELY_BULLISH_MOMENTUM:
    - Monthly RSI > 60
    - Weekly RSI > 60 (no upper cap)
    - Daily RSI 59–65  (no BRS alternative)

  BULLISH:
    - Monthly RSI > 60
    - Weekly RSI > 40 AND < 60   (neutral zone, approaching bullish)
    - Daily RSI 39–45  OR  daily Bullish Range Shift

No other parameters (volume, sector, resistance, etc.) are evaluated here.
The global gate (P1) is checked once at the top — if it fails, scan is skipped.

Usage:
    python tools/rsi_scan.py                  # S&P 500 + universe.json
    python tools/rsi_scan.py --no-sp500       # universe.json only
    python tools/rsi_scan.py --workers 12     # more parallel threads
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed

# Allow running directly from the tools/ directory
sys.path.insert(0, os.path.dirname(__file__))
import market_data as md

CONFIG_DIR = os.path.join(os.path.dirname(__file__), "..", "config")
UNIVERSE_FILE = os.path.join(CONFIG_DIR, "universe.json")


# --------------------------------------------------------------------------
# Universe helpers
# --------------------------------------------------------------------------

def load_universe_json() -> list[str]:
    """All tickers from universe.json (all sectors, deduplicated)."""
    with open(UNIVERSE_FILE) as f:
        data = json.load(f)
    tickers: list[str] = []
    for key, val in data.items():
        if not key.startswith("_") and isinstance(val, list):
            tickers.extend(val)
    return list(dict.fromkeys(tickers))


def fetch_sp500_tickers() -> list[str]:
    """
    Fetch S&P 500 constituents from Wikipedia.
    Requires: pandas + lxml (or html5lib).
    Returns empty list on any failure so the scan can continue with universe.json.
    """
    try:
        import io
        import urllib.request
        import pandas as pd
        req = urllib.request.Request(
            "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies",
            headers={"User-Agent": "Mozilla/5.0 (compatible; trading-bot-scanner/1.0)"},
        )
        with urllib.request.urlopen(req, timeout=15) as resp:
            html = resp.read().decode("utf-8")
        tables = pd.read_html(io.StringIO(html), attrs={"id": "constituents"})
        symbols = tables[0]["Symbol"].tolist()
        # Wikipedia uses dots (BRK.B); yfinance uses dashes (BRK-B)
        return [str(s).replace(".", "-") for s in symbols]
    except Exception as e:
        sys.stderr.write(f"[rsi_scan] Wikipedia S&P 500 fetch failed: {e}\n")
        sys.stderr.write("[rsi_scan] Falling back to universe.json only.\n")
        return []


def get_universe(sp500: bool = True) -> list[str]:
    """Merge universe.json with S&P 500 tickers (if sp500=True). Deduplicates."""
    local = load_universe_json()
    if not sp500:
        return local
    sp = fetch_sp500_tickers()
    return list(dict.fromkeys(local + sp))


# --------------------------------------------------------------------------
# Single-ticker classification
# --------------------------------------------------------------------------

def classify_ticker(symbol: str, market_gap_dates: set | None = None) -> dict:
    """
    Fetch RSI data for one ticker and classify into a tier.

    Returns a dict with keys:
      symbol, tier, price, monthly_rsi, weekly_rsi, daily_rsi, daily_brs
    tier is one of:
      EXTREMELY_BULLISH_PULLBACK | EXTREMELY_BULLISH_MOMENTUM | BULLISH | NONE | ERROR
    """
    try:
        a = md.analyze_ticker(symbol, market_gap_dates=market_gap_dates)
        if not a.ok:
            return {"symbol": symbol, "tier": "ERROR", "error": a.error}

        daily_brs = bool(a.range_shift_daily.get("bullish_range_shift"))
        daily_pullback_ok = (39 <= a.daily_rsi <= 45) or daily_brs
        daily_momentum_ok = (59 <= a.daily_rsi <= 65)
        monthly_ok = a.monthly_rsi > 60

        if not monthly_ok:
            tier = "NONE"
        elif 60 < a.weekly_rsi <= 65 and daily_pullback_ok:
            tier = "EXTREMELY_BULLISH_PULLBACK"
        elif a.weekly_rsi > 60 and daily_momentum_ok:
            tier = "EXTREMELY_BULLISH_MOMENTUM"
        elif 40 < a.weekly_rsi < 60 and daily_pullback_ok:
            tier = "BULLISH"
        else:
            tier = "NONE"

        # Entry filters — applied to EB Pullback and BULLISH; NOT to EB Momentum
        filter_reason = None
        if tier in ("EXTREMELY_BULLISH_PULLBACK", "BULLISH"):
            ef = a.entry_filter
            if ef.get("near_resistance"):
                tier = "NONE"
                filter_reason = f"near_resistance ({ef.get('dist_to_resistance_pct')}% to {ef.get('nearest_resistance')})"
            elif ef.get("has_gap_down_5d"):
                tier = "NONE"
                filter_reason = f"gap_down_5d (dates: {ef.get('gap_down_dates')})"

        return {
            "symbol": symbol,
            "tier": tier,
            "price": a.price,
            "monthly_rsi": a.monthly_rsi,
            "weekly_rsi": a.weekly_rsi,
            "daily_rsi": a.daily_rsi,
            "daily_brs": daily_brs,
            "daily_ok_reason": "brs" if (daily_brs and not (39 <= a.daily_rsi <= 45)) else "rsi_zone",
            **({"filter_reason": filter_reason} if filter_reason else {}),
        }
    except Exception as e:
        return {"symbol": symbol, "tier": "ERROR", "error": str(e)}


# --------------------------------------------------------------------------
# Orchestration
# --------------------------------------------------------------------------

def run_scan(tickers: list[str], workers: int = 8,
             market_gap_dates: set | None = None) -> dict:
    """
    Scan all tickers concurrently.

    Returns:
      {
        "EXTREMELY_BULLISH_PULLBACK": [...],
        "EXTREMELY_BULLISH_MOMENTUM": [...],
        "BULLISH": [...],
        "filtered": [...],   # passed RSI tiers but blocked by entry filters
        "total_scanned": N,
        "error_count": N,
      }
    sorted by weekly_rsi descending within each tier.
    """
    eb_pullback: list[dict] = []
    eb_momentum: list[dict] = []
    bull: list[dict] = []
    filtered: list[dict] = []
    errors: list[dict] = []
    done = 0
    total = len(tickers)

    with ThreadPoolExecutor(max_workers=workers) as ex:
        futures = {ex.submit(classify_ticker, t, market_gap_dates): t for t in tickers}
        for fut in as_completed(futures):
            done += 1
            r = fut.result()
            tier = r.get("tier", "NONE")
            if tier == "EXTREMELY_BULLISH_PULLBACK":
                eb_pullback.append(r)
            elif tier == "EXTREMELY_BULLISH_MOMENTUM":
                eb_momentum.append(r)
            elif tier == "BULLISH":
                bull.append(r)
            elif tier == "ERROR":
                errors.append(r)
            elif r.get("filter_reason"):
                filtered.append(r)
            if done % 25 == 0 or done == total:
                sys.stderr.write(f"[rsi_scan] {done}/{total} scanned\n")

    eb_pullback.sort(key=lambda x: x.get("weekly_rsi", 0), reverse=True)
    eb_momentum.sort(key=lambda x: x.get("weekly_rsi", 0), reverse=True)
    bull.sort(key=lambda x: x.get("weekly_rsi", 0), reverse=True)
    filtered.sort(key=lambda x: x.get("weekly_rsi", 0), reverse=True)

    return {
        "EXTREMELY_BULLISH_PULLBACK": eb_pullback,
        "EXTREMELY_BULLISH_MOMENTUM": eb_momentum,
        "BULLISH": bull,
        "filtered": filtered,
        "total_scanned": total,
        "error_count": len(errors),
        "errors": errors,
    }


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(
        description="Three-tier RSI scanner — EB Pullback / EB Momentum / Bullish"
    )
    ap.add_argument(
        "--no-sp500",
        action="store_true",
        help="Skip S&P 500 Wikipedia fetch; use universe.json only",
    )
    ap.add_argument(
        "--workers",
        type=int,
        default=8,
        help="Parallel threads for ticker analysis (default: 8)",
    )
    ap.add_argument(
        "--no-gate",
        action="store_true",
        help="Skip P1 global gate check (for testing)",
    )
    args = ap.parse_args()

    # P1 global gate — if market isn't POSITIVE, skip scan
    if not args.no_gate:
        sys.stderr.write("[rsi_scan] Checking global gate (P1)...\n")
        macro = md.macro_snapshot()
        vix = macro.get("vix", 99)
        spx_m = macro.get("sp500_monthly_rsi", 0)
        spx_w = macro.get("sp500_weekly_rsi", 0)
        dxy = macro.get("dxy_20d_change_pct", 0)
        gate_ok = spx_m > 60 and spx_w > 50 and vix < 25 and dxy < 3.0
        if not gate_ok:
            result = {
                "gate_passed": False,
                "gate_reason": f"SPX_M={spx_m} SPX_W={spx_w} VIX={vix} DXY_20d={dxy}%",
                "EXTREMELY_BULLISH_PULLBACK": [],
                "EXTREMELY_BULLISH_MOMENTUM": [],
                "BULLISH": [],
                "filtered": [],
                "total_scanned": 0,
                "error_count": 0,
            }
            print(json.dumps(result, indent=2))
            return
        sys.stderr.write(
            f"[rsi_scan] Gate PASSED — SPX_M={spx_m} SPX_W={spx_w} VIX={vix}\n"
        )

    tickers = get_universe(sp500=not args.no_sp500)
    sys.stderr.write(f"[rsi_scan] Universe: {len(tickers)} tickers\n")

    sys.stderr.write("[rsi_scan] Fetching market-wide gap dates (SPY)...\n")
    market_gap_dates = md.get_market_gap_down_dates()
    if market_gap_dates:
        sys.stderr.write(f"[rsi_scan] Market-wide gap days (excluded from stock filter): {sorted(market_gap_dates)}\n")

    results = run_scan(tickers, workers=args.workers, market_gap_dates=market_gap_dates)
    results["gate_passed"] = True

    print(json.dumps(results, indent=2))

    # Human-readable summary to stderr
    sys.stderr.write(
        f"\n=== RSI SCAN RESULTS ===\n"
        f"EXTREMELY BULLISH PULLBACK ({len(results['EXTREMELY_BULLISH_PULLBACK'])} stocks):\n"
    )
    for r in results["EXTREMELY_BULLISH_PULLBACK"]:
        brs_tag = " [BRS]" if r.get("daily_brs") else ""
        sys.stderr.write(
            f"  {r['symbol']:8s}  M={r['monthly_rsi']:5.1f}  W={r['weekly_rsi']:5.1f}  D={r['daily_rsi']:5.1f}{brs_tag}\n"
        )
    sys.stderr.write(f"\nEXTREMELY BULLISH MOMENTUM ({len(results['EXTREMELY_BULLISH_MOMENTUM'])} stocks):\n")
    for r in results["EXTREMELY_BULLISH_MOMENTUM"]:
        sys.stderr.write(
            f"  {r['symbol']:8s}  M={r['monthly_rsi']:5.1f}  W={r['weekly_rsi']:5.1f}  D={r['daily_rsi']:5.1f}\n"
        )
    sys.stderr.write(f"\nBULLISH ({len(results['BULLISH'])} stocks):\n")
    for r in results["BULLISH"]:
        brs_tag = " [BRS]" if r.get("daily_brs") else ""
        sys.stderr.write(
            f"  {r['symbol']:8s}  M={r['monthly_rsi']:5.1f}  W={r['weekly_rsi']:5.1f}  D={r['daily_rsi']:5.1f}{brs_tag}\n"
        )
    sys.stderr.write(f"\nFILTERED OUT — passed RSI but blocked by entry filters ({len(results['filtered'])} stocks):\n")
    for r in results["filtered"]:
        sys.stderr.write(
            f"  {r['symbol']:8s}  M={r['monthly_rsi']:5.1f}  W={r['weekly_rsi']:5.1f}  D={r['daily_rsi']:5.1f}  reason={r.get('filter_reason','?')}\n"
        )
    sys.stderr.write(
        f"\nScanned: {results['total_scanned']}  Errors: {results['error_count']}  Filtered: {len(results['filtered'])}\n"
    )


if __name__ == "__main__":
    main()
