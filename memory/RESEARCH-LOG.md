# Research Log — Last Run: 2026-10-09 06:00 ET (pre-market)
*(Scanner RSI/support/resistance = Thu 2026-10-08 close. Run before the open; no live-price chase check possible yet — market-open must apply the 3% chase cap against live quotes.)*

> This file is **overwritten on every pre-market run**. Git history is the archive.
> Market-open routine validates the "Last Run" date matches today before proceeding.

---

## Account Snapshot
- Equity: $100,000.00 (paper, PA3FLRNK3PUG, ACTIVE)
- Cash: $100,000.00 | Buying power: $400,000.00
- Open P&L: $0.00 (no open positions)
- Weekly entries: 0 / 3 (week of 2026-10-05; no positions or closed trades on record) | Open positions: 0 / 5

---

## Global Gate (P1) — POSITIVE ✓ (with macro caution)

| Indicator | Value | Status |
|-----------|-------|--------|
| SPX Monthly RSI | 80.07 | ✓ > 60 |
| SPX Weekly RSI | 64.12 | ✓ > 60 |
| VIX | 15.17 | ✓ < 18 |
| DXY | 102.08, +2.64% / 20d | ✓ < 3% (close to threshold) |
| 10Y Yield | 5.231% (+25.6bp / 20d) | ⚠ Above 5% and rising |
| SPX Price | $7,765.36 | |

**Verdict: POSITIVE. Proceed with scan.** Hard thresholds pass. Two soft warnings (10Y yield >5%, DXY near the 3% cap) — neither is a "spike", so the "any 2 bearish" rule is not triggered, but this is the closest the gate has been. Re-evaluate if DXY 20d > 3% or 10Y keeps climbing.

---

## Event Risk
- **Fed:** last FOMC hike was 2026-09-16 (3.75–4.00%); next FOMC Oct 27–28 — no Fed event within 3 days.
- **Earnings within 5 trading days:** none for the ENTER names (MRVL Dec 1, COP Nov 5, MRK Oct 29, LRCX Oct 21, KLAC Oct 28).
- Macro: tightening cycle + 10Y >5% is a headwind for long-duration/growth names.

---

## Risk Factors
- **Scan universe degraded:** scanner covers `config/universe.json` only (137 tickers), not the full S&P 500 (constituent fetch fallback). Names outside the universe were not scanned.
- **Sector P2 blocks:** Industrials (XLI W-RSI 41.4), Materials (43.3), Real Estate (35.1), Financials (47.0) fail P2 → CAT, DE, ETN, UNP, NEM, EQIX, C capped.
- **Concentration:** MRVL, LRCX, KLAC are all Semis/Technology — take at most one of them unless the others pull back.
- MRK stop is extremely tight (0.56%, support at 0.06% below price) — noise-stop risk; market-open may use a wider structural stop if still ≤ 2% risk.
- No held positions → no -7% alerts.

---

## Scanner Output — 137 scanned, 0 errors, gate passed

### Extremely Bullish Pullback — 2

| Ticker | Sector | M-RSI | W-RSI | D-RSI | Score | Max | Scorer | Notes |
|--------|--------|-------|-------|-------|-------|-----|--------|-------|
| COP | Energy | 63.6 | 60.4 | 60.0 [BRS] | 6 | 10 | ENTER (marginal) | P9 fail (1.24% to res); gap support 1.13% below |
| META | Comm Svcs | 65.0 | 60.1 | 57.5 [BRS] | 4 | 10 | SKIP | P2 (XLC W-RSI 50.1), P9 (3.56%) |

### Extremely Bullish Momentum — 7

| Ticker | Sector | M-RSI | W-RSI | D-RSI | Score | Max | Scorer | Notes |
|--------|--------|-------|-------|-------|-------|-----|--------|-------|
| **MRVL** | Technology | 70.6 | 67.1 | 61.2 | **8** | 8 | **ENTER** | 9.16% to resistance, green vol 1.26x |
| VEEV | Technology | 69.3 | 69.0 | 62.7 | 4 | 8 | SKIP | P9 (1.23%) |
| ANET | Technology | 74.2 | 67.3 | 60.0 | 4 | 8 | SKIP | P9 (0.21%) |
| AMD | Technology | 76.8 | 69.0 | 61.4 | 3 | 8 | SKIP | P8, P9 (2.89%) |
| AAPL | Technology | 74.1 | 64.5 | 61.2 | 3 | 8 | SKIP | P8, P9 (0.36%) |
| CRWD | Technology | 84.6 | 70.6 | 59.5 [BRS] | 2 | 8 | SKIP | at resistance (0.07%), weak volume |
| XOM | Energy | 67.4 | 62.0 | 63.6 | 2 | 8 | SKIP | at resistance (0.05%) |

