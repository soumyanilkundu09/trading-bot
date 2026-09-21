# Research Log — Last Run: 2026-09-21 12:20 ET (pre-market routine, run late — market already open)
*(Manual run at 12:15 ET Monday. Scanner RSI/support/resistance data = Friday 2026-09-18 close. Live prices from Alpaca at run time. The 09:45 market-open routine did not place any trades today.)*

> This file is **overwritten on every pre-market run**. Git history is the archive.
> Market-open routine validates the "Last Run" date matches today before proceeding.

---

## Account Snapshot
- Equity: $100,000.00 (paper, PA3FLRNK3PUG, ACTIVE)
- Cash: $100,000.00 | Buying power: $400,000.00
- Open P&L: $0.00 (no open positions)
- Weekly entries: 0 / 3 | Open positions: 0 / 5

---

## Global Gate (P1) — POSITIVE ✓ (with macro caution)

| Indicator | Value | Status |
|-----------|-------|--------|
| SPX Monthly RSI | 74.24 | ✓ > 60 |
| SPX Weekly RSI | 63.95 | ✓ > 60 (up from 60.87 on Fri) |
| VIX | 14.87 | ✓ < 18 |
| DXY 20d change | +1.42% | ✓ < 3% |
| 10Y Yield | 4.967% (+26bp / 20d) | ⚠ Elevated and rising; near 5% |
| SPX Price | $7,746.96 | Up ~1.3% vs Fri log ($7,650.50) |

**Verdict: POSITIVE. Proceed with scan.** All hard thresholds pass. Soft warning: 10Y yield has risen 26bp in 20 days and sits just under 5%, and the Fed hiked (see Event Risk). Only one soft bearish signal, so the "any 2 bearish" rule is not triggered.

---

