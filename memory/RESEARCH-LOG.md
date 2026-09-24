# Research Log — Last Run: 2026-09-24 08:30 ET (pre-market)

## Account Snapshot
- Equity: $100,000.00
- Buying Power: $400,000.00
- Cash: $100,000.00
- Open P&L: $0.00 (no open positions)
- Mode: PAPER

## Global Gate
| Indicator | Value | Threshold | Status |
|---|---|---|---|
| S&P 500 Monthly RSI | 73.8 | > 60 | ✅ |
| S&P 500 Weekly RSI | 62.7 | > 60 (healthy) | ✅ |
| CBOE VIX | 16.3 | < 25 (danger) / < 18 (normal) | ✅ |
| DXY 20d change | +2.07% | not > 3% spike | ✅ |
| US 10Y yield | 5.114% (20d chg +0.475) | not surging | ⚠️ caution (see Risk Factors) |

**Verdict: POSITIVE** — scanning proceeded.

## Event Risk
- Next FOMC meeting: **Oct 27–28, 2026** — outside the 3-day window, no imminent Fed risk.
- No other major macro events flagged.

## Risk Factors
- US 10Y yield has climbed from ~4.64% to 5.11% over the last 20 sessions (+0.475pt) — a meaningful rise, though not an explicit gate-breaker. Watch for equity headwind if this continues; a factor against chasing extended names.
- Scanner universe this run was `config/universe.json` (137 tickers) only — the Wikipedia S&P 500 constituent fetch returned `403 Forbidden`, so the full ~503-ticker S&P sweep did not run. Coverage is reduced to the curated watchlist universe; full-index coverage should be verified next run.
- No held positions (0 open) — no below-threshold P&L exposure.

## Scanner Output

### Sector ETF Snapshot (Weekly RSI / Monthly RSI)
| Sector | ETF | Weekly RSI | Monthly RSI |
|---|---|---|---|
| Technology | XLK | 66.77 | 74.78 |
| Healthcare | XLV | 61.18 | 71.29 |
| Energy | XLE | 58.57 | 62.92 |
| Communication Services | XLC | 50.89 | 60.71 |
| Financials | XLF | 47.77 | 64.16 |
| Materials | XLB | 46.85 | 60.38 |
| Consumer Staples | XLP | 43.43 | 63.15 |
| Industrials | XLI | 43.57 | 63.12 |
| Consumer Discretionary | XLY | 41.99 | 49.04 |
| Real Estate | XLRE | 38.92 | 59.84 |
| Utilities | XLU | 31.34 | 52.31 |

Scanned: 137 (universe.json fallback) | Errors: 0 | Gate: PASSED

### EXTREMELY BULLISH PULLBACK (1)
| Ticker | Monthly | Weekly | Daily | BRS | Score |
|---|---|---|---|---|---|
| TEM | 66.5 | 61.3 | 65.4 | Yes | 5/10 SKIP (sector data unavailable — Microcap) |

### EXTREMELY BULLISH MOMENTUM (6)
| Ticker | Monthly | Weekly | Daily | Score |
|---|---|---|---|---|
| FTNT | 87.8 | 73.2 | 64.5 | 3/8 SKIP (P8, P9) |
| VEEV | 66.3 | 68.0 | 61.3 | 3/8 SKIP (P8, P9) |
| PANW | 80.8 | 67.1 | 62.7 | 4/8 SKIP (P9) |
| TSM | 71.5 | 65.9 | 60.9 | 3/8 SKIP (P8, P9) |
| AAPL | 73.6 | 65.3 | 62.5 | 3/8 SKIP (P8, P9) |
| ABBV | 75.3 | 63.1 | 60.4 | 2/8 SKIP (P8, P9, P10) |

