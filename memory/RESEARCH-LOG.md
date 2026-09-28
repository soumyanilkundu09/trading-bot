# Research Log — Last Run: 2026-09-28 05:48 ET (pre-market)

## Account Snapshot
| Metric | Value |
|---|---|
| Equity | $100,000.00 |
| Cash | $100,000.00 |
| Buying Power | $400,000.00 |
| Open P&L | $0.00 (no open positions) |
| Mode | PAPER |

## Global Gate
| Indicator | Value | Threshold | Status |
|---|---|---|---|
| S&P 500 Monthly RSI | 74.2 | > 60 | ✅ |
| S&P 500 Weekly RSI | 63.84 | > 60, healthy | ✅ |
| CBOE VIX | 16.3 | < 25 (danger), < 18 (normal) | ✅ |
| DXY 20d change | +1.67% | not > 3% spike | ✅ |
| US 10Y Yield | 5.184% (20d chg +0.464) | not surging sharply | ⚠️ watch (elevated but not a spike) |

**Verdict: POSITIVE** — All mandatory gate conditions clear. 10Y yield is elevated in absolute terms but the 20-day change is not a sharp surge; not treated as disqualifying.

## Event Risk
- Next FOMC meeting: **October 27–28, 2026** — well outside the 3-day window. No imminent Fed-decision risk.
- No other major macro events flagged.

## Risk Factors
- No open positions — no -7% drawdown risk to flag.
- Sector breadth is narrow: of 11 sectors, only **Technology (W-RSI 67.25)** and **Healthcare (W-RSI 62.97)** clear the P2 "sector strong" bar (>60). Financials, Energy, Communication Services, Industrials, Real Estate, and Consumer Staples are all sub-60 on weekly RSI — this is why most BULLISH-tier candidates outside Tech/Healthcare fail P2.
- Scanner ran in **degraded coverage mode**: Wikipedia S&P 500 constituent fetch returned HTTP 403 (blocked), so the scan fell back to `config/universe.json` only (137 tickers) instead of the full ~503-ticker S&P 500 + universe set. Today's picks are drawn from a smaller-than-usual universe — worth a look at fixing the Wikipedia fetch (e.g., alternate source or cached constituent list) in a future maintenance pass.

## Scanner Output

**Sector ETF / Index Snapshot (Weekly RSI):**
| Sector | Weekly RSI | Verdict |
|---|---|---|
| Technology | 67.25 | Strong ✅ |
| Healthcare | 62.97 | Strong ✅ |
| Energy | 57.71 | Weak |
| Communication Services | 51.58 | Weak |
| Financials | 49.07 | Weak |
| Industrials | 44.07 | Weak |
| Consumer Staples | 42.20 | Weak |
| Real Estate | 37.69 | Weak |

Universe scanned: 137 tickers (universe.json fallback) | Gate: PASSED | Errors: 0 | Filtered (near-resistance): 5

**EXTREMELY BULLISH PULLBACK (1):**
| Ticker | Monthly RSI | Weekly RSI | Daily RSI | Price | Score |
|---|---|---|---|---|---|
| DDOG | 71.53 | 62.92 | 66.89 [BRS] | $268.13 | 3/10 |

**EXTREMELY BULLISH MOMENTUM (7):**
| Ticker | Monthly RSI | Weekly RSI | Daily RSI | Price | Score |
|---|---|---|---|---|---|
| CRWD | 84.45 | 70.61 | 62.12 [BRS] | $252.10 | 4/8 |
| TSM | 71.83 | 66.73 | 62.26 | $450.56 | 3/8 |
| ANET | 73.38 | 65.74 | 59.99 | $206.49 | 3/8 |
| MU | 73.13 | 65.38 | 63.29 | $1082.01 | 4/8 |
| MRVL | 69.57 | 64.88 | 63.08 | $261.80 | 3/8 |
| QQQ | 73.12 | 63.57 | 64.68 | $744.44 | 2/8 |
| PLTR | 66.95 | 62.81 | 63.67 | $189.63 | 4/8 |