## Event Risk
- **Fed:** FOMC raised the funds rate 25bp to 3.75–4.00% on 2026-09-16 ([CNBC](https://www.cnbc.com/2026/09/16/fed-rate-decision-september-2026.html)). Next FOMC is Oct 27–28 — **no Fed event within 3 days**. Note: this is a tightening cycle, a headwind for growth/long-duration names; the Friday log did not mention the hike.
- **Earnings (Part 7 disqualifier: within 5 trading days):** none for the ENTER names — ASML Oct 14, LLY Oct 29, CRWD Dec 1 (est.).
- 10Y yield at 4.967%. If it closes above 5% and holds, re-evaluate the gate at the next run.

---

## Risk Factors
- **Scan universe degraded:** Wikipedia S&P 500 fetch failed (HTTP 403), so the scanner fell back to `config/universe.json` only — **137 tickers scanned, not ~503**. Names outside universe.json (rest of the S&P 500) were not scanned today. Consider fixing the constituent source (e.g. a cached CSV or different endpoint).
- **Stale scan vs live market:** scanner prices are Friday closes (e.g. LLY 1152.46). The market rallied today (SPX ~+1.3%), so live entries are above scan prices. Chase check (max +3%) applied below.
- **Tech sector recovered:** XLK weekly RSI 63.37 (was 56.98 Friday) → Technology now passes P2. This is why CRWD/ASML/DDOG/TXN scores jumped vs Friday.
- Macro: Fed hiking + 10Y near 5%.
- No held positions → no -7% stop-outs to flag.

---

## Scanner Output — 137 tickers scanned, 0 errors, gate passed

### Sector ETF Snapshot (P2 context — Weekly RSI)

| Sector ETF | Weekly RSI | Monthly RSI | P2 (>60) |
|------------|-----------|-------------|----------|
| Energy (XLE) | 63.91 | 66.01 | ✓ PASS (no universe hits) |
| Technology (XLK) | 63.37 | 73.41 | ✓ PASS (new vs Fri) |
| Healthcare (XLV) | 60.77 | 70.92 | ✓ PASS |
| Financials (XLF) | 54.54 | 67.66 | ✗ |
| Communication Svcs (XLC) | 47.53 | 58.87 | ✗ |
| Materials (XLB) | 45.57 | 59.64 | ✗ |
| Consumer Staples (XLP) | 44.75 | 63.76 | ✗ |
| Industrials (XLI) | 43.00 | 62.85 | ✗ |
| Consumer Disc. (XLY) | 42.48 | 49.44 | ✗ |
| Real Estate (XLRE) | 41.84 | 61.77 | ✗ |
| Utilities (XLU) | 35.37 | 55.57 | ✗ |

### Extremely Bullish Pullback — 0 candidates

### Extremely Bullish Momentum — 2 scanned

| Ticker | Sector | M-RSI | W-RSI | D-RSI | Score | Max | Scorer | Final call | Notes |
|--------|--------|-------|-------|-------|-------|-----|--------|-----------|-------|
| CRWD | Technology | 83.4 | 68.0 | 60.4 [BRS] | 8/8 | 8 | ENTER | **BLOCKED (chase)** | Live $247.28 = +4.07% vs Fri close, exceeds 3% max chase ($244.74). Nearest resistance $250.30 now only ~1.2% away (P9 would fail on live data). Daily bearish divergence flagged. Monthly RSI 83 extended. → Watchlist, re-check on pullback |
| AAPL | Technology | 73.4 | 64.9 | 63.8 | 3/8 | 8 | SKIP | SKIP | P9 (2.13% to res), P10 (red vol 1.24x) |

### Bullish — 16 scanned

| Ticker | Sector | M-RSI | W-RSI | D-RSI | Score | Max | Scorer | Key blockers |
|--------|--------|-------|-------|-------|-------|-----|--------|--------------|
| **ASML** | Technology | 63.3 | 53.5 | 48.5 [BRS] | **8/10** | 10 | **ENTER** | P8 (green vol 0.99x), P10 (red vol 1.40x — see caveats) |
| **LLY** | Healthcare | 74.1 | 54.4 | 47.0 [BRS] | **6/10** | 10 | **ENTER (marginal)** | P9 (1.52% to res) |
| DDOG | Technology | 65.4 | 55.0 | 48.9 [BRS] | 5/10 | 10 | SKIP | P9 (2.04%), P10 (red vol 1.08x) |
| TXN | Technology | 62.9 | 51.0 | 51.2 [BRS] | 5/10 | 10 | SKIP | P9 (0.23% — at resistance), P10 (1.01x) |
| SCHW | Financials | 64.0 | 57.6 | 42.3 [BRS] | 4/10 | 10 | SKIP | P2 (Fin 54.54), P9 (1.01%) |
| NVDA | Technology | 70.6 | 56.9 | 54.0 [BRS] | 4/10 | 10 | SKIP | P7 (2.57% from support), P9 (1.27%) |
| CSCO | Technology | 78.1 | 54.1 | 46.1 [BRS] | 4/10 | 10 | SKIP | P8, P9 (2.46%), P10 (1.22x) |
| MA | Financials | 62.6 | 57.2 | 44.1 | 3/10 | 10 | SKIP | P2, P8 (0.95x), P9 (1.98%) |
| CAT | Industrials | 63.8 | 48.0 | 47.8 [BRS] | 3/10 | 10 | SKIP | P2 (Ind 43.0), P8, P9 (2.67%) |
| EQIX | Real Estate | 67.1 | 49.8 | 45.1 [BRS] | 3/10 | 10 | SKIP | P2 (RE 41.84), P8, P9 (2.51%) |
| NBIS | Technology | 68.7 | 55.7 | 52.0 [BRS] | 3/10 | 10 | SKIP | P7, P9 (0.40%), P10 |
| WMT | Cons. Staples | 63.8 | 41.2 | 45.7 [BRS] | 3/10 | 10 | SKIP | P2, P8, P9 (2.50%) |
| MPWR | Technology | 61.3 | 43.7 | 46.4 [BRS] | 2/10 | 10 | SKIP | P7, P8, P9, P10 |
| VZ | Comm. Svcs | 60.1 | 53.0 | 42.1 | 2/10 | 10 | SKIP | P2, P8, P9 (0.11%), P10 |
| C | Financials | 68.9 | 52.0 | 40.9 [BRS] | 2/10 | 10 | SKIP | P2, P8, P9 (1.28%), P10 (1.43x) |
| ETN | Industrials | 60.7 | 56.4 | 54.8 [BRS] | 1/10 | 10 | SKIP | P2, P7, P9 (0.42%), P10 |

### Filtered by Scanner (near resistance < 5%)
11 stocks blocked: DE, MU, TSM, TEM, MRVL, SPY, JPM, QQQ, INTC, META, GOOGL.

---

## Today's Entry Plan

### Trade/Hold Decision: ENTER 2 candidate(s) — ASML (primary), LLY (marginal, lowest priority)
**Weekly budget:** 0/3 used, 0/5 positions. **No orders placed by this routine.** Plans below use live Alpaca prices at 12:15 ET; re-validate at execution (chase ≤ +3% over Fri close, re-run scorer).

#### 1. ASML — BULLISH tier — Score 8/10 — Bracket order
- **Thesis:** Daily BRS confirmed (D-RSI 48.5, up from 42.8). Tech sector (XLK W-RSI 63.4) now passes P2. Price ~2.4% above support $1,639.25 with 6.6% room (Fri basis) to resistance $1,789.29. Last candle green, 1.31x avg volume, closes in upper half.
- **Entry:** ~$1,701.56 live (Fri close $1,679.25; +1.33%; max chase $1,729.63)
- **Stop:** $1,650.51 (−3.0%) — sits just above support $1,639.25; a close below support invalidates the setup
- **T1:** $1,803.65 (2R, exit 50% + trail stop to swing low) | T2: $1,854.69
- **Shares:** 2 | Value ≈ $3,403 (3.4% of equity) | Risk ≈ $102 (0.10% of capital) | R/R at T1: 2.0
- **Order type:** Bracket (market entry, day; stop + T1 atomic)
- **Caveats:** (a) P10 failed — last 4 red candles averaged 1.40x the 20-day volume (all 4 above average): that is conviction selling per the strategy's Adverse Low Move rule, and P8 also missed (0.99x). Score qualifies via P2+P7+P9 (8 pts) only. (b) Score is on Friday's close; at the live price, distance to support is ~3.7% and to resistance ~5.2%, so the P7 buffer has shrunk and P9 is barely above the 5% line. (c) T1 ($1,803.65) is ~0.8% above the nearest resistance ($1,789.29). (d) Earnings Oct 14 — outside the 5-day window.

#### 2. LLY — BULLISH tier — Score 6/10 (threshold minimum) — Bracket order — LOW CONVICTION
- **Thesis:** Daily BRS, healthcare (XLV W-RSI 60.77) just above 60, price sitting on support/CIP/gap (0.45% above $1,147.31), red-candle volume low (0.77x).
- **Entry:** ~$1,158.77 live (Fri close $1,152.46; +0.55%; max chase $1,187.03)
- **Stop:** $1,141.57 (−1.48%)
- **T1:** $1,193.17 (2R) | T2: $1,210.37
- **Shares:** 4 | Value ≈ $4,635 (4.6%) | Risk ≈ $69 | R/R at T1: 2.0
- **Order type:** Bracket
- **Caveats:** Fails P9 (the highest-weight parameter, 4 pts). Nearest resistance is $1,170.02, only ~1.0% above the live price, and T1 sits ~2% *beyond* it — reward to actual resistance is only ~0.65R. XLV just crossed 60 and could slip back under (P2 flip → score 4/10). Recommend market-open only take this if price pulls back toward support (~$1,147–1,152) or clears $1,170 on volume; otherwise skip.

**Priority if only one is taken:** ASML > LLY. Neither is required — HOLD (no trade) is a valid outcome.

### Blocked / Watch-only (no entry)
- **CRWD (8/8 scorer ENTER → BLOCKED):** 8F alert — chase rule (live +4.07% > 3% cap), price ~1.2% from resistance $250.30 at live, bearish daily divergence, monthly RSI 83.4 extended. Next action: watchlist; reconsider only after a pullback (support gap zone $213–216) with fresh scorer run.
- **Watchlist only:** DDOG (5), TXN (5), SCHW (4), NVDA (4), CSCO (4), MA (3), CAT (3), EQIX (3)

---

## Summary
- Gate: POSITIVE (SPX M/W 74.2/64.0, VIX 14.9; 10Y 4.97% and Fed hike = caution)
- Tickers scanned: 137 (degraded — S&P 500 constituent fetch failed) | Errors: 0
- EB Pullback: 0 | EB Momentum: 2 scanned, 1 scorer-ENTER (CRWD, blocked on chase) | Bullish: 16 scanned, 2 ENTER (ASML 8/10, LLY 6/10)
- Filtered by scanner: 11 (near resistance)
- Plan: ASML primary (2 sh), LLY marginal (4 sh, conditional). Budget 0/3.
