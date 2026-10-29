# Research Log — Last Run: 2026-10-29 05:45 ET (pre-market)

> Overwritten on every pre-market run. Git history is the archive. Scanner data = 2026-10-28 close.

## Account Snapshot
- Equity: $100,000.00 (paper, PA3FLRNK3PUG, ACTIVE) | Cash: $100,000.00 | Buying power: $400,000.00
- Open P&L: $0.00 (no open positions)
- Weekly entries: 0 / 3 | Open positions: 0 / 5

## Global Gate (P1) — POSITIVE ✓ (with macro caution)

| Indicator | Value | Status |
|-----------|-------|--------|
| S&P 500 Monthly RSI | 79.91 | ✓ > 60 |
| S&P 500 Weekly RSI | 60.09 | ✓ barely > 60 (thin margin) |
| VIX | 17.05 | ✓ < 25 |
| DXY | 102.28 (+0.35% 20d) | ✓ not spiking |
| US 10Y | 5.045% (-0.19 over 20d) | ⚠ high level, but falling |

Verdict: **POSITIVE**. Weekly RSI is a hair above 60 — a down week would flip the gate.

## Event Risk
- FOMC meeting was scheduled Oct 27–28 (decision already out); I did not verify the outcome, so check for post-FOMC volatility at the open.
- 10Y yield above 5% is a macro headwind. No other major event checked.

## Risk Factors
- Technology sector weekly RSI 58.18 (< 60) fails P2 for all tech names.
- Industrials W-RSI 43.85, Real Estate 43.7, Comm Services 35.26 — P2 blocks.
- No open positions, so no held-position stops at risk.

## Scanner Output
Scanned 137 | gate_passed: true | errors: 0 | Pullback 5 | Momentum 5 | Bullish 19

### EXTREMELY_BULLISH_PULLBACK (all pass via BRS; daily RSI is high, so these are extended, not pullbacks)
| Sym | M-RSI | W-RSI | D-RSI | Price | Score |
|-----|-------|-------|-------|-------|-------|
| CRWD | 83.8 | 64.7 | 59.5 | 266.71 | 4/10 |
| TXN | 62.2 | 62.4 | 70.3 | 309.66 | 1/10 |
| PANW | 72.2 | 60.7 | 55.7 | 394.40 | 0/10 |
| DDOG | 72.1 | 60.1 | 56.3 | 278.63 | 0/10 |
| AMD | 73.5 | 60.0 | 53.6 | 578.43 | 1/10 |

### EXTREMELY_BULLISH_MOMENTUM
| Sym | M-RSI | W-RSI | D-RSI | Price | Score |
|-----|-------|-------|-------|-------|-------|
| TMO | 68.9 | 71.4 | 64.1 | 704.85 | 3/10 |
| V | 66.3 | 67.5 | 61.4 | 401.02 | 1/10 |
| DHR | 63.0 | 63.5 | 62.4 | 234.06 | 2/10 |
| XLV | 63.3 | 68.0 | 64.8 | 179.77 | 2/10 |
| IGV | 61.0 | 60.7 | 59.6 | 111.92 | 0/10 |

### BULLISH (watchlist candidates; top scores)
| Sym | W-RSI | D-RSI | Score | Decision |
|-----|-------|-------|-------|----------|
| MRVL | 58.3 | 52.4 | 7/10 | ENTER |
| INTC | 50.0 | 45.0 | 5/10 | WATCH |
| GOOGL | 44.8 | 39.1 | 5/10 | WATCH |
| CEG | 45.9 | 43.9 | 4/10 | WATCH |
| MRK | 56.7 | 43.6 | 4/10 | WATCH |
| MS | 44.7 | 51.0 | 4/10 | WATCH |
| EQIX, DE, QQQ, ANET, ETN, CSCO, NEM, NVDA, FCX, C | | | 2–3/10 | WATCH |
| TSM, ABNB, MU | | | 1/10 | below threshold |

Scored with `strategy_scorer.py` (no live price); P2 fails for MRVL on Tech sector W-RSI 58.18, P8 fails on green volume 0.81x.

## Today's Entry Plan
**Trade/hold decision: ENTER 1 trade (MRVL) — conditional on live-price check at market-open.**

**MRVL** (Technology, BULLISH tier, score 7/10)
- Thesis: Monthly RSI 64.5, weekly 58.3, daily 52.4 with BRS confirmed. The scorer passes support proximity, resistance room and red-volume checks. P2 (sector) and P8 (green volume) fail, so conviction is moderate.
- Entry ~$251.73 (limit near the open price; do not chase above +3%)
- Stop $247.01 (-1.88%) | T1 $265.86 | R/R 2.99
- Shares 19 (~$4,783, 4.78% of equity) | risk ~$89.68 (0.09% of equity)
- Order type: limit. At market-open, re-score with `--live` and verify the chase cap, gap and earnings date.
- Close at T1: 50%, then trail the stop to the prior swing low (BULLISH tier rule).

All other names: watchlist only.
