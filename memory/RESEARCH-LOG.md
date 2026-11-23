# Research Log — Last Run: 2026-11-23 04:42 ET (pre-market)
*(The scheduled run started early, at about 04:42 ET. Macro data is the latest available: the Fri 2026-11-20 close plus overnight.)*

> This file is **overwritten on every pre-market run**. Git history is the archive.
> The market-open routine checks that the "Last Run" date matches today before it proceeds.

---

## Account Snapshot
- Equity: $100,000.00 (paper, PA3FLRNK3PUG, ACTIVE)
- Cash: $100,000.00 | Buying power: $400,000.00
- Open P&L: $0.00 (no open positions)
- Market clock: closed now; opens 2026-11-23 09:30 ET (regular trading day)
- Trading mode: PAPER

---

## Global Gate (P1) — ❌ FAILED (NEGATIVE)

| Indicator | Value | Threshold | Status |
|-----------|-------|-----------|--------|
| SPX Monthly RSI | 57.80 | > 60 | ✗ **Below 60** (was 63.65 on 11-20). The higher-timeframe bullish structure has broken |
| SPX Weekly RSI | 34.56 | > 60 | ✗ **In the bearish zone (< 40)**, down from 40.14 |
| VIX | 30.34 | < 18 normal / > 25 danger | ✗ **Danger zone** (was 29.13) |
| DXY 20d change | +1.41% (DXY 103.76) | < 3% | ✓ |
| 10Y Yield | 4.912% (-7.4bp / 20d) | not surging | ✓ Eased back below 5% |
| SPX Price | 6,910.39 | — | -3.7% vs the 11-20 log (7,175.83) |

**Verdict: NEGATIVE → Global gate FAILED. No scanning today and no trades.**
Reason: three bearish signals. The SPX monthly RSI of 57.8 is below 60, the SPX weekly RSI of 34.6 is in the bearish zone, and the VIX of 30.3 is above the 25 danger level. Under the Part 3 decision rule, two or more bearish signals mean SKIP ALL TRADES. The P1 hard gate (benchmark monthly RSI > 60) also fails on its own.

---

## Event Risk
- Thanksgiving week: US markets are closed Thu 2026-11-26 and close early (13:00 ET) on Fri 2026-11-27. Liquidity will be thin.
- Next FOMC: Dec 8–9, 2026. Not within 3 days.
- No other events were checked for this routine, because the gate failed.

---

## Risk Factors
- The risk-off move has deepened. The SPX monthly RSI has now lost 60, so the monthly, weekly and VIX signals are all bearish. The gate is unlikely to recover quickly: the monthly RSI has to get back above 60 and the weekly RSI has to climb about 25 points.
- There are no held positions, so none is below -7%.
- **State gap (carried over):** each scheduled run commits to its own branch, so the TRADE-LOG.md watchlist and weekly tracker date from 2026-09-21. This run started from the 2026-11-20 run's branch so the research history continues. The watchlist was not re-scored because the gate failed.

---

## Scanner Output
Not run because the global gate failed.

---

## Today's Entry Plan
Trade/hold decision: **HOLD. The global gate failed, so no setups were evaluated.**
Market-open routine: place no orders today.
