# Research Log — Last Run: 2026-10-16 05:50 ET (pre-market)

> Overwritten on every pre-market run. Git history is the archive. Scanner data = 2026-10-15 close. Market opens 09:30 ET today (Friday).
> Note: TRADE-LOG.md was last updated 2026-09-21 — no committed runs between then and now; weekly tracker re-based to week of 2026-10-12.

## Account Snapshot
- Equity $100,000.00 (paper PA3FLRNK3PUG, ACTIVE) | Cash $100,000.00 | Buying power $400,000.00
- Open P&L: $0.00 (no open positions) | Weekly entries: 0 / 3 | Open positions: 0 / 5

## Global Gate — POSITIVE ✓
| Indicator | Value | Status |
|-----------|-------|--------|
| S&P 500 Monthly RSI | 79.91 | ✓ > 60 (extended, but not a gate fail) |
| S&P 500 Weekly RSI | 61.69 | ✓ > 60 (thin margin) |
| VIX | 16.01 | ✓ < 25 |
| DXY | 101.71 (+1.28% / 20d) | ✓ < 3% |
| US 10Y | 5.089% (+9 bp / 20d) | ⚠ high level, not surging |

## Event Risk
- No FOMC decision within 3 days (next meeting expected late Oct — verify). Not machine-verified; no calendar tool available.
- Q3 earnings season underway: earnings dates were not checked by tools. GE Aerospace and MRK typically report ~Oct 21–29; verify before entry (Part 7: earnings within 5 trading days = reject).
- Weekly S&P RSI barely above 60 and 10Y > 5%: caution.

## Risk Factors
- Sector weekly RSI (P2 fails < 60): Tech 57.63, Comm Svcs 51.02, Cons Disc 47.52, Staples 58.40, Materials 49.57, Industrials 40.62, Utilities/RE 42.51. Only Healthcare (66.08) passes.
- No held positions.

## Scanner Output (137 scanned, 0 errors, 6 filtered, gate passed)
### EXTREMELY BULLISH PULLBACK
| Ticker | M/W/D RSI | Price | Score | Decision |
|---|---|---|---|---|
| MRK | 63.2 / 62.0 / 50.7 | 145.29 | 6/10 | ENTER (marginal; P9 fail, 3.43% to res) |
| CRWD | 75.8 / 62.6 / 46.5 | 244.59 | 4/10 | SKIP |
| ABNB | 68.7 / 61.0 / 61.9 | 174.27 | 4/10 | SKIP |
| META | 66.5 / 61.4 / 57.8 | 736.58 | 2/10 | SKIP |
### EXTREMELY BULLISH MOMENTUM (max 8)
| AAPL | 73.5 / 65.1 / 60.4 | 341.91 | 0/8 | SKIP (0.28% to res) |
| PLTR | 68.9 / 63.7 / 62.6 | 200.49 | 1/8 | SKIP |
### BULLISH
| Ticker | M/W/D RSI | Score | Decision |
|---|---|---|---|
| GE | 61.9 / 44.1 / 44.5 | 6/10 | BLOCKED — P8 hard gate failed (green vol 0.88x), P2 fail, P10 1.48x; likely earnings inside 5 days |
| NVDA | 66.3 / 52.5 / 40.1 | 4/10 | WATCH |
| JNJ | 65.1 / 50.7 / 41.0 | 4/10 | WATCH |
| DIS | 61.3 / 58.2 / 65.7 | 4/10 | WATCH |
| WMT, DE, APD, CSCO, CEG | | 3/10 | WATCH |
| DDOG, FCX, NEM, EQIX, MRVL | | 1–2/10 | WATCH/drop |
| AMD, PANW | | 0–1/10 | drop |

## Today's Entry Plan
Trade/hold decision: **ENTER 1 trade (marginal) — MRK**, subject to market-open validation (live-price chase ≤3%, earnings date check, P8 gate).

**MRK — Healthcare — EB Pullback — 6/10** (only sector passing P2; P7 gap support pass, P8 pass 1.07x)
- Entry ~145.29 | Stop 141.62 (-2.53%) | T1 152.63 (R/R 2.0) | T2 156.30
- Shares 34 (~$4,940, 4.94% of equity) | Risk ~$125 | Order: bracket, per config
- Caveat: P9 fails (3.43% to nearest resistance vs ≥6% large-cap requirement) and Healthcare sector is the lone strength. Market-open should skip if earnings are ≤5 trading days away or price has run >3%.

GE: not eligible (P8 gate). Weekly budget 0/3 — no budget constraint.
