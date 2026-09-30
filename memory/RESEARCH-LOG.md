# Research Log — Last Run: 2026-09-30 05:50 ET (pre-market)

> **Overwritten on every pre-market run.** Git history is the archive. Market-open validates the "Last Run" date matches today.
> Scanner data = 2026-09-29 close. Market-open must re-check live price (chase cap +3%) before ordering.

## Account Snapshot
- Equity: $100,000.00 (paper, PA3FLRNK3PUG, ACTIVE) | Cash: $100,000.00 | Buying power: $400,000.00
- Open P&L: $0.00 (no open positions)
- Weekly entries (week of 2026-09-28): 0 / 3 | Open positions: 0 / 5

## Global Gate (P1) — POSITIVE ✓ (borderline, macro caution)

| Indicator | Value | Status |
|-----------|-------|--------|
| SPX Monthly RSI | 79.74 | ✓ > 60 |
| SPX Weekly RSI | 60.005 | ⚠ Barely > 60 (was 63.84 last week — falling) |
| VIX | 16.03 | ✓ < 18 |
| DXY 20d change | +1.69% | ✓ < 3% (firming) |
| 10Y Yield | 5.255% (+46bp / 20d) | ⚠ Spiking; crossed 5% — one soft bearish signal |
| SPX Price | 7,670.84 | |

**Verdict: POSITIVE** — only one clear bearish signal (10Y), so the "any 2 bearish" rule is not triggered, and the scanner gate passed. **Fragile:** if SPX weekly RSI closes ≤ 60 or the 10Y keeps surging, the gate flips to INDECISIVE → no trades, and any open positions should be reviewed per Part 3 exit rule.

## Event Risk
- Fed: hiked 25bp to 3.75–4.00% on 2026-09-16; next FOMC Oct 27–28 — none within 3 days.
- Earnings (Part 7, within 5 trading days): not verified per-ticker for today's picks (no earnings-calendar source available in this run). Market-open should check INTC/AMAT/AMGN before ordering; INTC, AMAT and LRCX typically report mid/late Oct (outside window), AMGN late Oct.
- Quarter-end (Sep 30) flows; 10Y above 5% is the key macro risk.

## Risk Factors
- Gate is borderline (weekly RSI 60.005, 10Y surging).
- Sector P2: Tech (XLK W-RSI 65.25) and Healthcare (XLV 62.98) pass; all others fail (XLE 56.42, XLC 48.70, XLF 45.24, XLI 42.43, XLB 42.05, XLP 41.34, XLRE 36.87, XLY 39.97, XLU 31.90).
- INTC + AMAT are both Technology / semis — correlated; entering both concentrates sector risk (2 × ~5% of equity; max risk ~$290).
- INTC: BULLISH tier via daily BRS, but daily RSI is 58.5 (not in the 39–45 pullback zone) — more extended than a classic pullback entry.
- Scanner universe: 137 tickers scanned (config/universe.json only; S&P 500 constituent fetch unavailable) — not the full ~503.
- No held positions → no -7% alerts.

## Scanner Output — 137 scanned, 0 errors, gate passed

### EXTREMELY BULLISH PULLBACK
| Ticker | M-RSI | W-RSI | D-RSI | BRS | Price | Score | Decision |
|--------|-------|-------|-------|-----|-------|-------|----------|
| AMGN (Healthcare) | 68.06 | 60.98 | 60.6 | ✓ | 423.54 | 8/10 | ENTER ✅ |
| META (Comm Svcs) | 66.12 | 62.48 | 64.5 | ✓ | 738.96 | 5/10 | WATCH (P2 fail) |
| DE (Industrials) | 69.46 | 61.58 | 53.69 | ✓ | 680.36 | 3/10 | WATCH (P2 fail) |

