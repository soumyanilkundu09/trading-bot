# Research Log — Last Run: 2026-10-02 08:30 ET (pre-market)

## Account Snapshot
Paper account PA3FLRNK3PUG | Equity $100,000 | Cash $100,000 | Buying power $400,000 | Open positions 0 | Open P&L $0

## Global Gate
| Indicator | Value | Read |
|-----------|-------|------|
| SPX Monthly RSI | 79.29 | ✅ > 60 |
| SPX Weekly RSI | 59.79 | ⚠️ marginally < 60 (scanner gate threshold is > 50 → pass) |
| VIX | 15.97 | ✅ < 18 |
| DXY 20d change | +2.79% | ⚠️ just under 3% spike line |
| US 10Y yield | 5.237% (+0.475 over 20d) | ⚠️ rising fast — equity headwind |

**Verdict: POSITIVE (cautious).** Scanner gate passed; but weekly RSI sits just under 60 and DXY/10Y are both leaning risk-off. Treat as a thin positive: no more than the best-scoring setups, half-attention to new entries if DXY crosses +3% or SPX weekly RSI rolls over.

## Event Risk
- Today is the first Friday of the month — US jobs report (NFP) is normally released 08:30 ET; verify the print before the 09:45 market-open run. Rate-sensitive reaction risk is elevated given the 10Y at 5.2%.
- No FOMC decision within 3 days (next meeting is later in October — confirm date). Earnings-within-5-days check NOT automated: market-open must verify for MU, META, MRK before ordering (MU reports late Sept/Oct cycle historically; META/MRK report late Oct).
- Friday entry = weekend gap risk.

## Risk Factors
- Macro: 10Y yield surge + DXY +2.79%; SPX weekly RSI 59.79.
- Sector P2 blocks: Healthcare W-RSI 56.32, Energy 58.93, Materials 40.18, Financials/Industrials/Real Estate weak (see TRADE-LOG watchlist).
- Scanner caveat: META and INTC are in the PULLBACK tier through the daily-BRS path with daily RSI ~61 (not near 40) — they are momentum-like, not true GFS pullbacks.
- No held positions → no -7% alerts.
- Weekly budget: week of 2026-09-28 has 0/3 entries used.

## Scanner Output
Scanned 137 | Errors 0 | Filtered 9 (near resistance) | Gate passed.

### EXTREMELY BULLISH PULLBACK
| Ticker | Sector | M-RSI | W-RSI | D-RSI | BRS | Price | Score | Decision |
|---|---|---|---|---|---|---|---|---|
| META | Communication | 65.48 | 60.74 | 61.02 | Y | 725.70 | 8/10 | ENTER (P2 data n/a; daily RSI 61 caveat) |
| MRK | Healthcare | 73.82 | 60.87 | 45.00 | N | 143.76 | 7/10 | ENTER (true pullback; P2, P10 fail) |
| INTC | Technology | 62.84 | 61.92 | 61.65 | Y | 120.01 | 4/10 | SKIP |

### EXTREMELY BULLISH MOMENTUM
| Ticker | M-RSI | W-RSI | D-RSI | Price | Score | Decision |
|---|---|---|---|---|---|---|
| MU | 73.48 | 66.05 | 63.71 | 1098.15 | 8/8 | ENTER |
| MRVL | 70.05 | 65.95 | 63.39 | 268.00 | 7/8 | BLOCKED — P8 hard gate failed (green vol 0.93x) |
| PANW | 80.68 | 67.60 | 60.30 | 396.09 | 3 | SKIP (0.61% to resistance) |
| PLTR | 67.05 | 62.94 | 63.11 | 190.07 | 3 | SKIP |
| FTNT | 87.77 | 73.31 | 62.14 | 178.72 | 2 | SKIP |
| VEEV | 68.64 | 70.13 | 64.46 | 281.85 | 2 | SKIP |
| NVDA | 72.43 | 60.43 | 60.28 | 231.04 | 2 | SKIP |
| PSX | 77.37 | 72.27 | 62.28 | 263.94 | 1 | SKIP |
| QQQ | 72.94 | 62.74 | 61.51 | 742.02 | n/a | ETF — not traded |

### BULLISH (re-scored where daily RSI in 39–46 zone)
| Ticker | M-RSI | W-RSI | D-RSI | Price | Score | Decision |
|---|---|---|---|---|---|---|
| NEM | 65.66 | 52.08 | 39.68 | 114.63 | 6/10 | Scorer ENTER but P8 fail (0.93x) → hard gate blocks; WATCH |
| COP | 61.05 | 55.31 | 45.23 | 127.06 | 4/10 | WATCH |
| V | 63.92 | 55.05 | 40.13 | 359.94 | 3/10 | WATCH |
| LLY | 73.84 | 53.48 | 45.05 | 1150.63 | 3/10 | WATCH |
| KO | 74.36 | 56.59 | 39.68 | 86.12 | 2/10 | BELOW THRESHOLD |
| EQIX | 66.10 | 48.75 | 43.56 | 1012.55 | 2/10 | BELOW THRESHOLD |
| XLV | 68.85 | 56.32 | 41.34 | 166.19 | n/a | ETF — not scored |
| LRCX, AMAT, DE, AMGN, KLAC, COST | — | — | daily RSI 48–67 | — | not scored | Daily RSI outside 39–45 zone; BRS-only hit |

## Today's Entry Plan
Trade/hold decision: **ENTER 3 trades (conditional)** — ranked MU, MRK, META. Weekly budget 0/3; open positions 0/5. All subject to market-open checks: NFP reaction, earnings-within-5-days, P8 gate, chase cap (≤3% above plan entry), and gate still POSITIVE.

| # | Ticker | Tier | Score | Order | Entry ~ | Stop | T1 | R/R (T1) | Shares | Value | Risk |
|---|--------|------|-------|-------|---------|------|----|----------|--------|-------|------|
| 1 | MU | EB Momentum | 8/8 | market | 1098.15 | 1065.21 | none — trail 3-bar daily low | n/a | 4 | ~$4,393 | ~$132 |
| 2 | MRK | EB Pullback | 7/10 | market | 143.76 | 141.62 | 152.53 (T2 150.18) | 4.1 | 34 | ~$4,888 | ~$73 |
| 3 | META | EB Pullback* | 8/10 | market | 725.70 | 709.76 | 779.80 (T2 773.52) | 3.4 | 6 | ~$4,354 | ~$96 |

- **MU** — Momentum continuation: M/W/D RSI 73.5/66.1/63.7, all 8 momentum points pass, no resistance blocker. Exit by trailing stop or BRS only; no fixed target. Stop ~3% below entry. (Share count from scorer; verify risk ≤ 2% = $2,000 — well within.)
- **MRK** — Only true GFS pullback today: daily RSI 45.0 at the top of the zone, support 1% below, 6.1% to resistance, 7-green-day volume 1.06x. Weaknesses: Healthcare sector W-RSI 56.3 (P2), pullback volume 1.2x (P10). Tight 1.5% stop.
- **META** — Highest scorer but daily RSI 61 via BRS path means it is not a pullback to 40; treat as lowest-conviction. Enter only if market-open sees no gap-up chase >3% and sector data (P2) resolves; otherwise skip and keep as watch. Stop ~2.2% below.
- Correlation note: MU + (watch NEM/others) none; MU and META are both tech-adjacent mega-beta — if NFP/yields cause a risk-off open, drop META first, then MU.
