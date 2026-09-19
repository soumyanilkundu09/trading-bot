# Research Log — Last Run: 2026-09-19 14:40 ET (pre-market, weekend prep)
*(Market closed Saturday — data as of Friday 2026-09-18 close. This is a prep run for Monday 2026-09-21 open; market-open MUST re-validate live RSI/price/volume before executing.)*

> This file is **overwritten on every pre-market run**. Git history is the archive.
> Market-open routine validates the "Last Run" date matches today before proceeding.

---

## Account Snapshot
- Account: PA3FLRNK3PUG (PAPER)
- Equity: $100,000.00
- Cash: $100,000.00
- Buying power: $400,000.00
- Open P&L: $0.00 (no open positions)

---

## Global Gate (P1) — POSITIVE ✓

| Indicator | Value | Status |
|-----------|-------|--------|
| SPX Monthly RSI | 72.48 | ✓ > 60 |
| SPX Weekly RSI | 60.87 | ✓ Healthy (> 60) |
| VIX | 14.81 | ✓ < 25 (well inside normal band) |
| DXY 20d change | +1.44% | ✓ < 3% (not spiking) |
| 10Y Yield | 4.998% (20d Δ +0.26pp) | ⚠ Elevated, approaching 5% — not classified as "surging" but watch closely |
| SPX Price | $7,650.50 | — |

**Verdict: POSITIVE. Proceed with scan.**

---

## Event Risk
- No dedicated macro/event-calendar feed is wired into `tools/` — this check is manual/best-effort, not automated. No FOMC meeting is flagged as imminent from available data.
- 10Y yield at 4.998%, approaching the 5% level. If it crosses and holds on the next run, re-evaluate the global gate — this is a standing macro headwind for growth/duration-sensitive names.

---

## Risk Factors
- Technology sector ETF (XLK) Weekly RSI = 56.98 — below the 60 P2 threshold. Most Tech names fail P2 outright (CRWD and AAPL are Tech but scored under the EB Momentum tier, where P2 is only one of 4 weighted params).
- Only Healthcare (XLV, W-RSI 60.76) cleanly passes P2 today; the rest of the sector universe is sub-60.
- 10Y yield near 5% is a macro headwind, particularly for long-duration growth names.
- No open positions, so no below-(-7%) position risk this run.

---

## Scanner Output — 137 tickers scanned, 0 errors

### Sector ETF Snapshot (P2 context, Weekly RSI)

| Sector ETF | Weekly RSI | P2 Status (≥60) |
|------------|-----------|-----------|
| Healthcare (XLV) | 60.76 | ✓ PASS |
| Energy (XLE) | 58.28 | ✗ FAIL |
| Technology (XLK) | 56.98 | ✗ FAIL |
| Financials (XLF) | 54.54 | ✗ FAIL |
| Communication Svcs (XLC) | 47.53 | ✗ FAIL |
| Consumer Staples (XLP) | 44.75 | ✗ FAIL |
| Industrials (XLI) | 43.00 | ✗ FAIL |
| Real Estate (XLRE) | 41.84 | ✗ FAIL |
| Materials (XLB) | 39.32 | ✗ FAIL |
| Consumer Discretionary (XLY) | 37.12 | ✗ FAIL |
| Utilities (XLU) | 30.52 | ✗ FAIL |

### Extremely Bullish Pullback — 0 candidates
*No tickers qualified.*

### Extremely Bullish Momentum — 2 scanned, 1 ENTER

| Ticker | Sector | M-RSI | W-RSI | D-RSI | Score | Max | Decision | Key Notes |
|--------|--------|-------|-------|-------|-------|-----|----------|-----------|
| **CRWD** | Technology | 83.4 | 68.0 | 60.4 | **6/8** | 8 | **ENTER** | P2 fails (Tech W-RSI 56.98) but P8/P9(5.34%)/P10 all pass — clears the 6-pt threshold |
| AAPL | Technology | 73.4 | 64.9 | 63.8 | 1/8 | 8 | SKIP | P2 fail, P9 fail (2.13% to res), P10 fail (red vol 1.24x) |

