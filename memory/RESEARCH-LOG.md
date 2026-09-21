# Research Log — Last Run: 2026-09-21 05:41 ET (pre-market)

## Account Snapshot
- Equity: $100,000.00 | Cash: $100,000.00 | Buying power: $400,000.00
- Open positions: 0 | Open P&L: $0.00 (no positions held)

## Global Gate
| Indicator | Value | Threshold | Status |
|---|---|---|---|
| S&P 500 Monthly RSI | 72.48 | > 60 | ✅ |
| S&P 500 Weekly RSI | 60.87 | healthy (>60) | ✅ |
| CBOE VIX | 14.97 | < 25 (danger) / < 18 (normal) | ✅ |
| DXY 20d change | +1.33% | not >3% spike | ✅ |
| US 10Y yield | 4.998% (20d Δ +0.26) | not surging | ✅ |

**Verdict: POSITIVE** — full scan authorized.

## Event Risk
- No FOMC meeting within 3 trading days of 2026-09-21 (next scheduled meeting is Oct 27–28, 2026 per the Fed's published calendar — not live-verified this run, no FOMC-calendar data source is wired into the toolchain).
- No other major macro event flagged. Standard earnings-within-5-days check applied per ticker in Risk Factors below.

## Risk Factors
- **Tooling fix applied this run:** `tools/rsi_scan.py`'s S&P 500 constituent fetch (Wikipedia) was returning HTTP 403 (no User-Agent header on the request), silently degrading every prior scan to the 137-ticker `universe.json` fallback only. Fixed by adding a browser User-Agent; this run scanned the full 522-ticker universe (503 S&P 500 + universe.json, deduplicated). Fix committed alongside this log.
- **Sector concentration in today's picks:** 2 of the 3 ENTER candidates (FLEX, JBL) are Technology; the third (LH) is Healthcare. Tech sector ETF (XLK) is the single strongest sector this morning (Weekly RSI 63.37), which is why it dominates the top of the ranked list — not a guardrail violation, but a concentration worth watching if a Tech-wide reversal hits.
- No held positions to flag at -7% (portfolio is flat).
- Two candidates (LH, TRGP — both EB Pullback) and several BULLISH names fail P10 (recent red candles above 20d avg volume) — a mild, non-disqualifying pullback-conviction flag baked into their scores already.

## Scanner Output

### Sector ETF Snapshot (Weekly RSI / Monthly RSI)
| Sector | ETF | Weekly RSI | Monthly RSI |
|---|---|---|---|
| Technology | XLK | 63.37 | 73.41 |
| Energy | XLE | 63.91 | 66.01 |
| Healthcare | XLV | 60.77 | 70.92 |
| Financials | XLF | 54.54 | 67.66 |
| Materials | XLB | 45.57 | 59.64 |
| Communication Services | XLC | 47.53 | 58.87 |
| Consumer Staples | XLP | 44.75 | 63.76 |
| Real Estate | XLRE | 41.84 | 61.77 |
| Industrials | XLI | 43.00 | 62.85 |
| Consumer Discretionary | XLY | 42.48 | 49.44 |
| Utilities | XLU | 35.37 | 55.57 |

Universe: 522 scanned (503 S&P 500 + universe.json, deduped) | Errors: 0 | Filtered by entry rules (near-resistance / gap-down): 21

### EXTREMELY BULLISH PULLBACK (6)
| Ticker | Sector | M-RSI | W-RSI | D-RSI | BRS | Price | Score |
|---|---|---|---|---|---|---|---|
| LH | Healthcare | 65.12 | 62.64 | 49.82 | Y | 320.71 | 9/10 ✅ |
| TRGP | Energy | 79.67 | 62.15 | 56.00 | Y | 292.19 | 6/10 ✅ |
| CNC | Healthcare | 60.03 | 60.58 | 47.79 | Y | 65.11 | 5/10 |
| LITE | Technology | 79.75 | 60.42 | 54.02 | Y | 930.91 | 4/10 |
| AMP | Financials | 62.89 | 61.15 | 44.93 | N | 544.17 | 3/10 |
| STT | Financials | 81.17 | 64.62 | 39.90 | N | 182.87 | 2/10 |

### EXTREMELY BULLISH MOMENTUM (11)
| Ticker | Sector | M-RSI | W-RSI | D-RSI | Price | Score |
|---|---|---|---|---|---|---|
| CRWD | Technology | 83.36 | 68.04 | 60.38 | 237.61 | 8/8 ✅ |
| HPQ | Technology | 65.51 | 73.37 | 62.27 | 34.40 | 7/8 ✅ |
| DELL | Technology | 87.22 | 74.89 | 61.81 | 568.06 | 4/8 |
| DGX | Healthcare | 75.51 | 69.04 | 63.01 | 246.45 | 4/8 |
| HPE | Technology | 86.85 | 71.12 | 59.26 | 60.73 | 3/8 |
| FFIV | Technology | 75.92 | 67.57 | 61.84 | 432.11 | 3/8 |
| AAPL | Technology | 73.42 | 64.92 | 63.81 | 335.73 | 3/8 |
| GILD | Healthcare | 73.54 | 64.07 | 62.59 | 150.11 | 3/8 |
| VRSN | Technology | 63.01 | 63.23 | 63.89 | 303.12 | 3/8 |
| PFG | Financials | 73.78 | 68.31 | 59.13 | 117.64 | 1/8 |
| BBY | Consumer_Discretionary | 70.96 | 66.23 | 59.41 | 92.90 | 0/8 |

### BULLISH (58 total — top 20 by score shown; full watchlist below)
| Ticker | Sector | M-RSI | W-RSI | D-RSI | BRS | Price | Score |
|---|---|---|---|---|---|---|---|
| FLEX | Technology | (see scorer) | | | | 108.58 | 9/10 ✅ |
| JBL | Technology | | | | | 299.52 | 9/10 ✅ |
| ASML | Technology | 63.28 | 53.51 | 48.52 | Y | 1679.25 | 8/10 ✅ |
| WDC | Technology | 66.86 | 49.62 | 45.79 | Y | 441.36 | 8/10 ✅ |
| LLY | Healthcare | 74.05 | 54.40 | 47.04 | Y | 1152.46 | 6/10 ✅ |
| DDOG | Technology | 65.35 | 54.95 | 48.90 | Y | 229.89 | 5/10 |
| KEYS | Technology | 68.96 | 56.17 | 54.50 | Y | 335.00 | 5/10 |
| ADI | Technology | 62.78 | 52.74 | 55.11 | Y | 375.72 | 5/10 |
| APH | Technology | 66.42 | 51.64 | 44.11 | Y | 77.55 | 5/10 |
| TXN | Technology | 62.94 | 51.03 | 51.18 | Y | 266.71 | 5/10 |
| BE | Industrials | 67.92 | 57.14 | 57.53 | Y | 265.63 | 5/10 |
| SCHW | Financials | 63.95 | 57.56 | 42.34 | Y | 105.22 | 4/10 |
| GL | Financials | 71.90 | 57.43 | 48.35 | Y | 173.42 | 4/10 |
| NVDA | Technology | 70.62 | 56.92 | 54.01 | Y | 222.04 | 4/10 |
| STX | Technology | 80.46 | 56.82 | 52.83 | Y | 858.47 | 4/10 |
| FAST | Industrials | 68.82 | 56.17 | 46.44 | Y | 49.01 | 4/10 |
| WAB | Industrials | 71.46 | 56.12 | 43.88 | Y | 280.23 | 4/10 |
| CSCO | Technology | 78.06 | 54.12 | 46.10 | Y | 109.51 | 4/10 |
| MA | Financials | 62.61 | 57.19 | 44.09 | N | 565.08 | 3/10 |
| CAT | Industrials | 60.22 | 48.24 | 47.90 | Y | 808.99 | 3/10 |
| EQIX | Real_Estate | 67.14 | 49.82 | 45.07 | Y | 1021.59 | 3/10 |

*(remaining BULLISH-tier names scored < 3 or omitted for brevity — full data in this run's commit; ask for the complete table if needed)*

## Today's Entry Plan

**Trade/hold decision: ENTER 3 trades (weekly budget cap reached: 3/3)**

Weekly budget resets today (new Mon–Fri week). Nine tickers scored ≥6 (ENTER-qualified); only the top 3 by score fit this week's 3-trade budget. The other 6 are PROMOTE-blocked by guardrail 8E (see below).

---

### 1. LH (Labcorp) — Healthcare — EXTREMELY_BULLISH_PULLBACK — Score 9/10 ✅
**Thesis:** Monthly RSI 65.1 confirms macro uptrend; Weekly RSI 62.6 with confirmed BRS. Healthcare sector (XLV) Weekly RSI 60.77 — sector strong (P2 ✅). Daily RSI 49.8 with BRS at the pullback zone. Price 1.03% from support (P7 ✅), 6.0% from resistance (P9 ✅), green-day volume in line with average (P8 ✅). Only P10 fails (last 4 red candles slightly above avg volume — mild, non-disqualifying).
- Entry: $320.37 | Stop: $315.47 (-1.53%) | T1: $339.59 | T2: $335.07
- R/R (T1): 3.92 | Shares: 15 | Position value: $4,805.55 (4.81% of capital) | Risk: $73.50 (0.07% of capital)
- Order type: Market entry, bracket order (stop-loss + T1 target)

### 2. FLEX (Flex Ltd) — Technology — BULLISH — Score 9/10 ✅
**Thesis:** Monthly RSI strong, Weekly RSI in bullish-approaching zone with BRS confirmed. Tech sector (XLK) Weekly RSI 63.37 — sector strong (P2 ✅). Price 0.61% from support (P7 ✅), 6.87% from resistance (P9 ✅), green-day volume above average (P8 ✅). Only P10 fails (marginal, 1.18x avg on red candles).
- Entry: $108.58 | Stop: $107.38 (-1.11%) | T1: $116.05 | T2: $112.18
- R/R (T1): 6.22 | Shares: 46 | Position value: $4,994.68 (4.99% of capital) | Risk: $55.20 (0.06% of capital)
- Order type: Market entry, bracket order (stop-loss + T1 target)

### 3. JBL (Jabil) — Technology — BULLISH — Score 9/10 ✅
**Thesis:** Same Tech sector tailwind as FLEX (XLK Weekly RSI 63.37, P2 ✅). Price 1.59% from support (P7 ✅), 5.42% from resistance (P9 ✅), green-day volume above average (P8 ✅). Only P10 fails (1.42x avg on red candles, mild).
- Entry: $299.52 | Stop: $293.30 (-2.08%) | T1: $315.75 | T2: $318.18
- R/R (T1): 2.61 | Shares: 16 | Position value: $4,792.32 (4.79% of capital) | Risk: $99.52 (0.10% of capital)
- Order type: Market entry, bracket order (stop-loss + T1 target)

---

### Guardrail-Blocked (qualified ENTER, weekly budget exhausted — 8E)
```
╔═══════════════════════════════════════════════════════════╗
║  TRADE BLOCKED — GUARDRAIL VIOLATION                     ║
╠═══════════════════════════════════════════════════════════╣
║  Stocks      : CRWD(8/8), ASML(8/10), WDC(8/10),          ║
║                HPQ(7/8), TRGP(6/10), LLY(6/10)            ║
║  Blocked by  : 8E — Weekly Trade Budget (3/3 used by      ║
║                LH, FLEX, JBL above)                        ║
║  Reason      : All 6 scored ≥6 (ENTER-qualified) but no    ║
║                budget slots remain this week                ║
║  Next action : PROMOTE — watchlisted, re-evaluate at        ║
║                daily-summary / next Monday reset             ║
╚═══════════════════════════════════════════════════════════╝
```

**Portfolio guardrail check for the 3 entries above:** open_positions 0→3 (< 5 ✅) | weekly_trade_count 0→3 (= 3, at cap ✅) | each position ≤ 5% cap ✅ | all equity delivery, no restricted instruments ✅.
