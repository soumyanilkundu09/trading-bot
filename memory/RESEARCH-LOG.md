# Research Log — Last Run: 2026-09-19 08:30 ET (pre-market)
*(Weekend prep run — data as of Friday 2026-09-18 close)*

> This file is **overwritten on every pre-market run**. Git history is the archive.
> Market-open routine validates the "Last Run" date matches today before proceeding.

---

## Account Snapshot
- Equity: (paper account — check Alpaca dashboard)
- Buying power: (paper account)
- Open P&L: $0.00 (no open positions)

---

## Global Gate (P1) — POSITIVE ✓

| Indicator | Value | Status |
|-----------|-------|--------|
| SPX Monthly RSI | 72.48 | ✓ > 60 |
| SPX Weekly RSI | 60.87 | ✓ Healthy |
| VIX | 14.81 | ✓ < 25 |
| DXY 20d change | +1.44% | ✓ < 3% |
| 10Y Yield | 4.998% | ⚠ Elevated — watch if crosses 5% and holds |
| SPX Price | $7,650.50 | — |

**Verdict: POSITIVE. Proceed with scan.**

---

## Event Risk
- No FOMC decision known in next 3 days. Standard Monday open.
- 10Y yield at 4.998% — approaching 5%. If it crosses and holds, re-evaluate global gate at next run.

---

## Risk Factors
- Technology sector ETF (XLK) W-RSI = 56.98 — below 60 threshold. All Tech stocks fail P2.
- Only Healthcare passes P2 today; universe effectively limited to one sector.
- 10Y yield near 5% acts as macro headwind for growth names.

---

## Scanner Output — 137 tickers scanned, 0 errors

### Sector ETF Snapshot (P2 context)

| Sector ETF | Weekly RSI | P2 Status |
|------------|-----------|-----------|
| Healthcare (XLV) | 60.76 | ✓ PASS |
| Technology (XLK) | 56.98 | ✗ FAIL |
| Financials (XLF) | 54.54 | ✗ FAIL |
| Communication Svcs (XLC) | 47.53 | ✗ FAIL |
| Industrials (XLI) | 43.00 | ✗ FAIL |
| Real Estate (XLRE) | 41.84 | ✗ FAIL |
| Consumer Staples (XLP) | 44.75 | ✗ FAIL |

### Extremely Bullish Pullback — 0 candidates
*No tickers qualified.*

### Extremely Bullish Momentum — 2 scanned, 0 ENTER

| Ticker | Sector | M-RSI | W-RSI | D-RSI | Score | Max | Decision | Key Blockers |
|--------|--------|-------|-------|-------|-------|-----|----------|--------------|
| CRWD | Technology | 83.4 | 68.0 | 60.4 | 2/8 | 8 | SKIP | P2 (Tech W-RSI 56.98 < 60), P9 (5.34% to res) |
| AAPL | Technology | 73.4 | 64.9 | 63.8 | 1/8 | 8 | SKIP | P2 (Tech W-RSI 56.98 < 60), P9 (2.13% to res), P10 (red vol 1.24x avg) |

### Bullish — 16 scanned, 1 ENTER