### Bullish — 16 scanned, 2 ENTER

| Ticker | Sector | M-RSI | W-RSI | D-RSI | Score | Max | Decision | Key Blockers / Notes |
|--------|--------|-------|-------|-------|-------|-----|----------|--------------|
| **LLY** | Healthcare | 74.0 | 54.4 | 47.0 [BRS] | **6/10** | 10 | **ENTER** | Only P9 fails (1.52% to res); P2 passes — Healthcare ETF W-RSI 60.76 |
| **ASML** | Technology | 63.3 | 53.5 | 48.5 [BRS] | **6/10** | 10 | **ENTER\*** | P2, P8, P10 fail; P7 + P9 (6.55%) pass. **P8 = 0.99x (green vol < 20d avg) — fails the Part 4/P8 hard gate in TRADING-STRATEGY.md ("will not execute an order unless p8_entry_ok = true"). Flagging as BLOCKED pending live Monday volume re-check — see Guardrail Alert below.** |
| SCHW | Financials | 64.0 | 57.5 | 42.3 [BRS] | 4/10 | 10 | SKIP | P2 fail (Fin W-RSI 54.54), P9 fail (1.01% to res) |
| MA | Financials | 62.6 | 57.2 | 44.1 | 3/10 | 10 | SKIP | P2, P8, P9 fail (1.98% to res) |
| DDOG | Technology | 65.3 | 54.9 | 48.9 [BRS] | 3/10 | 10 | SKIP | P2, P9 (2.04% to res), P10 fail |
| TXN | Technology | 62.9 | 51.0 | 51.2 [BRS] | 3/10 | 10 | SKIP | P2, P9 (0.23% to res), P10 fail |
| CAT | Industrials | 63.8 | 48.0 | 47.8 [BRS] | 3/10 | 10 | SKIP | P2 (Ind W-RSI 43.0), P8, P9 fail (2.67% to res) |
| EQIX | Real Estate | 67.1 | 49.8 | 45.1 [BRS] | 3/10 | 10 | SKIP | P2 (RE W-RSI 41.84), P8, P9 fail (2.51% to res) |
| WMT | Cons. Staples | 63.8 | 41.2 | 45.7 [BRS] | 3/10 | 10 | SKIP | P2 (CS W-RSI 44.75), P8, P9 fail (2.50% to res) |
| NVDA | Technology | 70.6 | 56.9 | 54.0 [BRS] | 2/10 | 10 | SKIP | P2, P7, P9 fail (1.27% to res) |
| CSCO | Technology | 78.1 | 54.1 | 46.1 [BRS] | 2/10 | 10 | SKIP | P2, P8, P9 (2.46%), P10 fail |
| C | Financials | 68.9 | 52.0 | 40.9 [BRS] | 2/10 | 10 | SKIP | P2, P8, P9, P10 fail |
| VZ | Comm. Svcs | 60.1 | 53.0 | 42.1 | 2/10 | 10 | SKIP | P2, P8, P9 (0.11% — at resistance), P10 fail |
| ETN | Industrials | 60.7 | 56.4 | 54.8 [BRS] | 1/10 | 10 | SKIP | P2, P7, P9, P10 fail |
| NBIS | Technology | 68.7 | 55.7 | 52.0 [BRS] | 1/10 | 10 | SKIP | P2, P7, P9, P10 fail |
| MPWR | Technology | 61.3 | 43.7 | 46.4 [BRS] | 0/10 | 10 | SKIP | All params failed |

### Filtered by Scanner (near resistance < 5%) — 11 stocks
DE (3.11%), MU (2.64%), TSM (2.48%), TEM (4.39%), MRVL (3.97%), SPY (2.33%), JPM (4.84%), QQQ (1.83%), INTC (2.48%), META (2.95%), GOOGL (4.23%).

---

## Guardrail Alert — ASML (8F)

