# Research Log — Last Run: 2026-09-22 05:45 ET (pre-market)

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
| SPX Monthly RSI | 74.43 | ✓ > 60 |
| SPX Weekly RSI | 64.46 | ✓ > 60 (healthy, up from 64.46... trending) |
| VIX | 14.88 | ✓ < 18 (normal band) |
| DXY 20d change | +1.54% | ✓ < 3% (not spiking) |
| 10Y Yield | 4.963% (+25.9bp / 20d) | ⚠ Elevated and still rising; sits just under 5% |
| SPX Price | $7,764.70 | — |

**Verdict: POSITIVE. Proceed with scan.** All hard thresholds pass (Monthly/Weekly RSI, VIX, DXY). Soft warning: 10Y yield continues to grind higher near the 5% level — only one soft bearish signal, so the "any 2 bearish" disqualifier is not triggered.

---

## Event Risk
- **Fed:** Per prior session's research, FOMC last met 2026-09-16 (25bp hike to 3.75–4.00%). Next scheduled FOMC is Oct 27–28, 2026 — **no Fed event within 3 days**.
- **Earnings:** No dedicated earnings-calendar tool is wired into this bot (`tools/` has no calendar source), so earnings dates for today's candidates (MRVL, LRCX, MU, TXN, LLY, MS) are **not independently verified** this run. Market-open should sanity-check each ticker isn't inside a 5-trading-day earnings window before executing (Part 7 disqualifier).
- 10Y yield at 4.963%, still climbing. If it closes above 5% and holds, re-evaluate the gate at the next run.

---

## Risk Factors
- **Scan universe degraded:** Wikipedia S&P 500 fetch failed (HTTP 403) again — scanner fell back to `config/universe.json` only (**137 tickers scanned, not ~503**). Consider fixing the constituent source.
- **Sector concentration:** All 3 ENTER picks today (MRVL, LRCX, MU) are Technology/semiconductor names — correlated exposure to one sub-sector. XLK is genuinely the strongest sector (W-RSI 66.5, M-RSI 74.67), which is why it dominates the candidate list, but a single semi-sector drawdown would hit all three together. Flagging for awareness; not blocked by any hard guardrail.
- No held positions → no -7% stop-outs to flag.
- No urgent overnight thesis breaks identified.

---

## Scanner Output — 137 tickers scanned, 0 errors, gate passed

### Sector ETF Snapshot (P2 context — Weekly RSI)

| Sector ETF | Weekly RSI | Monthly RSI | P2 (>60) |
|------------|-----------|-------------|----------|
| Technology (XLK) | 66.50 | 74.67 | ✓ PASS |
| Healthcare (XLV) | 61.35 | 71.45 | ✓ PASS |
| Energy (XLE) | 58.72 | 63.02 | ✗ |
| Financials (XLF) | 54.61 | 67.70 | ✗ |
| Communication Svcs (XLC) | 54.60 | 62.58 | ✗ |
| Materials (XLB) | 44.57 | 58.98 | ✗ |
| Consumer Disc. (XLY) | 44.54 | 50.74 | ✗ |
| Industrials (XLI) | 43.35 | 63.02 | ✗ |
| Real Estate (XLRE) | 42.30 | 61.98 | ✗ |
| Consumer Staples (XLP) | 41.63 | 62.28 | ✗ |
| Utilities (XLU) | 33.90 | 54.42 | ✗ |

### Extremely Bullish Pullback — 4 candidates

| Ticker | Sector | M-RSI | W-RSI | D-RSI | Score | Max | Decision | Notes |
|--------|--------|-------|-------|-------|-------|-----|----------|-------|
| **MRVL** | Technology | 69.2 | 64.1 | 62.4 [BRS] | **9/10** | 10 | **ENTER** | Only fails P8 (green vol 0.87x); 16.6% room to resistance |
| **MU** | Technology | 72.4 | 63.8 | 61.3 [BRS] | **6/10** | 10 | **ENTER** | Fails P9 (4.37% to res — mildest miss of the 6-scorers) |
| META | Comm. Services | 66.2 | 63.4 | 77.7 [BRS] | 2/10 | 10 | SKIP | P2, P7, P9 all fail; daily RSI extended at 77.7 |
| INTC | Technology | 63.2 | 63.3 | 71.0 [BRS] | 4/10 | 10 | SKIP | P7, P9 fail |

### Extremely Bullish Momentum — 9 candidates

