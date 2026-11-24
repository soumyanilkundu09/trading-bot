# Research Log — Last Run: 2026-11-24 04:42 ET (pre-market)
*(The scheduled run started early, at about 04:42 ET. Macro data is the latest available: the Mon 2026-11-23 close plus overnight.)*

> This file is **overwritten on every pre-market run**. Git history is the archive.
> The market-open routine checks that the "Last Run" date matches today before it proceeds.

---

## Account Snapshot
- Equity: $100,000.00 (paper, PA3FLRNK3PUG, ACTIVE)
- Cash: $100,000.00 | Buying power: $400,000.00
- Open P&L: $0.00 (no open positions)
- Market clock: closed now; opens 2026-11-24 09:30 ET (regular trading day)
- Trading mode: PAPER

---

## Global Gate (P1) — ❌ FAILED (NEGATIVE)

| Indicator | Value | Threshold | Status |
|-----------|-------|-----------|--------|
| SPX Monthly RSI | 65.17 | > 60 | ✓ Back above 60 (was 57.80 on 11-23) |
| SPX Weekly RSI | 44.74 | > 60 | ✗ **Below 60**. Up from 34.56 but the weekly structure is not bullish |
| VIX | 27.52 | < 18 normal / > 25 danger | ✗ **Danger zone** (was 30.34) |
| DXY 20d change | +2.0% (DXY 104.24) | < 3% | ✓ Rising, but under the spike threshold |
| 10Y Yield | 4.918% (-7.5bp / 20d) | not surging | ✓ |
| SPX Price | 7,237.17 | — | +4.7% vs the 11-23 log (6,910.39) |

**Verdict: NEGATIVE → Global gate FAILED. No scanning today and no trades.**
Reason: two bearish signals. The SPX weekly RSI of 44.7 is below 60, and the VIX of 27.5 is above the 25 danger level. Under the Part 3 decision rule, two or more bearish signals mean SKIP ALL TRADES. The P1 check (VIX below threshold) also fails on its own.

---

## Event Risk
- Thanksgiving week: US markets are closed Thu 2026-11-26 and close early (13:00 ET) on Fri 2026-11-27. Liquidity will be thin.
- Next FOMC: Dec 8–9, 2026. Not within 3 days.
- No other events were checked for this routine, because the gate failed.

---

## Risk Factors
- The market bounced sharply: SPX is up about 4.7% and the monthly RSI is back above 60. Fear is still high, though (VIX 27.5), and the weekly RSI has to climb about 15 points to clear 60. One strong session does not confirm the trend has recovered.
- DXY is up 2.0% over 20 days and still rising. It is under the 3% threshold, but worth watching.
- There are no held positions, so none is below -7%.
- **State gap (carried over):** each scheduled run commits to its own branch, so the TRADE-LOG.md watchlist and weekly tracker date from 2026-09-21. This run started from the 2026-11-23 run's branch so the research history continues. The watchlist was not re-scored because the gate failed.

---

## Scanner Output
Not run because the global gate failed.

---

## Today's Entry Plan
Trade/hold decision: **HOLD. The global gate failed, so no setups were evaluated.**
Market-open routine: place no orders today.
