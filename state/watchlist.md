# Watchlist — Active Monitoring

> Stocks in a valid RSI tier but scoring < 6 — not ready to enter yet.
> Re-scored each pre-market and daily-summary run.
> Promote to Active Trade List when tier ≠ NONE AND scorer returns ENTER (score ≥ 6).

**Last updated:** 2026-09-19 (pre-market run)

| Ticker | Sector | Tier | Score | Max | Last Scored | Key Blockers | Notes |
|--------|--------|------|-------|-----|-------------|--------------|-------|
| SCHW | Financials | BULLISH | 4/10 | 10 | 2026-09-19 | P2 (Fin W-RSI 54.54 < 60), P9 (1.01% to res) | Closest Financials pick; need sector ETF recovery |
| MA | Financials | BULLISH | 3/10 | 10 | 2026-09-19 | P2 (Fin W-RSI 54.54), P8 (green vol 0.95x), P9 (1.98% to res) | At support/gap zone (P7 pass); watch for sector recovery |
| DDOG | Technology | BULLISH | 3/10 | 10 | 2026-09-19 | P2 (Tech W-RSI 56.98), P9 (2.04% to res), P10 (red vol 1.08x) | Needs Tech sector ETF to cross 60 |
| ASML | Technology | BULLISH | 2/10 | 10 | 2026-09-19 | P2 (Tech W-RSI 56.98), P8, P9 (6.55% — nearest to P9 pass among Tech) | Best P9 distance in Tech universe — first to pass if Tech ETF recovers |
| CAT | Industrials | BULLISH | 3/10 | 10 | 2026-09-19 | P2 (Ind W-RSI 43.0), P8, P9 (2.67% to res) | Industrials sector deeply below P2 threshold |
| EQIX | Real_Estate | BULLISH | 3/10 | 10 | 2026-09-19 | P2 (RE W-RSI 41.84), P8, P9 (2.51% to res) | Data center play; RE sector weak |

---

### Promoted to Active Trade List (this run)
| Ticker | Sector | Tier | Score | Promoted On | Notes |
|--------|--------|------|-------|-------------|-------|
| LLY | Healthcare | BULLISH | 6/10 | 2026-09-19 | ENTER signal — see Monday market-open plan in research log |

---

### Dropped This Run (tier decayed to NONE or 0 score)
| Ticker | Last Score | Tier | Reason |
|--------|-----------|------|--------|
| PANW | — | — | Not in universe scan output (not in universe.json or failed RSI) |
| MPWR | 0/10 | BULLISH | All 5 params failed — no signal at all; dropped pending recovery |

---

### Notes
- Only Healthcare sector ETF passes P2 (W-RSI 60.76) today. All Tech/Fin/Ind/RE candidates blocked at P2.
- ASML is the highest P9-distance stock in Technology (6.55%) — it will be the first to unlock if Tech ETF crosses 60.
- CRWD and AAPL qualified as EB Momentum at scanner level but scored 2/8 and 1/8 (P2 + P9 failing); not added to watchlist as they are Momentum tier with very few remaining scoring levers.