```
╔═══════════════════════════════════════════════════════════╗
║  TRADE FLAGGED — GUARDRAIL CAUTION                        ║
╠═══════════════════════════════════════════════════════════╣
║  Stock       : ASML — NASDAQ                              ║
║  Score       : 6 / 10 (scorer says ENTER)                 ║
║  Blocked by  : Strategy Part 4, P8 footnote (hard gate)   ║
║  Reason      : last-7-green-day volume = 0.99x 20d avg    ║
║                (< 1.0 → P8 fails; P8 is enforced as a      ║
║                hard gate regardless of overall score)      ║
║  Next action : Do NOT execute at market-open unless Monday's║
║                live daily volume confirms p8_entry_ok=true.║
║                Otherwise treat as watchlist-only this week.║
╚═══════════════════════════════════════════════════════════╝
```

---

## Today's Entry Plan

### Trade/Hold Decision: ENTER 2 confirmed (LLY, CRWD) + 1 conditional (ASML, pending P8 re-check)

Weekly budget: 0/3 used (week resets Monday 2026-09-21 regardless). All 3 fit within the 3-trade/week and 5-position caps if all confirm.

**1. LLY — BULLISH tier — Bracket order**
- Catalyst: BRS confirmed on daily. Healthcare ETF (XLV) W-RSI 60.76 passes P2.
- Entry: ~$1,152.46 (Friday close; max chase = $1,186.84, i.e. entry × 1.03)
- Stop: $1,141.57 (0.94% below entry)
- Target T1: $1,174.24 (50% exit) | T2: $1,185.13 (trail remainder)
- Shares: 4 | Position value: ~$4,610 (4.61% of capital) | Risk: ~$44 (0.94%)
- R/R at T1: 2.0
- Order type: Bracket (stop + T1 atomically)
- Caution: P9 fails (only 1.52% to resistance) — T1 sits right at resistance; minimum-threshold entry.

**2. CRWD — EXTREMELY BULLISH MOMENTUM tier — Trailing-stop trade (no fixed target)**
- Catalyst: Monthly 83.4 / Weekly 68.0 / Daily 60.4 — strong momentum continuation. P8, P9 (5.34% to res), P10 all pass.
- Entry: ~$237.61 (confirm Monday open ≤ max chase $244.74)
- Initial stop: $230.48 (3.0% below entry) — trail per 20-SMA / 3-candle-low per trend-following rules (no fixed monetary target; Weekly/Monthly RSI both > 60 → trend-following exit only)
- Shares: 21 | Position value: ~$4,990 (4.99% of capital) | Risk: ~$150
- Caution: P2 fails (Tech sector W-RSI 56.98 < 60) — sector tailwind is not confirmed; this is a single-stock momentum play against a lagging sector.

**3. ASML — BULLISH tier — CONDITIONAL, do not auto-execute**
- Scorer says ENTER (6/10) but **fails the P8 hard gate** (green-day volume 0.99x < 1.0x 20d avg) — see Guardrail Alert above.
- If market-open re-checks Monday's live daily volume and P8 flips to pass → entry: ~$1,679.25, stop $1,631.05, T1 $1,789.29, T2 $1,823.85, shares 2, R/R 2.28.
- If P8 still fails Monday → **do not enter; keep on watchlist**, re-score at next session.

**Watchlist only (no entry, score < 6):** SCHW (4), MA (3), DDOG (3), TXN (3), CAT (3), EQIX (3), WMT (3), NVDA (2), CSCO (2), C (2), VZ (2), ETN (1), NBIS (1), MPWR (0), AAPL (1, EB Momentum).

---

## Summary
- Gate: POSITIVE
- Tickers scanned: 137
- EB Pullback: 0 candidates
- EB Momentum: 2 scanned, 1 ENTER (CRWD)
- Bullish: 16 scanned, 2 ENTER (LLY confirmed, ASML conditional — P8 hard-gate flag)
- Filtered by scanner: 11 stocks (near resistance)
- Monday plan: Market-open must re-validate live RSI/price/volume for all three names before executing; ASML additionally requires P8 (green volume) to flip to pass before any order is placed. Weekly budget 0/3 used entering Monday.
