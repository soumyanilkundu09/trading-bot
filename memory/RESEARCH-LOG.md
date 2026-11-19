# Research Log — Last Run: 2026-11-19 04:43 ET (pre-market)
*(The scheduled run started early, at about 04:43 ET. Macro data is the latest available: the Wed 2026-11-18 close plus overnight.)*

> This file is **overwritten on every pre-market run**. Git history is the archive.
> The market-open routine checks that the "Last Run" date matches today before it proceeds.

---

## Account Snapshot
- Equity: $100,000.00 (paper, PA3FLRNK3PUG, ACTIVE)
- Cash: $100,000.00 | Buying power: $400,000.00
- Open P&L: $0.00 (no open positions)
- Market clock: closed now; opens 2026-11-19 09:30 ET (regular trading day)
- Trading mode: PAPER

---

## Global Gate (P1) — ❌ FAILED (NEGATIVE)

| Indicator | Value | Threshold | Status |
|-----------|-------|-----------|--------|
| SPX Monthly RSI | 67.45 | > 60 | ✓ (was 67.91 yesterday) |
| SPX Weekly RSI | 44.10 | > 60 | ✗ Sideways zone (40–60), down from 44.60 yesterday |
| VIX | 22.28 | < 18 normal / > 25 danger | ⚠ Caution band (18–25); down from 23.62 |
| DXY 20d change | +1.86% (DXY 103.7) | < 3% | ✓ (was +2.15% yesterday) |
| 10Y Yield | 5.066% (+11.3bp / 20d) | not surging | ⚠ Above 5% and rising over 20 days, a headwind |
| SPX Price | 7,323.63 | — | -0.2% vs yesterday's log (7,340.53) |

**Verdict: NEGATIVE → Global gate FAILED. No scanning today and no trades.**
Reason: the SPX weekly RSI of 44.1 is below 60, which fails the weekly leg outright. The VIX is in the caution band at 22.3, and the 10Y yield is above 5% and rising. Under the Part 3 decision rule, two or more bearish or indecisive signals mean SKIP ALL TRADES. The weekly RSI drifted lower again; the VIX and DXY eased a little.

---

## Event Risk
- Next FOMC: Dec 8–9, 2026. Not within 3 days.
- No other events were checked for this routine, because the gate failed.

---

## Risk Factors
- The benchmark weekly RSI is still falling in the sideways zone (44.6 → 44.1). The monthly RSI is easing (67.9 → 67.5) but still above 60. Do not open new longs until the SPX weekly RSI is back above 60 and the VIX is back below 18–25.
- The 10Y yield is above 5% and up 11bp over 20 days.
- There are no held positions, so none is below -7%.
- **State gap (carried over):** each scheduled run commits to its own branch, so the TRADE-LOG.md watchlist and weekly tracker date from 2026-09-21. This run started from the 2026-11-18 run's branch so the research history continues. The watchlist was not re-scored because the gate failed.

---

## Scanner Output
Not run because the global gate failed.

---

## Today's Entry Plan
Trade/hold decision: **HOLD. The global gate failed, so no setups were evaluated.**
Market-open routine: place no orders today.