### Bullish — 15

| Ticker | Sector | M-RSI | W-RSI | D-RSI | Score | Max | Scorer | Key blockers |
|--------|--------|-------|-------|-------|-------|-----|--------|--------------|
| **MRK** | Healthcare | 72.7 | 59.5 | 44.6 [BRS] | **7** | 10 | **ENTER** | P2 (XLV W-RSI 58.3), P10 (red vol 1.12x) |
| LRCX | Technology | — | 54.6 | 52.1 | 6 | 10 | ENTER (marginal) | P9 (0.33% to res) |
| KLAC | Technology | — | 52.7 | 56.0 | 6 | 10 | ENTER (marginal) | P9 (2.74% to res) |
| ASML | Technology | 64.8 | 56.4 | 51.3 [BRS] | 4 | 10 | SKIP | P8, P9 (1.04%), P10 (1.40x) |
| DE | Industrials | — | 55.8 | 42.0 | 4 | 10 | SKIP | P2 (41.4), P9 |
| MPWR | Technology | — | 52.9 | 53.6 | 4 | 10 | SKIP | P7, P9 |
| AMAT | Technology | — | 55.7 | 55.5 | 3 | 10 | SKIP | P7, P9 (0.23%), P10 |
| LLY | Healthcare | — | 55.2 | 51.5 | 3 | 10 | SKIP | P2, P9 (0.04%), P10 |
| CAT | Industrials | — | 46.3 | 43.3 | 3 | 10 | SKIP | P2, P9, P10 |
| C | Financials | — | 48.2 | 39.4 | 3 | 10 | SKIP | P2, P8, P9 |
| AMGN | Healthcare | 63.6 | 56.8 | 50.3 | 2 | 10 | SKIP | P2, P7, P9 |
| NEM | Materials | — | 52.7 | 43.2 | 2 | 10 | SKIP | P2, P8, P9, P10 |
| UNP | Industrials | — | 50.5 | 46.0 | 2 | 10 | SKIP | P2, P8, P9 (0.14%), P10 |
| EQIX | Real Estate | — | 48.5 | 44.1 | 2 | 10 | SKIP | P2 (35.1), P8, P9, P10 |
| ETN | Industrials | — | 54.7 | 48.8 | 1 | 10 | SKIP | P2, P7, P9, P10 |

Near-misses filtered by scanner (not added): DDOG, V, KO, CSCO, MA, EOG, TXN, GOOGL, COST, WMT, LIN.

---

## Today's Entry Plan
**Trade/hold decision: ENTER 2 trades (MRVL, MRK) + 1 conditional (COP). Max 3 new entries this week; LRCX/KLAC watch-only (Tech concentration).**

### 1. MRVL — EB Momentum, 8/8 — ENTER
- Thesis: M-RSI 70.6 / W-RSI 67.1 / D-RSI 61.2 (momentum zone), sector XLK W-RSI 66.8 passes P2, 9.16% clear to resistance, green-volume 1.26x.
- Entry ~$274.73 (scan close) — skip if live > $282.97 (+3% chase cap). Stop $266.49 (-3.0%). Target: none — trail 3-bar daily low; exit on BRS/stop.
- Shares 18 (~$4,945, 4.95% of equity; risk ~$148). Order: market/bracket stop per config.

### 2. MRK — Bullish, 7/10 — ENTER
- Thesis: M-RSI 72.7, W-RSI 59.5, D-RSI 44.6 in pullback zone with BRS; price sits on support (0.06%), 5.52% to resistance.
- Entry ~$142.42 — skip if live > $146.69. Stop $141.62 (-0.56%, very tight; acceptable to use a wider structural stop if risk ≤ 2%). T1 $150.28 (close 50%, trail rest). R/R ≈ 9.8 on scorer stop.
- Shares 35 (~$4,985; risk ~$28 on scorer stop). Earnings Oct 29 (>5 trading days).

### 3. COP — EB Pullback, 6/10 — CONDITIONAL (marginal)
- Thesis: M-RSI 63.6 / W-RSI 60.4, D-RSI 60 with BRS, Energy sector passes P2 (XLE 63.4), gap support 1.1% below. P9 failed (resistance only 1.24% above) → T1 $138.56 sits beyond resistance.
- Enter only on a pullback toward ~$132–133 or a break above resistance (~$135.9) with volume. Entry ref $134.20, stop $132.02, T1 $138.56, T2 $140.74, shares 37 (~$4,965, risk ~$81).

### Watch-only
LRCX (6/10, 0.33% to res), KLAC (6/10, 2.74% to res): enter only if MRVL is skipped and one is clear of resistance; do not stack >1 semi.
