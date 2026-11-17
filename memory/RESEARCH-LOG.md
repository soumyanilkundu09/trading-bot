# Research Log — Last Run: 2026-11-17 04:42 ET (pre-market)
*(Scheduled run fired early, ~04:42 ET. Macro data = latest available (Mon 2026-11-16 close / overnight).)*

> This file is **overwritten on every pre-market run**. Git history is the archive.
> Market-open routine validates the "Last Run" date matches today before proceeding.

---

## Account Snapshot
- Equity: $100,000.00 (paper, PA3FLRNK3PUG, ACTIVE)
- Cash: $100,000.00 | Buying power: $400,000.00
- Open P&L: $0.00 (no open positions)
- Market clock: closed now; opens 2026-11-17 09:30 ET (regular trading day)

---

## Global Gate (P1) — ❌ FAILED (NEGATIVE)

| Indicator | Value | Threshold | Status |
|-----------|-------|-----------|--------|
| SPX Monthly RSI | 70.08 | > 60 | ✓ |
| SPX Weekly RSI | 47.02 | > 60 | ✗ — sideways zone (40–60); was 63.95 on 2026-09-21 |
| VIX | 24.17 | < 18 normal / > 25 danger | ⚠ Caution band (18–25), near danger |
| DXY 20d change | +1.67% | < 3% | ✓ |
| 10Y Yield | 5.121% (+0.4bp / 20d) | not surging | ⚠ Above 5% — elevated headwind |
| SPX Price | 7,416.59 | — | ~-4.3% vs 2026-09-21 log (7,746.96) |

**Verdict: NEGATIVE → Global gate FAILED — no scanning today, no trades.**
Reason: SPX weekly RSI 47.0 < 60 (hard fail of the Weekly RSI leg), plus VIX in the caution band at 24.2 and the 10Y above 5%. Two or more bearish/indecisive signals → Part 3 decision rule = SKIP ALL TRADES.

---

## Event Risk
- Next FOMC: Dec 8–9, 2026 — not within 3 days.
- No other routine-relevant events checked, since the gate failed.

---

## Risk Factors
- Benchmark weekly RSI has dropped into the sideways zone (40–60). Do not open new longs until SPX weekly RSI is back above 60 and VIX is back below 18–25.
- VIX at 24.2 is close to the 25 danger threshold.
- No held positions, so nothing is below -7%.
- **State gap:** the last committed run before this one was 2026-09-21. TRADE-LOG.md watchlist and weekly tracker are ~8 weeks stale. The watchlist was not re-scored today because the gate failed. The daily-summary/weekly-review runs should refresh it once the gate passes.

---

## Scanner Output
Not run — global gate failed.

---

## Today's Entry Plan
Trade/hold decision: **HOLD — global gate failed, no setups evaluated.**
Market-open routine: place no orders today.
