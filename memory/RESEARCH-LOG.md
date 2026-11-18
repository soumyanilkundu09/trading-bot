# Research Log — Last Run: 2026-11-18 04:43 ET (pre-market)
*(The scheduled run started early, at about 04:43 ET. Macro data is the latest available: the Tue 2026-11-17 close plus overnight.)*

> This file is **overwritten on every pre-market run**. Git history is the archive.
> The market-open routine checks that the "Last Run" date matches today before it proceeds.

---

## Account Snapshot
- Equity: $100,000.00 (paper, PA3FLRNK3PUG, ACTIVE)
- Cash: $100,000.00 | Buying power: $400,000.00
- Open P&L: $0.00 (no open positions)
- Market clock: closed now; opens 2026-11-18 09:30 ET (regular trading day)
- Trading mode: PAPER

---

## Global Gate (P1) — ❌ FAILED (NEGATIVE)

| Indicator | Value | Threshold | Status |
|-----------|-------|-----------|--------|
| SPX Monthly RSI | 67.91 | > 60 | ✓ (was 70.08 yesterday) |
| SPX Weekly RSI | 44.60 | > 60 | ✗ Sideways zone (40–60), down from 47.02 yesterday |
| VIX | 23.62 | < 18 normal / > 25 danger | ⚠ Caution band (18–25) |
| DXY 20d change | +2.15% (DXY 103.8) | < 3% | ✓ but rising (+1.67% yesterday) |
| 10Y Yield | 5.103% (-4.3bp / 20d) | not surging | ⚠ Above 5%, which is a headwind (not surging) |
| SPX Price | 7,340.53 | — | -1.0% vs yesterday's log (7,416.59) |

**Verdict: NEGATIVE → Global gate FAILED. No scanning today and no trades.**
Reason: the SPX weekly RSI of 44.6 is below 60, which fails the weekly leg outright. The VIX is in the caution band at 23.6, and the 10Y yield is above 5%. Under the Part 3 decision rule, two or more bearish or indecisive signals mean SKIP ALL TRADES. The weekly RSI is getting worse.

---

## Event Risk
- Next FOMC: Dec 8–9, 2026. Not within 3 days.
- No other events were checked for this routine, because the gate failed.

---

## Risk Factors
- The benchmark weekly RSI is falling deeper into the sideways zone (47.0 → 44.6). The monthly RSI is also easing (70.1 → 67.9). Do not open new longs until the SPX weekly RSI is back above 60 and the VIX is back below 18–25.
- The DXY 20-day change is rising toward the 3% risk-off threshold.
- There are no held positions, so none is below -7%.
- **State gap (carried over):** each scheduled run commits to its own branch, so the TRADE-LOG.md watchlist and weekly tracker on this branch date from 2026-09-21. The watchlist was not re-scored because the gate failed.

---

## Scanner Output
Not run because the global gate failed.

---

## Today's Entry Plan
Trade/hold decision: **HOLD. The global gate failed, so no setups were evaluated.**
Market-open routine: place no orders today.