| Ticker | Sector | M-RSI | W-RSI | D-RSI | Score | Max | Decision | Notes |
|--------|--------|-------|-------|-------|-------|-----|----------|-------|
| **LLY** | Healthcare | 74.1 | 54.4 | 47.0 [BRS] | **6/10** | 10 | **ENTER** | P9 fail only (1.52% to res); Healthcare ETF W-RSI=60.76 just crossed 60 |
| SCHW | Financials | 64.0 | 57.5 | 42.3 [BRS] | 4/10 | 10 | SKIP | P2 fail (Fin W-RSI 54.54), P9 fail (1.01% to res) |
| MA | Financials | 62.6 | 57.2 | 44.1 | 3/10 | 10 | SKIP | P2 fail (Fin W-RSI 54.54), P9 fail (1.98% to res), P8 fail |
| DDOG | Technology | 65.4 | 54.9 | 48.9 [BRS] | 3/10 | 10 | SKIP | P2 fail (Tech W-RSI 56.98), P9 fail (2.04% to res) |
| TXN | Technology | 62.9 | 51.0 | 51.2 [BRS] | 3/10 | 10 | SKIP | P2 fail (Tech W-RSI 56.98), P9 fail (0.23% to res) |
| CAT | Industrials | 63.8 | 48.0 | 47.8 [BRS] | 3/10 | 10 | SKIP | P2 fail (Ind W-RSI 43.0), P9 fail (2.67% to res) |
| EQIX | Real Estate | 67.1 | 49.8 | 45.1 [BRS] | 3/10 | 10 | SKIP | P2 fail (RE W-RSI 41.84), P9 fail (2.51% to res) |
| WMT | Cons. Staples | 63.8 | 41.2 | 45.7 [BRS] | 3/10 | 10 | SKIP | P2 fail (CS W-RSI 44.75), P9 fail (2.50% to res) |
| ASML | Technology | 63.3 | 53.5 | 48.5 [BRS] | 2/10 | 10 | SKIP | P2 fail, P9 fail (6.55%), P8/P10 fail |
| NVDA | Technology | 70.6 | 56.9 | 54.0 [BRS] | 2/10 | 10 | SKIP | P2 fail, P7 fail, P9 fail (1.27%) |
| CSCO | Technology | 78.1 | 54.1 | 46.1 [BRS] | 2/10 | 10 | SKIP | P2 fail, P9 fail (2.46%), P8/P10 fail |
| C | Financials | 68.9 | 52.0 | 40.9 [BRS] | 2/10 | 10 | SKIP | P2 fail, P8/P9/P10 fail |
| VZ | Comm. Svcs | 60.1 | 53.0 | 42.1 | 2/10 | 10 | SKIP | P2 fail, P9 fail (0.11% — at resistance) |
| NBIS | Technology | 68.7 | 55.7 | 52.0 [BRS] | 1/10 | 10 | SKIP | P2 fail, P7 fail, P9 fail (0.40%) |
| ETN | Industrials | 60.7 | 56.4 | 54.8 [BRS] | 1/10 | 10 | SKIP | P2 fail, P7 fail, P9 fail (0.42%) |
| MPWR | Technology | 61.3 | 43.7 | 46.4 [BRS] | 0/10 | 10 | SKIP | All params failed |

### Filtered by Scanner (near resistance < 5%)
11 stocks blocked: DE, MU, TSM, TEM, MRVL, SPY, JPM, QQQ, INTC, META, GOOGL.

---

## Today's Entry Plan

### Trade/Hold Decision: ENTER LLY (1 trade)

**LLY — BULLISH tier — Bracket order**
- Catalyst: BRS confirmed on daily. Healthcare ETF (XLV) W-RSI just crossed 60 — P2 now passing.
- Entry: ~$1,152.46 (Friday close; confirm Monday live price ≤ 3% above = max chase $1,186.84)
- Stop: $1,141.57 (0.94% below entry — tight; confirm trigger candle low Monday morning)
- Target (T1): $1,174.24 (2R, nearest resistance)
- Shares: 4 | Position value: ~$4,610 | Risk: ~$43 (0.94%)
- R/R at T1: 2.0
- Order type: Bracket (stop + T1 atomically)
- Caution: P9 failed (only 1.52% to resistance) — T1 is right at resistance. Minimum threshold entry. If intraday opens weak and trigger low drops significantly, stop may need adjustment.

**Watchlist only (no entry today):** SCHW, MA, DDOG, ASML, CAT, EQIX

---

## Summary
- Gate: POSITIVE
- Tickers scanned: 137
- EB Pullback: 0 candidates
- EB Momentum: 2 scanned, 0 ENTER (Tech sector P2 block)
- Bullish: 16 scanned, 1 ENTER (LLY)
- Filtered by scanner: 11 stocks (near resistance)
- Monday plan: Enter LLY on open IF daily RSI still in Bullish zone, live price ≤ chase threshold, weekly budget available (0/3 used)
