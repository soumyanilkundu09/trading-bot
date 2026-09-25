# Research Log — Last Run: 2026-09-25 05:48 ET (pre-market)

## Account Snapshot
- Equity: $100,000.00
- Cash: $100,000.00
- Buying power: $400,000.00
- Open P&L: $0.00 (no open positions)
- Weekly budget: 0/3 entries used (week of 2026-09-21)
- Open positions: 0/5

## Global Gate

| Indicator | Value | Threshold | Status |
|---|---|---|---|
| SPX Monthly RSI | 73.78 | > 60 | ✅ PASS |
| SPX Weekly RSI | 62.64 | > 60 (healthy) | ✅ PASS |
| CBOE VIX | 15.38 | < 25 danger / < 18 normal | ✅ PASS (normal band) |
| DXY 20d change | +1.96% | not spiking > 3%/20d | ✅ PASS |
| US 10Y yield | 5.162% (+0.498 abs / 20d) | not surging | ⚠️ CAUTION (meaningful rise, no hard threshold breached) |

**Verdict: POSITIVE** — scanning proceeds.

## Event Risk
- Next FOMC meeting: **October 27–28, 2026** — not within 3 trading days. No macro-event caution flag needed today.
- 10Y yield has risen ~0.5pp over the last 20 trading days to 5.16% — a mild headwind worth watching but not a gate failure.

## Risk Factors
- **Scanner coverage was reduced today.** The Wikipedia S&P 500 constituent fetch returned `403 Forbidden`, so `rsi_scan.py` fell back to `config/universe.json` only (137 tickers) instead of the full S&P 500 (~503) + universe. Today's scan is **not** a full-market scan — some qualifying names outside `universe.json` may have been missed. Worth a look if this keeps failing on future runs (may need a User-Agent header or an alternate S&P 500 source).
- No open positions, so no -7% drawdown checks apply.
- **P8 (green-volume) hard gate** blocked 5 otherwise-qualifying ENTER signals (COP, GE, TSM, MRVL, VEEV) — see Today's Entry Plan. Per `TRADING-STRATEGY.md` Part 4/P8: even when total score clears the entry threshold, an order is not placed unless P8 (sustained above-average green-day volume) independently passes. These are watchlisted instead.
- TEM (EB_PULLBACK tier via BRS override) was excluded from consideration: daily RSI is 70.5 (deeply extended, not a genuine pullback), it is 26.98% from the nearest support (P7 fails hard), and its universe.json sector tag ("Microcap") has no sector-ETF mapping for P2. Adding it would be forcing a thesis the tier label doesn't actually support.

## Scanner Output

**Universe scanned:** 137 tickers (universe.json only — see Risk Factors). Gate: PASSED. Errors: 0.