| Ticker | Sector | M-RSI | W-RSI | D-RSI | Score | Max | Decision | Notes |
|--------|--------|-------|-------|-------|-------|-----|----------|-------|
| MPC | Energy | 88.2 | 74.0 | 62.3 | 5/8 | 8 | SKIP | P2 (Energy < 60), P10 |
| PSX | Energy | 77.0 | 73.9 | 61.6 | 5/8 | 8 | SKIP | P2, P10 |
| FTNT | Technology | 87.5 | 72.1 | 62.4 | 3/8 | 8 | SKIP | P8, P9 |
| CRWD | Technology | 84.3 | 70.2 | 64.6 [BRS] | 4/8 | 8 | SKIP | P9 (near resistance); scored 8/8 yesterday but pulled back |
| MRK | Healthcare | 77.7 | 66.7 | 59.9 | 3/8 | 8 | SKIP | P8, P9 |
| ANET | Technology | 73.2 | 65.5 | 60.0 | 2/8 | 8 | SKIP | P8, P9, P10 |
| TSM | Technology | 71.4 | 65.4 | 61.7 [BRS] | 2/8 | 8 | SKIP | P8, P9, P10 |
| ABBV | Healthcare | 75.2 | 62.9 | 59.6 | 3/8 | 8 | SKIP | P9, P10 |
| PLTR | Technology | 65.5 | 61.0 | 61.2 | 3/8 | 8 | SKIP | P8, P9 |

### Bullish — 18 candidates

| Ticker | Sector | M-RSI | W-RSI | D-RSI | Score | Max | Decision | Notes |
|--------|--------|-------|-------|-------|-------|-----|----------|-------|
| SCHW | Financials | 65.8 | 59.8 | 48.6 [BRS] | 4/10 | 10 | SKIP | P2 (Fin 54.61), P9 (1.01%) |
| KO | Cons. Staples | 76.0 | 59.7 | 44.7 | 3/10 | 10 | SKIP | P2, P9, P10 |
| ETN | Industrials | 62.0 | 59.1 | 58.3 [BRS] | 1/10 | 10 | SKIP | P2, P7, P9, P10 |
| DDOG | Technology | 68.7 | 58.5 | 57.0 [BRS] | 4/10 | 10 | SKIP | P8, P9, P10 |
| NBIS | Technology | 69.6 | 57.3 | 55.4 [BRS] | 3/10 | 10 | SKIP | P7, P9, P10 |
| CSCO | Technology | 79.6 | 56.1 | 50.9 [BRS] | 5/10 | 10 | SKIP | P9 (2.46%... at 111.46 basis), P10 |
| COP | Energy | 61.7 | 55.8 | 43.0 | 0/10 | 10 | SKIP | All 5 params fail |
| **LLY** | Healthcare | 74.6 | 55.5 | 50.9 [BRS] | **6/10** | 10 | **QUALIFIED (budget-blocked)** | Fails P9 — only 0.45% to resistance, essentially at the ceiling |
| ASML | Technology | 64.3 | 55.3 | 51.9 [BRS] | 3/10 | 10 | SKIP | P7, P9, P10 — score collapsed from yesterday's 8/10 |
| XOM | Energy | 62.9 | 55.1 | 44.5 | 2/10 | 10 | SKIP | P2, P8, P9, P10 |
| AMGN | Healthcare | 60.7 | 54.6 | 45.1 [BRS] | 4/10 | 10 | SKIP | P7, P9 |
| **TXN** | Technology | 63.5 | 52.4 | 54.5 [BRS] | **6/10** | 10 | **QUALIFIED (budget-blocked)** | Fails P9 — 0.94% to resistance |
| **LRCX** | Technology | 61.1 | 52.3 | 51.3 [BRS] | **7/10** | 10 | **ENTER** | Fails P7 (5.72% from support) and P10 (red vol 1.31x) |
| BRK.B | Financials | 67.3 | 52.3 | 43.9 | 3/10 | 10 | SKIP | P2, P9, P10 |
| **MS** | Financials | 73.8 | 52.2 | 42.1 [BRS] | **6/10** | 10 | **QUALIFIED (budget-blocked)** | Fails P2 (sector weak, Fin W-RSI 54.61), P8, P10 — weakest quality of the 6/10s |
| CAT | Industrials | 64.1 | 49.3 | 50.2 [BRS] | 3/10 | 10 | SKIP | P2 (Ind 43.35), P8, P9 |
| MPWR | Technology | 63.7 | 48.0 | 53.8 [BRS] | 5/10 | 10 | SKIP | P9 (0.9%... near res), P10 |
| WMT | Cons. Staples | 64.2 | 42.3 | 48.4 [BRS] | 3/10 | 10 | SKIP | P2, P8, P9 |