### EXTREMELY BULLISH MOMENTUM (max 8)
| Ticker | M-RSI | W-RSI | D-RSI | Price | Score | Decision |
|--------|-------|-------|-------|-------|-------|----------|
| MU | 72.8 | 64.03 | 59.75 | 1064.97 | 4/8 | below threshold |
| MRVL | 69.68 | 65.14 | 61.59 | 263.27 | 4/8 | below threshold |
| VEEV | 67.95 | 68.85 | 64.5 | 278.46 | 4/8 | below threshold |
| FTNT | 87.6 | 72.39 | 59.74 | 176.01 | 3/8 | below threshold |
| PLTR | 66.56 | 61.58 | 60.4 | 186.98 | 3/8 | below threshold |
| QQQ (ETF) | 72.61 | 61.4 | 59.25 | 737.96 | — | not scored (index ETF) |

### BULLISH (scored)
| Ticker | M | W | D | Price | Score | Decision |
|--------|---|---|---|-------|-------|----------|
| INTC (Tech) | 62.03 | 59.67 | 58.49 | 115.97 | 10/10 | ENTER ✅ |
| AMAT (Tech) | 60.58 | 57.49 | 62.97 | 512.01 | 8/10 | ENTER ✅ |
| LRCX (Tech) | 63.03 | 56.83 | 59.52 | 323.88 | 6/10 | ENTER-eligible, budget-capped (P9: at resistance 0%) |
| LLY (Healthcare) | 75.09 | 57.28 | 56.07 | 1185.09 | 6/10 | ENTER-eligible, budget-capped (P9: 0.21% to res) |
| CSCO | 74.93 | 51.15 | 42.44 | 106.94 | 5/10 | WATCH |
| COP | 60.44 | 53.83 | 41.43 | 125.44 | 4/10 | WATCH |
| KO / MA | | | | 86.87 / 563.53 | 3/10 | WATCH |
| C / ETN / EQIX | | | | | 2/10 | WATCH |
| NEM | | | | 117.06 | 1/10 | WATCH |
| Unscored (P2 sector fail, not near threshold): KLAC, MPWR, CAT, GOOGL, GE, COST, WMT | | | | | | skipped |

Also filtered near resistance by scanner: DDOG, ASML, TXN, BRK.B.

## Today's Entry Plan
**Trade/hold decision: ENTER 3 trades** (uses the full weekly budget of 3; ranked by score). Risk sized at 2% cap, ≤5% of equity each. Order type: limit at/near entry; **skip if live price > entry +3% (chase cap)** or the gate has flipped at market open.

| # | Ticker | Tier | Score | Entry ~ | Stop | T1 | R/R | Shares | Order |
|---|--------|------|-------|---------|------|----|-----|--------|-------|
| 1 | INTC | BULLISH | 10/10 | 115.97 | 112.49 (-3.0%) | 125.54 | 2.75 | 43 | Limit |
| 2 | AMAT | BULLISH | 8/10 | 512.01 | 496.65 (-3.0%) | 549.65 | 2.45 | 9 | Limit |
| 3 | AMGN | EB_PULLBACK | 8/10 | 423.54 | 410.83 (-3.0%) | 448.96 | 2.00 | 11 | Limit |

**Theses:**
- **INTC** — M/W RSI > 60 zone with daily BRS confirmed; Tech sector passes P2 (XLK W-RSI 65.25); only 0.89x red-volume (accumulation), green-volume 1.24x; gap support beneath; 8.3% to resistance. Caveat: daily RSI 58.5, extended.
- **AMAT** — Semis leadership, sector strong, 7.35% room to resistance, volume supportive (green 1.10x / red 0.94x). Fails only P7 (11.5% above support) → stop is the tight 3% cap.
- **AMGN** — Only EB_PULLBACK hit; M 68 / W 61, BRS ✓, 5.2% to resistance, red volume light (0.79x), Healthcare passes P2. Also diversifies away from Tech.
- Not entered (budget cap): LRCX and LLY (score 6, both fail P9 at resistance) — watchlist; revisit on pullback/breakout.
- Correlation note: INTC + AMAT = 2 Tech semis. Total planned risk ≈ $428 (0.43% of equity).
