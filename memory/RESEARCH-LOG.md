# Research Log — Last Run: 2026-11-16 04:42 ET (pre-market)
*(Scheduled run, executed before the US open. Market opens 09:30 ET today (Alpaca clock). Macro data reflects Friday 2026-11-13 close.)*

> This file is **overwritten on every pre-market run**. Git history is the archive.
> Market-open routine validates the "Last Run" date matches today before proceeding.

---

## Account Snapshot
- Equity: $100,000.00 (paper, ACTIVE, `is_paper: true`)
- Cash: $100,000.00 | Buying power: $400,000.00
- Open P&L: $0.00. Alpaca shows no open positions, which matches TRADE-LOG.md.
- Weekly entries: 0 / 3 (new week of 2026-11-16) | Open positions: 0 / 5
- Trading mode: PAPER

---

## Global Gate (P1) — ❌ FAILED (NEGATIVE)

| Indicator | Value | Strategy threshold (Part 3) | Status |
|-----------|-------|-----------------------------|--------|
| SPX Monthly RSI | 74.62 | > 60 | ✓ |
| SPX Weekly RSI | 52.44 | > 60 | ✗ Sideways zone (40–60), down from 63.95 on 2026-09-21 |
| VIX | 20.05 | < 15 bullish / > 20 bearish (danger > 25) | ✗ Above 20, in caution band |
| DXY 20d change | +1.70% | < 3% | ✓ |
| US 10Y yield | 5.154% (+1.8bp / 20d) | stable / not spiking | ⚠ Above 5% (last run said to re-evaluate the gate if 10Y holds above 5%) |
| SPX price | 7,561.67 | — | Down about 2.4% from 7,746.96 on 2026-09-21 |

**Verdict: NEGATIVE. No scanning today, no trades.**
Two Layer-1 indicators are bearish: Weekly RSI is below 60 and VIX is above 20. The 10Y yield above 5% adds a third soft headwind. Part 3 says that if any 2 are bearish, skip all trades.

> Note: `tools/rsi_scan.py` has its own looser built-in gate (`spx_w > 50 and vix < 25`). That gate would pass today, at W-RSI 52.44 and VIX 20.05. This log follows the strategy spec, `memory/TRADING-STRATEGY.md` Part 3, which takes precedence. The scanner gate should be aligned to Weekly RSI > 60 in a future code change.

---

## Event Risk
- No FOMC decision is expected within 3 days. The next meeting is expected in early-to-mid December; confirm before entering.
- Gate failed, so no per-ticker earnings check was done.

---

## Risk Factors
- The weekly trend has turned down. SPX Weekly RSI fell from about 64 to 52, a possible Bearish Range Shift starting on the weekly. Watch whether it gets capped at 60 on the next bounce.
- Rates: 10Y yield is above 5% and the Fed is in a tightening cycle. This is a headwind for growth and long-duration names, which fill most of the watchlist (Tech).
- **State gap:** the last committed run before this one was 2026-09-21. Watchlist scores in TRADE-LOG.md are about 8 weeks old and should not be relied on. They were not rescored today because the gate failed.
- No held positions, so none are below -7%.

---

## Scanner Output
Not run: global gate failed.

---

## Today's Entry Plan
**Trade/hold decision: HOLD (gate FAILED — no setups evaluated).**
The market-open routine should place no orders today.