**BULLISH (16):**
| Ticker | Sector | Monthly RSI | Weekly RSI | Daily RSI | Price | Score |
|---|---|---|---|---|---|---|
| AMGN | Healthcare | 65.69 | 59.20 | 56.35 [BRS] | $414.67 | **8/10 ENTER** |
| LLY | Healthcare | 75.06 | 57.18 | 55.82 [BRS] | $1183.99 | 5/10 |
| CSCO | Technology | 74.62 | 50.85 | 41.63 [BRS] | $106.69 | 5/10 |
| CAT | Industrials | 64.29 | 49.93 | 52.09 [BRS] | $821.04 | 4/10 |
| ASML | Technology | 65.02 | 56.97 | 54.58 [BRS] | $1743.61 | 4/10 |
| MA | Financials | 63.14 | 57.89 | 48.45 [BRS] | $567.50 | 3/10 |
| COP | Energy | 61.52 | 55.53 | 44.25 [BRS] | $127.29 | 3/10 |
| JPM | Financials | 71.50 | 55.23 | 41.41 [BRS] | $342.88 | 3/10 |
| MPWR | Technology | 65.90 | 53.61 | 60.45 [BRS] | $1366.90 | 3/10 |
| COST | Consumer Staples | 61.80 | 44.34 | 52.31 [BRS] | $922.76 | 3/10 |
| GOOGL | Communication Services | 60.98 | 50.92 | 49.68 [BRS] | $343.85 | 2/10 |
| C | Financials | 70.03 | 54.30 | 49.74 [BRS] | $134.27 | 2/10 |
| EQIX | Real Estate | 65.70 | 48.18 | 42.11 | $1008.54 | 2/10 |
| WMT | Consumer Staples | 64.41 | 43.06 | 49.33 [BRS] | $107.97 | 2/10 |
| GE | Industrials | 62.46 | 48.27 | 47.26 [BRS] | $327.02 | 1/10 |

**Filtered out (RSI passed, blocked by near-resistance entry filter):**
| Ticker | Monthly RSI | Weekly RSI | Daily RSI | Reason |
|---|---|---|---|---|
| META | 66.7 | 64.2 | 71.1 | 3.80% to resistance ($779.80) |
| DE | 70.0 | 63.7 | 58.4 | 4.51% to resistance ($721.22) |
| INTC | 63.4 | 63.7 | 67.0 | 3.62% to resistance ($127.44) |
| ETN | 62.5 | 60.2 | 59.1 | 4.19% to resistance ($458.50) |
| TXN | 64.5 | 54.7 | 60.0 | 2.92% to resistance ($286.07) |

## Today's Entry Plan

**Trade/hold decision: ENTER 1 trade (AMGN)**

Weekly budget: new week (Mon 2026-09-28) — 0/3 entries used, full budget available.

### AMGN — Healthcare — BULLISH tier — Score 8/10 (ENTER)
- **Thesis:** Monthly RSI 65.69 (>60) and Weekly RSI 59.20 confirm the GFS macro trend; Healthcare is one of only two sectors clearing the P2 strength bar (sector W-RSI 62.97). Daily RSI 56.35 shows a completed Bullish Range Shift (BRS) — RSI has reclaimed and is holding above 40 with a higher structure. Passed P2 (sector strong), P8 (green-day volume ~1.0x avg), P9 (7.43% clearance to resistance — healthy R:R room), and P10 (recent red candles on below-average volume, 0.79x — weak/no-conviction selling). Only miss is P7 (9.33% from the nearest support/CIP/gap zone — not a precision entry-at-support setup, but the other 4 parameters clear comfortably for the 8/10 score).
- **Entry:** ~$414.67 (market open / bracket order)
- **Stop-loss:** $402.23 (3.0% below entry)
- **Target 1:** $445.49 (RSI-60 equivalent zone, 50% exit)
- **Target 2:** $451.99 (trail remaining 50%)
- **R/R (to T1):** 2.48
- **Shares:** 12 (position value $4,976.04 = 4.98% of capital — at the 5% position cap; risk $149.28 = 0.15% of capital, well inside the 2% risk ceiling since share count is capped by the position-size limit, not the risk limit)
- **Order type:** Market, bracket order (stop-loss + target attached), day TIF, no extended hours — per `config/trading_config.json`
- **Guardrail pre-check:** weekly_trade_count 0/3 ✓ | open_positions 0/5 ✓ | equity delivery ✓ | P8 entry gate (green-day volume ok) ✓ → clear to execute in market-open routine.

All other scanned tickers scored below the 6/10 promotion threshold and remain on the watchlist (see `memory/TRADE-LOG.md`).