**Sector ETF weekly RSI snapshot (from today's P2 checks):**

| Sector | Weekly RSI | Status |
|---|---|---|
| Technology (XLK) | 66.44 | Strong |
| Healthcare (XLV) | 62.22 | Strong |
| Energy (XLE) | 59.16 | Below 60 threshold |
| Communication_Services (XLC) | 53.33 | Neutral |
| Financials (XLF) | 47.73 | Weak |
| Industrials (XLI) | 41.98 | Weak |
| Consumer_Staples (XLP) | 41.02 | Weak |
| Real_Estate (XLRE) | 38.11 | Weak |

### Tier 1 — EXTREMELY BULLISH PULLBACK (2 hits)
| Ticker | M-RSI | W-RSI | D-RSI | BRS | Score | Decision |
|---|---|---|---|---|---|---|
| TEM | 67.65 | 64.12 | 70.54 | Yes | 1/10 | SKIP — extended, no real support nearby (see Risk Factors) |
| ETN | 62.50 | 60.19 | 59.06 | Yes | 5/10 | SKIP (Industrials W-RSI 41.98 fails P2; 7.38% from support) |

### Tier 2 — EXTREMELY BULLISH MOMENTUM (10 hits)
| Ticker | M-RSI | W-RSI | D-RSI | Score | Decision |
|---|---|---|---|---|---|
| TSM | 71.86 | 66.85 | 62.61 | 7/8 | ENTER (score) → **BLOCKED by P8 gate**, watchlisted |
| VEEV | 67.16 | 68.79 | 63.79 | 7/8 | ENTER (score) → **BLOCKED by P8 gate**, watchlisted |
| MRVL | 69.36 | 64.40 | 62.02 | 7/8 | ENTER (score) → **BLOCKED by P8 gate**, watchlisted |
| PANW | 80.63 | 66.73 | 61.23 | 4/8 | WATCH |
| MU | 73.10 | 65.30 | 63.10 | 4/8 | WATCH |
| FTNT | 87.82 | 73.17 | 64.55 | 3/8 | WATCH |
| AAPL | 73.44 | 64.97 | 61.14 | 3/8 | WATCH |
| ANET | 73.26 | 65.49 | 59.41 | 2/8 | BELOW THRESHOLD |
| ABBV | 75.27 | 63.10 | 60.20 | 2/8 | BELOW THRESHOLD |
| QQQ | 72.86 | 62.94 | 63.15 | 2/8 | BELOW THRESHOLD (index ETF, no sector data) |

### Tier 3 — BULLISH (15 hits)
| Ticker | M-RSI | W-RSI | D-RSI | Score | Decision |
|---|---|---|---|---|---|
| AMGN | 63.58 | 57.47 | 51.94 | 10/10 | **ENTER ✅** |
| COP | 62.76 | 57.42 | 47.50 | 6/10 | ENTER (score) → **BLOCKED by P8 gate**, watchlisted |
| TXN | 63.49 | 52.39 | 53.87 | 6/10 | **ENTER ✅** |
| GE | 60.73 | 45.75 | 39.73 | 6/10 | ENTER (score) → **BLOCKED by P8 gate**, watchlisted |
| LLY | 75.05 | 57.12 | 55.70 | 5/10 | WATCH |
| LRCX | 61.55 | 53.38 | 52.83 | 5/10 | WATCH |
| ASML | 64.58 | 55.97 | 52.43 | 4/10 | WATCH |
| CAT | 63.61 | 47.53 | 46.79 | 4/10 | WATCH |
| MA | 62.80 | 57.44 | 47.20 | 3/10 | WATCH |
| MPWR | 65.17 | 51.85 | 57.67 | 3/10 | WATCH |
| CSCO | 74.93 | 51.15 | 42.16 | 3/10 | WATCH |
| EQIX | 68.61 | 51.48 | 48.36 | 3/10 | WATCH |
| C | 69.08 | 52.39 | 43.71 | 2/10 | BELOW THRESHOLD |
| GOOGL | 60.76 | 50.40 | 48.53 | 2/10 | BELOW THRESHOLD |
| WMT | 64.22 | 42.45 | 48.06 | 2/10 | BELOW THRESHOLD |

**Filtered (tier decayed to NONE — near resistance):** DE (3.8% to resistance), DDOG (0.33% to resistance).
**Dropped from prior watchlist (tier now NONE):** CRWD, SCHW, NVDA.

## Today's Entry Plan

**Trade/hold decision: ENTER 2 trades** (AMGN, TXN). 5 additional score-qualified signals (COP, GE, TSM, MRVL, VEEV) are blocked by the P8 green-volume hard gate and moved to watchlist instead of entered.

### 1. AMGN — Healthcare — BULLISH tier — Score 10/10 (all 5 params passed)
- **Thesis:** Monthly RSI 63.6 confirms macro uptrend; Healthcare sector weekly RSI 62.2 is strong (P2 pass). Price is at a gap-support zone (P7 pass, 7.44% away — gap-type support has a wider tolerance than plain support). Sustained above-average green-day volume confirms accumulation (P8 pass — clears the hard gate). 9.68% of room to the nearest resistance (P9 pass) and the recent pullback came on below-average red-day volume (P10 pass, "Adverse Low Move" — weak sellers). Full 5/5 params clean.
- **Entry:** ~$406.16 (market/bracket at next session open)
- **Stop:** $393.98 (-3.00%)
- **Target 1 (50%):** $445.49 (daily RSI-60 equivalent)
- **Target 2 (trail 50%):** $442.70 (prior swing high)
- **R/R to T1:** 3.23
- **Shares:** 12 (capped by 5% position limit, not 2% risk — high share price)
- **Position value:** $4,873.92 (4.87% of equity)
- **Risk $:** $146.16
- **Order type:** Market, bracket (per `trading_config.json`), day TIF

### 2. TXN — Technology — BULLISH tier — Score 6/10 (4 of 5 params passed)
- **Thesis:** Monthly RSI 63.5, Technology sector weekly RSI 66.4 strong (P2 pass). Price 2.09% from support (P7 pass). Green-day volume 1.16x the 20-day average (P8 pass — clears the hard gate). Red-day volume 0.98x average, i.e. weak selling on the pullback (P10 pass). Only P9 fails — price is 1.0% from resistance, tighter than ideal, so T1 is modest (R/R 2.0). Acceptable given the other 4 params are clean and this stock has been on the watchlist since 09/21 building toward this score.
- **Entry:** ~$270.61 (market/bracket at next session open)
- **Stop:** $263.63 (-2.58%)
- **Target 1 (50%):** $284.57
- **Target 2 (trail 50%):** $291.55
- **R/R to T1:** 2.0
- **Shares:** 18
- **Position value:** $4,870.98 (4.87% of equity)
- **Risk $:** $125.64
- **Order type:** Market, bracket, day TIF

**Guardrail check (both trades):** open_positions_count 0→2 (< 5 ✅) | weekly_trade_count 0→2 (< 3 ✅) | each position ≤ 5% of capital ✅ | equity delivery only ✅.

### Blocked (score qualified, P8 hard gate failed) — moved to watchlist
| Ticker | Tier | Score | P8 green-vol ratio | Next action |
|---|---|---|---|---|
| TSM | EB_MOMENTUM | 7/8 | 0.91x (< 1.0) | Re-check next session |
| MRVL | EB_MOMENTUM | 7/8 | 0.85x | Re-check next session |
| VEEV | EB_MOMENTUM | 7/8 | 0.85x | Re-check next session |
| COP | BULLISH | 6/10 | 0.98x | Re-check next session |
| GE | BULLISH | 6/10 | 0.95x | Re-check next session |
