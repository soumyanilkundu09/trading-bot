# Research Log — Last Run: 2026-10-26 05:45 ET (pre-market)

> Overwritten on every pre-market run. Git history is the archive.
> Market-open routine validates the "Last Run" date matches today before proceeding.
> Note: run executed ~05:45 ET (earlier than the usual 08:30); scanner data = Fri 2026-10-23 close.

---

## Account Snapshot
- Equity: $100,000.00 (paper, PA3FLRNK3PUG, ACTIVE)
- Cash: $100,000.00 | Buying power: $400,000.00
- Open P&L: $0.00 (no open positions)
- Weekly entries: 0 / 3 | Open positions: 0 / 5

---

## Global Gate (P1) — POSITIVE ✓ (with caution: weekly RSI below 60, FOMC this week)

| Indicator | Value | Status |
|-----------|-------|--------|
| SPX Monthly RSI | 78.29 | ✓ > 60 |
| SPX Weekly RSI | 55.71 | ⚠ < 60 (above scanner's 50 floor; not "> 60" per strict Part 3 wording) |
| SPX price | 7,623.68 | — |
| VIX | 19.17 | ✓ < 25 (caution band 18–25) |
| DXY 20d change | +0.41% (101.78) | ✓ < 3% |
| 10Y Yield | 4.988% (−25bp / 20d) | ⚠ Near 5% but falling |

Scanner gate (M>60, W>50, VIX<25, DXY<3%) passed. Verdict: POSITIVE, low-conviction.

---

## Event Risk
- **FOMC meeting Tue–Wed Oct 27–28 (decision Wed 14:00 ET) — within 3 days.** Part 7 avoid-list: "Major central bank event within 3 days". Caution flag for market-open.
- Earnings: MRK Oct 29 (inside 5-day window → blocked); MPC Nov 3 (6 trading days out, just outside window); MRVL Dec 1 (clear). Big-tech earnings week (AAPL etc.) broadly.

---

## Risk Factors
- Sector weekly RSI (P2 >60): only **Energy (XLE 69.4), Healthcare (XLV 67.6), Staples (XLP 62.0)** pass. Technology XLK 52.7, Financials 54.4, Materials 52.6, Cons Disc 47.2, Utilities 47.0, Real Estate 46.0, Industrials 36.7, Comm Svcs 38.5 all fail.
- Technology has lost P2 since last run (XLK W-RSI 63.4 → 52.7); CRWD and DDOG deteriorated sharply.
- No open positions, so no held-position stress.

---

## Scanner Output
Scanned: 137 | Errors: 0 | Filtered (near resistance etc.): 8

**Sector ETF weekly/monthly RSI:** XLK 52.7/67.8 · XLF 54.4/56.9 · XLV 67.6/63.0 · XLE 69.4/66.3 · XLY 47.2/62.5 · XLP 62.0/59.5 · XLI 36.7/59.4 · XLB 52.6/61.0 · XLU 47.0/59.4 · XLRE 46.0/55.4 · XLC 38.5/55.2

### EXTREMELY BULLISH PULLBACK
| Ticker | Sector | Price | M-RSI | W-RSI | D-RSI | BRS | Score | Decision |
|--------|--------|-------|-------|-------|-------|-----|-------|----------|
| CRWD | Technology | 257.55 | 80.66 | 63.18 | 55.92 | Y | 1/10 | SKIP |
| MRK | Healthcare | 145.27 | 63.17 | 61.72 | 49.47 | Y | 5/10 | SKIP (earnings Oct 29) |

### EXTREMELY BULLISH MOMENTUM
| Ticker | Sector | Price | M-RSI | W-RSI | D-RSI | BRS | Score | Decision |
|--------|--------|-------|-------|-------|-------|-----|-------|----------|
| MPC | Energy | 457.27 | 82.11 | 73.51 | 59.70 | N | 7/8 | ENTER (conditional, see plan) |
| KO | Cons. Staples | 92.70 | 68.72 | 65.93 | 59.69 | Y | 3/8 | SKIP |
| HCA | Healthcare (Microcap list) | 469.33 | 60.26 | 61.11 | 64.61 | N | 3/8 | SKIP |
| DHR | Healthcare | 230.44 | 61.95 | 62.07 | 59.66 | N | 2/8 | SKIP |
| AAPL | Technology | 347.69 | 74.35 | 67.01 | 63.76 | N | 1/8 | SKIP |
| XLV | ETF (sector) | 179.25 | 63.00 | 67.64 | 63.95 | N | n/a | Not traded (sector ETF) |

### BULLISH
| Ticker | Sector | Price | M-RSI | W-RSI | D-RSI | BRS | Score | Decision |
|--------|--------|-------|-------|-------|-------|-----|-------|----------|
| MRVL | Technology | 228.61 | 60.78 | 53.43 | 41.13 | Y | 8/10 | ENTER (conditional; P2 fails but scorer ≥6) |
| CEG | Utilities | 253.39 | 60.95 | 44.74 | 40.65 | Y | 4/10 | WATCH |
| DE | Industrials | 646.03 | 67.73 | 54.22 | 46.61 | Y | 2/10 | WATCH |
| TSM | Technology | 418.37 | 64.59 | 51.30 | 41.28 | Y | 3/10 | WATCH |
| CSCO | Technology | 106.49 | 74.83 | 49.32 | 41.80 | Y | 3/10 | WATCH |
| PANW | Technology | 380.61 | 69.16 | 59.02 | 52.32 | Y | 0/10 | WATCH |
| DDOG | Technology | 269.65 | 70.28 | 58.57 | 53.21 | Y | 0/10 | WATCH |

---

## Today's Entry Plan
**Trade/hold decision: HOLD by default — 2 conditional candidates (MPC, MRVL). FOMC decision Wed Oct 28 is within the 3-day central-bank-event window (Part 7).**

Recommendation for market-open: do not enter on Monday by default. If market-open elects to override the FOMC caution, use the plans below, re-score with `--live`, and enforce the 3% chase cap and guardrails. Both are paper trades at ≤5% position size.

### 1. MRVL — Technology, BULLISH tier, score 8/10
- Thesis: Daily RSI 41.1 in 39–45 zone with BRS; price 0.8% above support; 5.06% room to resistance; red-day volume light (0.94x), green volume strong (1.18x). Only P2 fails (XLK W-RSI 52.7). Earnings Dec 1, clear.
- Entry ~228.61 (limit) | Stop 225.65 (−1.29%) | T1 240.18 | R/R 3.9 | 21 shares (~$4.8k, 4.8% equity, risk ~$62) | Order: limit at/under 228.61 (max chase 3% → 235.47).
- Caveat: tight stop (1.3%) is vulnerable to FOMC-day volatility; sector is weakening.

### 2. MPC — Energy, EB MOMENTUM tier, score 7/8
- Thesis: M/W-RSI 82.1/73.5, daily RSI 59.7 in momentum zone; Energy is the strongest sector (XLE W-RSI 69.4); 6.09% to resistance. P10 fails (red vol 1.23x).
- Entry ~457.27 | Stop 443.55 (−3.0%) | No fixed T1: trail with 3-bar daily low; exit on BRS | 10 shares (~$4.57k, 4.6% equity, risk ~$137) | Order: limit; max chase 3% → 470.99.
- Caveat: extended (monthly RSI >80); earnings Nov 3 is 6 trading days out — exit/trim decision needed before then.

### Blocked / skipped notes
- MRK: earnings Oct 29 (within 5 days) — blocked regardless of score.
- CRWD/DDOG/PANW/AAPL: Technology P2 failure plus near-resistance/volume issues.
