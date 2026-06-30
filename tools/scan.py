"""
scan.py — Pre-market universe scanner orchestrator.

Workflow (matches agents/prompts/01_pre_market.md):
  1. Evaluate the global gate once (shared across all tickers).
  2. If gate not POSITIVE -> stop, report.
  3. Pre-screen every universe ticker cheaply (monthly RSI > 60, weekly RSI > 60,
     daily RSI in [scan band]).
  4. Fully score survivors with the 12-parameter engine.
  5. Classify into Active (>=86) / Watchlist (65-85) / Skip, rank by score.
  6. Print a JSON report the agent turns into a research log.

Usage:
    python tools/scan.py                # scan full universe
    python tools/scan.py --limit 30     # cap tickers (faster smoke test)
    python tools/scan.py --sector Technology   # one sector only
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from dataclasses import asdict

import market_data as md
import strategy_scorer as ss

CONFIG_DIR = os.path.join(os.path.dirname(__file__), "..", "config")


def load_universe() -> dict:
    with open(os.path.join(CONFIG_DIR, "universe.json")) as f:
        u = json.load(f)
    return {k: v for k, v in u.items() if not k.startswith("_")}


def prescreen(a: md.TickerAnalysis, filters: dict) -> bool:
    """Cheap filter before full scoring."""
    if not a.ok:
        return False
    return (
        a.monthly_rsi >= filters["monthly_rsi_min"]
        and a.weekly_rsi >= filters["weekly_rsi_min"]
        and filters["daily_rsi_min"] <= a.daily_rsi <= filters["daily_rsi_max"]
    )


def main():
    ap = argparse.ArgumentParser(description="Pre-market scanner")
    ap.add_argument("--limit", type=int, default=None, help="Max tickers to scan")
    ap.add_argument("--sector", default=None, help="Restrict to one sector")
    ap.add_argument("--relax", action="store_true",
                    help="Widen the daily-RSI prescreen band (diagnostic)")
    args = ap.parse_args()

    cfg = ss.load_config()
    capital = float(cfg["trading"].get("total_capital", 100000))
    filters = dict(cfg["market"]["scanner_filters"])
    if args.relax:
        filters["daily_rsi_min"] = 30
        filters["daily_rsi_max"] = 60

    # --- Global gate (once) ---
    macro = md.macro_snapshot()
    outlook = ss.evaluate_global_outlook(cfg, macro)

    report = {
        "outlook": outlook["outlook"],
        "gate_passed": outlook["gate_passed"],
        "macro": macro,
        "gate_checks": outlook["checks"],
        "scanned": 0,
        "prescreen_passed": [],
        "active": [],
        "watchlist": [],
        "skipped_or_dq": [],
    }

    if not outlook["gate_passed"]:
        report["message"] = f"Global gate {outlook['outlook']} — no scanning."
        print(json.dumps(report, indent=2, default=str))
        return

    # --- Build ticker list ---
    universe = load_universe()
    if args.sector:
        universe = {args.sector: universe.get(args.sector, [])}
    pairs = [(sym, sector) for sector, syms in universe.items() for sym in syms]
    if args.limit:
        pairs = pairs[: args.limit]

    for sym, sector in pairs:
        report["scanned"] += 1
        a = md.analyze_ticker(sym)
        if not prescreen(a, filters):
            continue
        report["prescreen_passed"].append(
            {"symbol": sym, "sector": sector, "m_rsi": a.monthly_rsi,
             "w_rsi": a.weekly_rsi, "d_rsi": a.daily_rsi}
        )
        r = ss.score_ticker(sym, sector, macro=macro, capital=capital)
        if not r.ok:
            continue
        entry = {
            "symbol": sym,
            "sector": sector,
            "score": r.score,
            "decision": r.decision,
            "passed": list(r.passed.keys()),
            "failed": list(r.failed.keys()),
            "disqualifiers": r.disqualifiers,
            "p8_entry_ok": r.p8_entry_ok,
            "trade_plan": r.trade_plan,
        }
        if r.decision == "ENTER_FULL":
            report["active"].append(entry)
        elif r.decision == "WATCHLIST_HALF":
            report["watchlist"].append(entry)
        else:
            report["skipped_or_dq"].append(
                {"symbol": sym, "score": r.score, "decision": r.decision,
                 "disqualifiers": r.disqualifiers}
            )

    report["active"].sort(key=lambda x: x["score"], reverse=True)
    report["watchlist"].sort(key=lambda x: x["score"], reverse=True)

    print(json.dumps(report, indent=2, default=str))


if __name__ == "__main__":
    main()
