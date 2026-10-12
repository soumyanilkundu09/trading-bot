# Research Log — Last Run: 2026-10-12 05:50 ET (pre-market)

> Overwritten on every pre-market run. Scanner data = Friday 2026-10-09 close (no live quote pass in this routine). Note: Mon Oct 12 is Columbus Day — US equity market is OPEN.

## Account Snapshot
- Equity $100,000.00 (paper, PA3FLRNK3PUG) | Cash $100,000 | Buying power $400,000
- Open P&L $0.00 | Open positions 0 / 5 | Weekly entries 0 / 3 (new week of 2026-10-12)

## Global Gate (P1) — POSITIVE ✓ (macro caution)
| Indicator | Value | Status |
|---|---|---|
| SPX Monthly RSI | 80.42 | ✓ > 60 (extended) |
| SPX Weekly RSI | 65.55 | ✓ > 60 |
| VIX | 15.43 | ✓ < 18 |
| DXY 20d change | +2.69% | ⚠ near 3% limit (passes) |
| 10Y yield | 5.244% (+28bp / 20d) | ⚠ above 5%, still rising |
| SPX | 7,811.54 | |

**Verdict: POSITIVE — scan run.** Two soft warnings (DXY close to spike threshold, 10Y > 5% and rising) but no hard threshold breached; "any 2 bearish" rule judged not triggered. If DXY crosses +3% or yields keep surging, gate may fail at the next run.

## Event Risk
- Fed: last hike 2026-09-16 (3.75–4.00%); next FOMC Oct 27–28 — no Fed event within 3 days.
- **ASML Q3 results Oct 14** — semiconductor read-through risk for MRVL/AMAT/LRCX/AVGO within the holding window.
- Earnings (Part 7, within 5 trading days): MRVL none (est. Nov 26/Dec 1; investor day announced Oct 6), AMAT est. Nov 12, AVGO reported Sep 2, LRCX est. Oct 21 (7 trading days out; unconfirmed).

## Risk Factors
- **Scan universe degraded:** S&P 500 Wikipedia fetch failed (HTTP 403) → only `config/universe.json` (137 tickers) scanned, not ~503.
- Sector P2 (Weekly RSI >60): Technology 67.99 ✓, Energy 63.18 ✓, Healthcare 60.85 ✓. Fail: Financials 49.3, Consumer Staples 49.1, Consumer Disc. 46.6, Materials 44.1, Industrials 42.5, Real Estate 40.1.
- **Correlation:** all ENTER candidates are semiconductors, ahead of ASML earnings. Do not take more than 2 of them without human judgement; hard cap 3/week.
- Macro: Fed tightening cycle, 10Y > 5%, DXY +2.7%.
- No held positions.

## Scanner Output — 137 scanned, 0 errors, gate passed
(Score = scorer pts / max; ENTER at ≥6)

### EXTREMELY BULLISH PULLBACK
| Ticker | M/W/D RSI | Price | Score | Decision |
|---|---|---|---|---|
| MRK | 63.4 / 62.3 / 51.5 (BRS) | 145.57 | 5/10 | WATCH (P9 3.23% to res, P10 red vol 1.09x) |

### EXTREMELY BULLISH MOMENTUM
| Ticker | M/W/D RSI | Price | Score | Decision |
|---|---|---|---|---|
| MRVL | 67.6 / 67.2 / 61.5 | 275.31 | 8/8 | **ENTER** |
| ANET | 76.8 / 69.1 / 64.8 | 216.73 | 4/8 | WATCH (P9) |
| PANW | 74.7 / 70.3 / 63.0 | 418.92 | 3/8 | WATCH |
| CVX | 64.6 / 62.0 / 59.7 | 211.99 | 3/8 | WATCH |
| CRWD | 84.5 / 74.2 / 64.8 (BRS) | 275.06 | 2/8 | WATCH (P8, P9 4.3%, P10) |
| XOM | 67.5 / 62.2 / 64.4 | 169.01 | 2/8 | WATCH (0.36% to resistance) |
| SPY, QQQ | — | — | n/a | index ETFs, not traded |

### BULLISH
| Ticker | M/W/D RSI | Price | Score | Decision |
|---|---|---|---|---|
| AMAT | 63.3 / 55.3 / 54.5 | 506.95 | 6/10 | **ENTER** |
| AVGO | 60.1 / 47.7 / 50.1 | 361.54 | 6/10 | **ENTER** |
| LRCX | 65.0 / 54.2 / 51.2 | 318.81 | 6/10 | ENTER (backup; earnings Oct 21) |
| META | 65.2 / 59.7 / 56.7 | 718.38 | 4/10 | WATCH (P2 fail) |
| MPWR | 61.5 / 54.0 / 55.2 | 1386.17 | 4/10 | WATCH |
| C | 71.8 / 49.7 / 44.6 | 129.63 | 3/10 | WATCH |
| CAT | 65.3 / 46.9 / 44.7 | 800.63 | 3/10 | WATCH |
| ASML | 62.2 / 57.0 / 52.5 | 1780.30 | 2/10 | WATCH (earnings Oct 14 — avoid) |
| JNJ, ETN, NEM, EQIX, WMT | — | — | 2/10 | WATCH |
| ABNB | 66.9 / 56.6 / 51.8 | 165.85 | 0/10 | WATCH |

## Today's Entry Plan
**Trade/hold decision: ENTER up to 3 trades (ranked), semis-concentrated — apply live chase (≤3%) and P8/P9 re-check at market-open.**

1. **MRVL** (EB Momentum, 8/8) — entry ~$275.31, stop $267.05 (-3.0%), no fixed target (trail 3-bar daily low; exit on stop/BRS), shares 18 (~$4,956, 4.96%), risk ~$149. Order: limit at/just above open price, day. Thesis: M/W/D RSI 67.6/67.2/61.5, 8.9% to resistance, green vol 1.22x, sector pass.
2. **AMAT** (Bullish, 6/10) — entry ~$506.95, stop $491.74 (-3.0%), T1 $537.37, T2 $552.58, R/R 2.0, shares 9 (~$4,563), risk ~$137. Order: limit. Caveat: P9 fail (resistance near), P7 via gap only.
3. **AVGO** (Bullish, 6/10) — entry ~$361.54, stop $356.18 (-1.5%), T1 $372.26, T2 $377.62, R/R 2.0, shares 13 (~$4,700), risk ~$70. Order: limit. Tight stop vs. ASML-event gap risk.
- Backup: **LRCX** — entry ~$318.81, stop $311.54, T1 $333.35, T2 $340.62, 15 shares; only if one above is blocked.
- Weekly budget: 0/3 used; at most 3 new entries this week.
