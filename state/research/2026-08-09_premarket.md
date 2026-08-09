# Pre-Market Research — 2026-08-09 (Sun)

**Run:** Pre-market scan (manual — market closed today, next open Mon 2026-08-10 09:30 ET; run performed as prep for Monday)
**Trading mode:** PAPER
**Global outlook:** ✅ **POSITIVE** — gate PASSED

## Global Market Gate (P1 — mandatory)

| Indicator | Value | Check |
|-----------|-------|-------|
| S&P 500 Monthly RSI | 70.75 | ✅ > 60 |
| S&P 500 Weekly RSI | 67.53 | ✅ healthy |
| CBOE VIX | 14.90 | ✅ < 18 (calm) |
| DXY 20d change | −1.66% | ✅ not spiking |
| US 10Y yield | 4.66% (Δ20d +0.05) | ✅ stable |

**Verdict:** Bullish risk-taking supported. Proceed to scan.

## Event Risk Check
- FOMC: last meeting Jul 28–29, 2026 (decision Jul 29). Next meeting expected ~mid-September 2026 (~6 weeks out per regular 8-meeting cadence). **No Fed decision within 3 days.**
- No other major macro event flagged.

## Scan Result (universe = 100 liquid S&P 500 / Nasdaq 100 names, config/universe.json)

- **Pre-screen filter used:** `config/market_config.json.scanner_filters` — Monthly RSI ≥ 60, Weekly RSI ≥ 40, Daily RSI 35–48.
- **Pre-screen survivors (7):** AAPL, AMD, MU, WMT, ABBV, CAT, PLD
- Remaining 93 names: mostly extended above the daily-40 pullback zone (index near highs) or failing the monthly/weekly trend filter.
- Existing watchlist name **TXN** re-scored for currency (see below).

### ✅ Active Trade List (score ≥ 80)
_None this session._

### ⚠️ Watchlist (65–79)
_None this session._

### ❌ Disqualified / Skipped

| Ticker | Sector | Score | Key Passed | Key Failed / Disqualifier |
|--------|--------|-------|-----------|---------------------------|
| AAPL | Technology | 62 | P2,P4,P5,P6,P7,P8,P12 | P9 (0.69% to resistance), P11 (RSI 47.6, not at 40), **Bearish Divergence near resistance**, **P10 red candles high-vol** |
| PLD | Real_Estate | 58 | P4,P5,P7,P8,P11,P12 | P2 (sector weak), P6, P9, **P10 red candles high-vol** |
| ABBV | Healthcare | 56 | P2,P4,P5,P6,P7,P12 | P8, P9, P11, **Bearish Divergence near resistance**, **P10 high-vol** |
| TXN (watchlist) | Technology | 54 | P2,P4,P5,P7,P8,P12 | P6, P9 (3.57%), P11 (RSI 49.97), **P10 high-vol** — dropped from 98 (2026-06-30); no longer qualifies |
| CAT | Industrials | 40 | P2,P4,P6,P11 | P5,P7,P8,P9 (0.32% to resistance), **P10 high-vol** |
| MU | Technology | 48 | P2,P4,P5,P7,P9 | P6,P8,P11, **P10 high-vol** |
| AMD | Technology | 38 | P2,P4,P5,P9 | P6,P7,P8,P10,P11,P12 |
| WMT | Consumer_Staples | 42 | P4,P5,P6,P7,P8 | P2 (sector weak), P9, P11, **Bearish Range Shift on Weekly**, **P10 high-vol** |

## Notable Market Observation
Every one of the 8 names scored triggered the **P10 disqualifier — last 3–4 red candles on above-average volume** (conviction selling), and two (AAPL, ABBV) also show Bearish Divergence near resistance. Despite a technically POSITIVE global gate (low VIX, high benchmark RSI), this is a broad, fairly uniform distribution/pullback signature across sectors — not isolated to one name. Worth treating as a caution flag: the index-level strength is not being confirmed by clean accumulation at the single-stock level right now.

## Watchlist Update
- **TXN** removed from Active Watchlist — re-scored 54 (below 65 threshold), disqualified on P10. No longer an actionable setup; will re-screen in future runs if it resets.
- No new names qualify for the watchlist this session.

## Notes for Market-Open Job
- **No Active Trade List candidates** — market-open job should take **no entries** based on this scan.
- Weekly budget: 0/3 used. Open positions: 0/5.
- If Monday's pre-open action clears any of AAPL/PLD/ABBV back through P9/P10/P11, they're the closest to watchlist-worthy (56–62) and worth a quick re-check.