### BULLISH (18)
| Ticker | Sector | Monthly | Weekly | Daily | Score | Decision |
|---|---|---|---|---|---|---|
| AMGN | Healthcare | 63.5 | 57.4 | 51.8 | 10/10 | **ENTER ✅** |
| CSCO | Technology | 74.3 | 50.6 | 40.8 | 7/10 | **ENTER ✅** |
| GE | Industrials | 60.6 | 45.6 | 39.3 | 6/10 | **ENTER ✅** |
| LRCX | Technology | 61.6 | 53.5 | 53.0 | 5/10 | WATCH (P9, P10) |
| ETN | Industrials | 62.4 | 59.9 | 58.6 | 5/10 | WATCH (P2, P7, P10) |
| LLY | Healthcare | 74.0 | 54.3 | 46.8 | 5/10 | WATCH (P8, P9) |
| ASML | Technology | 65.1 | 57.1 | 55.1 | 4/10 | WATCH (P8, P9, P10) |
| CAT | Industrials | 63.9 | 48.6 | 48.9 | 4/10 | WATCH (P2, P9) |
| MA | Financials | 61.5 | 55.3 | 42.1 | 3/10 | WATCH (P2, P9, P10) |
| MPWR | Technology | 65.7 | 53.1 | 60.3 | 3/10 | WATCH (P7, P9, P10) |
| V | Financials | 64.5 | 56.2 | 40.4 | 3/10 | WATCH (P2, P9, P10) |
| WMT | Consumer_Staples | 65.5 | 46.5 | 57.5 | 3/10 | WATCH (P2, P8, P9) |
| TXN | Technology | 63.8 | 53.0 | 56.0 | 3/10 | WATCH (P7, P9, P10) |
| EQIX | Real_Estate | 68.9 | 51.8 | 49.0 | 3/10 | WATCH (P2, P8, P9) |
| COP | Energy | 62.0 | 56.3 | 45.2 | 2/10 | BELOW THRESHOLD |
| C | Financials | 69.0 | 52.2 | 43.3 | 2/10 | BELOW THRESHOLD |
| EOG | Energy | 60.5 | 53.0 | 44.7 | 2/10 | BELOW THRESHOLD |
| NBIS | Microcap | 69.0 | 56.2 | 52.3 | 1/10 | BELOW THRESHOLD |

Filtered pre-tier (near-resistance): MU, MRVL, META, INTC, QQQ, SPY, DDOG, NVDA — all had qualifying RSI but < 5% (or worse) upside to resistance, excluded before tier classification.

## Today's Entry Plan

**Trade/hold decision: ENTER 3 trades** (AMGN, CSCO, GE) — fills the full weekly budget (0/3 used this week before these).

### AMGN — Healthcare — BULLISH tier — Score 10/10 (all 5 params pass)
- Thesis: Monthly RSI 63.5, Weekly RSI 57.4 holding above 40 (no BeRS), sector (XLV) Weekly RSI 61.18 strong. Daily at support/gap zone (dist_support 7.38%, gap support confirmed), sustained green volume (1.07x 20d avg), red-candle pullback on low volume (0.82x) = healthy correction, 9.75% room to resistance.
- Entry: $405.91 | Stop: $393.73 (-3.0%) | Target 1: $445.49 | R/R: 3.25
- Shares: 12 | Position value: $4,870.92 (4.87% of capital) | Risk: $146.16 (0.15% of capital)
- Order type: Market, bracket order, day TIF (per trading_config.json)

### CSCO — Technology — BULLISH tier — Score 7/10
- Thesis: Monthly RSI 74.3 strong, sector (XLK) Weekly RSI 66.77 very strong, daily RSI 40.8 right at the classic GFS inflection point, 5.42% room to resistance. Fails P7 (14.51% from nearest support — not at a tight support/CIP/gap zone) and P10 (recent red-candle volume 1.62x avg — some selling conviction on the pullback); still clears the 6-point ENTER bar on strength of P2/P9.
- Entry: $106.44 | Stop: $103.25 (-3.0%) | Target 1: $112.82 | R/R: 2.0
- Shares: 46 | Position value: $4,896.24 (4.90% of capital) | Risk: $146.74 (0.15% of capital)
- Order type: Market, bracket order, day TIF

### GE — Industrials — BULLISH tier — Score 6/10 (marginal — right at ENTER threshold)
- Thesis: Price sitting right at support (0.37% away), 5.5% room to resistance. Fails P2 (Industrials/XLI Weekly RSI only 43.57 — sector not confirmed strong), P8 (green-day volume 0.96x, below average — soft conviction), P10 (recent red volume 1.16x — some selling pressure). Only clears threshold via P7+P9 (6 pts). Tight technical stop (0.86%) gives an attractive R/R (6.37) but the setup is the weakest of the three — flag for extra scrutiny at market-open before firing.
- Entry: $319.52 | Stop: $316.76 (-0.86%) | Target 1: $337.09 | R/R: 6.37
- Shares: 15 | Position value: $4,792.80 (4.79% of capital) | Risk: $41.40 (0.04% of capital)
- Order type: Market, bracket order, day TIF

**Weekly budget note:** these 3 entries, if all executed, use the full 3/3 weekly allowance. No further new entries should be taken this week (resets Monday 2026-09-28).
**Guardrail check:** 0/5 open positions before entry (room for all 3); each position ≤ 5% of capital; combined risk ≤ 0.34% of capital — well inside 2% per-trade cap.
