# Research Log — Last Run: 2026-10-15 08:30 ET (pre-market)

## Account Snapshot
Paper account PA3FLRNK3PUG — Equity $100,000.00 | Cash $100,000.00 | Buying power $400,000 | Open P&L $0 | Open positions 0/5 | Weekly entries 0/3

## Global Gate — ✅ POSITIVE
| Indicator | Value | Verdict |
|-----------|-------|---------|
| S&P 500 Monthly RSI | 79.71 | ✅ > 60 (extended, but trend intact) |
| S&P 500 Weekly RSI | 60.37 | ✅ > 60 (marginal) |
| VIX | 17.46 | ✅ < 18 normal |
| DXY | 101.96 (+1.74% 20d) | ✅ < 3% |
| US 10Y yield | 5.19% (+0.24 pts 20d) | ⚠️ elevated and rising, not yet "surging" |
Outlook: POSITIVE. Scanner `gate_passed: true`. Caveat: weekly RSI barely above 60 and 10Y at 5.19% — size conservatively.

## Event Risk
- Next FOMC: Oct 27–28 (outside 3-day window). No Fed decision imminent.
- Earnings: JNJ reported Oct 13 (done, beat +2.7%). EQIX reports Oct 28 after close (9 trading days out — outside 5-day block, but inside any multi-week hold).
- Day-of macro data calendar not verified (no calendar feed); check CPI/PPI/retail-sales risk manually.

## Risk Factors
- No held positions → no -7% alerts.
- Sector P2 blocks (sector weekly RSI < 60): Technology 58.83, Communication_Services 47.85, Consumer_Discretionary 44.47, Industrials 39.69, Materials 45.33, Utilities 43.06, Real_Estate 39.67, Consumer_Staples 56.96. Only Healthcare (63.63) passes P2.
- Rising 10Y yield (5.19%) is a headwind for Real Estate (EQIX) and long-duration tech.
- Prior watchlist names ASML, LLY, TXN, SCHW, CSCO, MA, CAT no longer qualify for any scanner tier today → dropped.

## Scanner Output
Scanned 137 | Errors 0 | Filtered (near resistance) 8 (MA, MRK, AMGN, QQQ, DIS, CSCO, GOOGL, AMZN)

### Extremely Bullish Pullback
| Ticker | Sector | M-RSI | W-RSI | D-RSI | BRS | Price | Score | Decision |
|--------|--------|-------|-------|-------|-----|-------|-------|----------|
| CRWD | Technology | 77.5 | 64.2 | 49.0 | Y | 249.35 | 4/10 | WATCH |
| META | Comm Svcs | 66.6 | 61.6 | 58.3 | Y | 738.24 | 2/10 | WATCH |

### Extremely Bullish Momentum (max 8)
| Ticker | Sector | M-RSI | W-RSI | D-RSI | Price | Score | Decision |
|--------|--------|-------|-------|-------|-------|-------|----------|
| XLV (ETF) | Healthcare | 60.2 | 63.6 | 62.1 | 173.95 | 4/8 | SKIP (0.1% to resistance) |
| TMO | Healthcare | 66.2 | 70.3 | 60.2 | 673.27 | 2/8 | SKIP (0.45% to res) |
| MSFT | Technology | 63.2 | 67.0 | 62.6 | 534.04 | 1/8 | SKIP |
| AAPL | Technology | 73.7 | 65.5 | 62.0 | 343.01 | 1/8 | SKIP |
| PLTR | Technology | 69.0 | 63.9 | 63.3 | 200.97 | 1/8 | SKIP |

### Bullish
| Ticker | Sector | M-RSI | W-RSI | D-RSI | BRS | Price | Score | Decision |
|--------|--------|-------|-------|-------|-----|-------|-------|----------|
| JNJ | Healthcare | 65.4 | 51.0 | 41.5 | Y | 253.91 | 9/10 | ENTER ✅ |
| EQIX | Real Estate | 65.3 | 46.3 | 40.9 | Y | 995.82 | 6/10 | ENTER (marginal) |
| DE | Industrials | 68.4 | 54.9 | 45.6 | Y | 651.12 | 3/10 | WATCH |
| NVDA | Technology | 68.3 | 54.6 | 44.0 | N | 221.49 | 3/10 | WATCH |
| FCX | Materials | 70.2 | 53.8 | 43.5 | N | 69.61 | 3/10 | WATCH |
| CEG | Utilities | 63.0 | 50.2 | 51.2 | Y | 279.66 | 3/10 | WATCH |
| DDOG | Technology | 70.2 | 59.9 | 54.0 | Y | 269.29 | 2/10 | WATCH |
| ABNB | Cons Disc | 67.2 | 57.4 | 53.6 | Y | 167.15 | 2/10 | WATCH |
| ANET | Technology | 71.4 | 56.7 | 42.7 | N | 195.44 | 2/10 | WATCH |
| TSM | Technology | 66.6 | 54.7 | 40.8 | N | 430.12 | 2/10 | WATCH |
| ETN | Industrials | 62.6 | 49.5 | 41.4 | Y | 408.71 | 2/10 | WATCH |
| MRVL | Technology | 63.4 | 57.7 | 44.5 | N | 245.47 | 1/10 | WATCH |
| WMT | Cons Staples | 63.2 | 54.0 | 69.0 | Y | 116.20 | 1/10 | WATCH |

## Today's Entry Plan
Trade/hold decision: ENTER 2 trade(s) — JNJ (primary), EQIX (marginal, lower conviction). Weekly budget 0/3 used. Both subject to market-open live-price/chase/guardrail re-check (re-score with `--live`).

### 1. JNJ — Healthcare — BULLISH tier — Score 9/10 (only P10 fails: red-candle volume 1.46x)
- Thesis: M-RSI 65.4 / W-RSI 51.0 / D-RSI 41.5 with BRS; sits 0.55% above support; 6.1% room to resistance; Healthcare is the only sector passing P2 (W-RSI 63.6). Earnings already out (Oct 13) → no event risk.
- Entry ~$253.91 | Stop $251.25 (1.05%) | T1 $269.39 | R/R (T1) 5.8 | Shares 19 (~$4,824, 4.8% of equity) | Risk ≈ $50.5 | Order: market (day) with bracket
- Caveat: 1.46x red-volume (distribution) warrants watching the open; very tight stop (1%) — skip if gaps down through support.

### 2. EQIX — Real Estate — BULLISH tier — Score 6/10 (marginal: P2, P8, P10 fail)
- Thesis: D-RSI 40.9 at support (0.06%, congestion-in-price), 5.2% to resistance. But Real Estate W-RSI 39.7 (sector weak), 10Y yield rising, earnings Oct 28.
- Entry ~$995.82 | Stop $990.21 (0.56%) | T1 $1,047.28 | R/R 9.2 | Shares 5 (~$4,979, 4.98%) | Risk ≈ $28 | Order: market (day) with bracket
- Caveat: 0.56% stop is inside normal noise for a ~$1000 stock; market-open should drop it if open > 1% above $995.82 or sector weakens. Optional skip at executor discretion — JNJ is the clear A-setup.
