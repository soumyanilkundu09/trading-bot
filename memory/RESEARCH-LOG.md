# Research Log — Last Run: 2026-10-14 08:30 ET (pre-market)

> Overwritten on every pre-market run. Git history is the archive.
> Scanner RSI/support/resistance = prior close (2026-10-13). Entry prices are scorer reference prices; market-open must re-check live price (chase cap 3%).

## Account Snapshot
- Equity: $100,000.00 (paper, PA3FLRNK3PUG, ACTIVE) | Cash: $100,000.00 | Buying power: $400,000.00
- Open P&L: $0.00 (no open positions) | Weekly entries: 0 / 3 | Open positions: 0 / 5

## Global Gate (P1) — POSITIVE ✓ (macro caution)

| Indicator | Value | Status |
|-----------|-------|--------|
| SPX Monthly RSI | 80.38 | ✓ > 60 |
| SPX Weekly RSI | 65.18 | ✓ healthy |
| VIX | 15.25 | ✓ < 25 |
| DXY | 102.24 (+2.02% / 20d) | ✓ < 3% |
| US 10Y yield | 5.217% (+21bp / 20d) | ⚠ above 5%, rising — soft headwind, not a spike |

**Verdict: POSITIVE.** One soft caution (10Y > 5%).

## Event Risk
- Next FOMC Oct 27–28 (decision Oct 28, 2:00 PM ET) — **not within 3 days**. No major macro event flagged. (Sources disagree on the current policy-rate level; irrelevant to this gate.)

## Risk Factors
- 10Y yield > 5% and rising: headwind for growth/long-duration names (NBIS, DDOG).
- Sector P2: Industrials W-RSI 41.7, Materials 45.5, Consumer Disc 45.8, Staples 51.6 — all below threshold (blocks ETN, DE, NEM, ABNB, PM).
- Gap-down filters (2026-10-12): MU, INTC.
- Held positions below -7%: none (no positions).

## Scanner Output
Scanned 137 | Errors 0 | Filtered 11. Gate passed.

**EXTREMELY BULLISH PULLBACK**
| Ticker | Sector | M/W/D RSI | Price | Score | Decision |
|---|---|---|---|---|---|
| DDOG | Technology | 72.6 / 64.0 / 64.3 (BRS) | 283.30 | 4/10 | WATCH (P7 4.39% from support, P9 2.31% to res) |

**EXTREMELY BULLISH MOMENTUM** (SPY, IGV are ETFs — not traded)
| Ticker | Sector | M/W/D RSI | Price | Score | Decision |
|---|---|---|---|---|---|
| AAPL | Technology | 73.5 / 65.0 / 60.5 | 341.33 | 3/8 | SKIP (0.1% to resistance, red vol 1.15x) |
| ABBV | Healthcare | 73.0 / 65.6 / 61.7 | 274.24 | 1/8 | SKIP (P2 59.33, P9, P10) |
| PM | Staples | 65.0 / 61.4 / 61.8 | 199.37 | 2/8 | SKIP (P2, P9) |

**BULLISH**
| Ticker | Sector | M/W/D RSI | Price | Score | Decision |
|---|---|---|---|---|---|
| NBIS | Technology | 63.8 / 50.9 / 41.7 | 206.90 | **9/10** | **ENTER** |
| MRK | Healthcare | 60.8 / 58.4 / 44.2 (BRS) | 141.97 | **7/10** | **ENTER** |
| DE | Industrials | 68.3 / 54.7 / 45.2 | 650.01 | 3/10 | WATCH (P2 41.7) |
| ETN | Industrials | 66.1 / 56.0 / 50.7 | 428.35 | 3/10 | WATCH (P2) |
| NEM | Materials | 63.4 / 52.5 / 43.8 | 115.57 | 3/10 | WATCH (P2, P8, P9) |
| LRCX | Technology | 62.3 / 50.5 / 42.9 | 301.41 | 3/10 | WATCH (at resistance 0.19%, P7 5.5% from support) |
| ABNB | Cons. Disc. | 66.8 / 56.4 / 51.5 | 165.59 | 0/10 | BELOW THRESHOLD |

## Today's Entry Plan
**Trade/hold decision: ENTER 2 trades (NBIS, MRK)** — weekly budget 0/3 → 2/3 after both.

### 1. NBIS — BULLISH tier, score 9/10 (Technology; sector W-RSI 64.89 ✓)
- Thesis: M-RSI 63.8, W-RSI 50.9, daily RSI 41.7 pulling back into the 40 zone, sitting right on support (0.02%). Only P10 fails (red vol 1.21x).
- Entry ~$206.90 | Stop $205.82 | T1 $223.31 | R/R 15.2 | Shares 24 (~$4,966, 4.97%) | Risk ~$26
- Order: limit at/near $206.90; skip if live price > ~$213.10 (3% chase cap).
- ⚠ Caution: stop is only 0.52% below entry (tight, noise-prone; scorer's T2 $210.14 is below T1 — likely a scorer quirk). Market-open should confirm a bullish daily candle holding support and consider a structurally wider stop (still capped by 7% max-stop and 2% risk). High-beta name amid 10Y > 5%.

### 2. MRK — BULLISH tier, score 7/10 (Healthcare; sector W-RSI 59.33 — P2 fail, still ≥ 6)
- Thesis: M-RSI 60.8, W-RSI 58.4, daily RSI 44.2 with BRS in the 40 zone; 2.2% above support, 5.85% to resistance.
- Entry ~$141.97 | Stop $138.12 | T1 $150.28 | T2 $153.52 | R/R 2.16 | Shares 35 (~$4,969, 4.97%) | Risk ~$135
- Order: limit at/near $141.97; skip if live price > ~$146.23. Fails: P2 (sector 59.33), P10 (red vol 1.03x).

Both are separate sectors (Tech, Healthcare); no sector-loss blocks. Respect max 3/week, 5 open.
