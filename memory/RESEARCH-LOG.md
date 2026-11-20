# Research Log — Last Run: 2026-11-20 04:42 ET (pre-market)
*(The scheduled run started early, at about 04:42 ET. Macro data is the latest available: the Thu 2026-11-19 close plus overnight.)*

> This file is **overwritten on every pre-market run**. Git history is the archive.
> The market-open routine checks that the "Last Run" date matches today before it proceeds.

---

## Account Snapshot
- Equity: $100,000.00 (paper, PA3FLRNK3PUG, ACTIVE)
- Cash: $100,000.00 | Buying power: $400,000.00
- Open P&L: $0.00 (no open positions)
- Market clock: closed now; opens 2026-11-20 09:30 ET (regular trading day)
- Trading mode: PAPER

---

## Global Gate (P1) — ❌ FAILED (NEGATIVE)

| Indicator | Value | Threshold | Status |
|-----------|-------|-----------|--------|
| SPX Monthly RSI | 63.65 | > 60 | ✓ but falling fast (was 67.45 yesterday) |
| SPX Weekly RSI | 40.14 | > 60 | ✗ At the bottom of the sideways zone (40–60), down from 44.10 |
| VIX | 29.13 | < 18 normal / > 25 danger | ✗ **Danger zone** (was 22.28 yesterday, +6.9 pts) |
| DXY 20d change | +1.82% (DXY 103.82) | < 3% | ✓ |
| 10Y Yield | 5.052% (+6.4bp / 20d) | not surging | ⚠ Above 5%, a headwind |
| SPX Price | 7,175.83 | — | -2.0% vs yesterday's log (7,323.63) |

**Verdict: NEGATIVE → Global gate FAILED. No scanning today and no trades.**
Reason: the SPX weekly RSI of 40.1 is far below 60, and the VIX of 29.1 is above the 25 danger level. Under the Part 3 decision rule, two or more bearish signals mean SKIP ALL TRADES. Conditions worsened sharply since yesterday: SPX fell about 2%, the VIX jumped about 7 points, and the monthly RSI fell almost 4 points toward the 60 line.

---

## Event Risk
- Next FOMC: Dec 8–9, 2026. Not within 3 days.
- No other events were checked for this routine, because the gate failed.

---

## Risk Factors
- Risk-off move: the VIX is in the danger zone and the SPX weekly RSI is about to drop below 40 (bearish zone). If the SPX monthly RSI drops below 60, the higher-timeframe structure breaks as well.
- The 10Y yield is still above 5%.
- There are no held positions, so none is below -7%.
- **State gap (carried over):** each scheduled run commits to its own branch, so the TRADE-LOG.md watchlist and weekly tracker date from 2026-09-21. This run started from the 2026-11-19 run's branch so the research history continues. The watchlist was not re-scored because the gate failed.

---

## Scanner Output
Not run because the global gate failed.

---

## Today's Entry Plan
Trade/hold decision: **HOLD. The global gate failed, so no setups were evaluated.**
Market-open routine: place no orders today.