### Filtered by Scanner (9 stocks — passed RSI tiers but blocked by entry filters)
| Ticker | Reason | Re-scored anyway? |
|--------|--------|-------------------|
| SPY | near_resistance (0.76%) | ETF — not a scan target |
| DE | near_resistance (2.97%) | — |
| QQQ | near_resistance (0.95%) | ETF — not a scan target |
| TEM | near_resistance (4.77%) | — |
| NVDA | near_resistance (3.28%) | Yes — 4/10, fails P7 (4.83%), P9 (1.39%) |
| C | near_resistance (4.53%) | — |
| GOOGL | near_resistance (1.25%) | — |
| EQIX | near_resistance (4.65%) | Yes — 3/10, fails P2 (RE 42.30), P8, P9 (0.22% — at resistance) |
| EOG | gap_down_5d (2.6% on 2026-09-16) | — |

---

## Today's Entry Plan

### Trade/Hold Decision: ENTER 3 candidate(s) — MRVL, LRCX, MU
**Weekly budget:** 0/3 used → all 3 slots allocated today. **No orders placed by this routine** — market-open executes. Prices below are the scanner's basis (yesterday's close); market-open must re-validate against live quotes (chase ≤ +3%, re-run scorer) before sending orders.

Six tickers scored ≥6 (ENTER-qualified) today: MRVL(9), LRCX(7), MU/TXN/LLY/MS all tied at 6. With only 3 weekly slots available, the 3 highest-quality setups were selected — MRVL and LRCX on raw score, and MU over the other three 6/10s because it has by far the mildest parameter miss (P9 at 4.37% vs. TXN 0.94%, LLY 0.45%, and MS which additionally fails the sector-strength gate P2). See "Blocked by Weekly Budget" below for TXN/LLY/MS.

#### 1. MRVL — Extremely Bullish Pullback — Score 9/10 — Bracket order
- **Thesis:** Cleanest setup of the day. Monthly RSI 69.2, Weekly RSI 64.1 (both well above 60), Daily RSI 62.4 confirmed via Bullish Range Shift. Technology sector strongly passes P2 (XLK W-RSI 66.5). 16.6% of room to nearest resistance — no proximity risk. Only miss is P8 (last 7 green daily candles average 0.87x the 20-day volume — sustained buying not yet confirmed on volume).
- **Entry:** ~$257.31 (scan basis)
- **Stop:** $251.04 (−2.44%, low of trigger candle)
- **T1:** $299.90 (partial exit 50%) | **T2:** $276.12 (trail remaining 50%)
- **Shares:** 19 | Value ≈ $4,889 (4.89% of equity) | Risk ≈ $119 (0.12% of capital) | R/R at T1: 6.79
- **Order type:** Bracket (market entry, day; stop + T1 atomic)

#### 2. LRCX — Bullish — Score 7/10 — Bracket order
- **Thesis:** Monthly 61.1, Weekly 52.3, Daily 51.3 via BRS. Sector strong (P2 pass, same Tech tailwind as MRVL). Only 5.97% to resistance so real room exists (P9 passes).
- **Caveats:** Misses P7 — price is 5.72% from the nearest support/CIP/gap, not a tight entry-zone touch. Misses P10 — last 4 red candles averaged 1.31x the 20-day volume, i.e. some real selling pressure on the pullback (a mild Adverse-Low-Move violation). This is more of a "strength continuation" entry than a textbook pullback-to-support entry — size and manage accordingly.
- **Entry:** ~$302.15 (scan basis)
- **Stop:** $293.09 (−3.00%)
- **T1:** $320.27 (partial exit 50%) | **T2:** $329.33 (trail remaining 50%)
- **Shares:** 16 | Value ≈ $4,834 (4.83% of equity) | Risk ≈ $145 (0.14% of capital) | R/R at T1: 2.0
- **Order type:** Bracket

#### 3. MU — Extremely Bullish Pullback — Score 6/10 — Bracket order
- **Thesis:** Monthly 72.4, Weekly 63.8, Daily 61.3 via BRS — same strong Tech/semis tailwind as MRVL. Price sits in a gap-support zone (P7 pass), last 7 green days average 1.17x volume (P8 pass), red-candle volume on the pullback is low at 0.89x (P10 pass, Adverse Low Move confirmed).
- **Caveats:** Misses P9 — only 4.37% to resistance, the shallowest cushion of the three entries today.
- **Entry:** ~$1,043.51 (scan basis)
- **Stop:** $1,012.20 (−3.00%)
- **T1:** $1,106.13 (partial exit 50%) | **T2:** $1,137.44 (trail remaining 50%)
- **Shares:** 4 | Value ≈ $4,174 (4.17% of equity) | Risk ≈ $125 (0.13% of capital) | R/R at T1: 2.0
- **Order type:** Bracket

**Combined:** 3 positions, $13,897 deployed (13.9% of equity), $389 total risk (0.39% of capital) — well within all Guardrail 8B caps. All three are Technology/semiconductor names (see Risk Factors — sector concentration).

---

### Blocked by Weekly Budget (Guardrail 8E) — score ≥ 6 but no slots remaining

```
╔═══════════════════════════════════════════════════════════╗
║  TRADE BLOCKED — GUARDRAIL VIOLATION                      ║
╠═══════════════════════════════════════════════════════════╣
║  Stock       : TXN — NASDAQ                                ║
║  Score       : 6/10 (setup qualified on score)              ║
║  Blocked by  : 8E — Weekly Trade Budget (3/3 allocated)     ║
║  Reason      : Ranked below MRVL/LRCX/MU; fails P9 at 0.94% ║
║                to resistance (tighter than MU's 4.37%)      ║
║  Next action : Watchlisted; re-evaluate next Monday, or     ║
║                sooner if a 09-22 entry exits early           ║
╚═══════════════════════════════════════════════════════════╝

╔═══════════════════════════════════════════════════════════╗
║  TRADE BLOCKED — GUARDRAIL VIOLATION                      ║
╠═══════════════════════════════════════════════════════════╣
║  Stock       : LLY — NYSE                                   ║
║  Score       : 6/10 (setup qualified on score)               ║
║  Blocked by  : 8E — Weekly Trade Budget (3/3 allocated)      ║
║  Reason      : Fails P9 at 0.45% to resistance — essentially ║
║                at the ceiling; weakest R:R of the six        ║
║  Next action : Watchlisted; re-evaluate next Monday, or      ║
║                sooner if a 09-22 entry exits early            ║
╚═══════════════════════════════════════════════════════════╝

╔═══════════════════════════════════════════════════════════╗
║  TRADE BLOCKED — GUARDRAIL VIOLATION                      ║
╠═══════════════════════════════════════════════════════════╣
║  Stock       : MS — NYSE                                     ║
║  Score       : 6/10 (setup qualified on score)                ║
║  Blocked by  : 8E — Weekly Trade Budget (3/3 allocated)       ║
║  Reason      : Also fails P2 — Financials sector W-RSI 54.61  ║
║                is below the 60 strength gate ("strong stock   ║
║                in a weak sector"); plus P8, P10 fail           ║
║  Next action : Watchlisted; lowest priority of the six —      ║
║                re-evaluate only if Financials (XLF) reclaims   ║
║                W-RSI > 60                                      ║
╚═══════════════════════════════════════════════════════════╝
```

### Watchlist-only (score < 6, no action)
CSCO (5), MPWR (5), CRWD (4/8), NVDA (4), SCHW (4), DDOG (4), AMGN (4), KO (3), NBIS (3), ASML (3), BRK.B (3), CAT (3), WMT (3), EQIX (3) — see `memory/TRADE-LOG.md` Watchlist for full blocker detail.
Not carried to watchlist (score 0–2, multiple hard failures): COP (0), ETN (1), XOM (2), META (2), ANET (2), TSM (2).
Dropped from watchlist entirely (tier decayed to NONE — no longer qualifies for any tier): MA.

---

## Summary
- Gate: POSITIVE (SPX M/W 74.4/64.5, VIX 14.9; 10Y 4.96% and still rising = soft caution)
- Tickers scanned: 137 (degraded — S&P 500 constituent fetch failed) | Errors: 0
- EB Pullback: 4 scanned, 2 ENTER-qualified (MRVL 9/10, MU 6/10) | EB Momentum: 9 scanned, 0 ENTER-qualified | Bullish: 18 scanned, 4 ENTER-qualified (LRCX 7/10, TXN/LLY/MS 6/10)
- Filtered by scanner: 9 (8 near-resistance, 1 gap-down)
- Plan: ENTER 3 — MRVL, LRCX, MU (all Technology). TXN, LLY, MS qualified but budget-blocked (8E). Weekly budget after execution: 3/3.
