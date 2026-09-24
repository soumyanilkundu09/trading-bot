# Trade Log — Last Updated: 2026-09-24 08:30 ET (pre-market run)
**Trading mode:** PAPER

> Source of truth for all trade state. Updated by every agent run.
> Sections: Open Positions → Watchlist → Weekly Tracker → Closed Trades.
> Git history is the audit trail — no date-stamped log files.

---

## Open Positions

| Ticker | Sector | Tier | Entry Date | Entry $ | Shares | Stop $ | T1 $ | T2 $ | Status | Thesis |
|--------|--------|------|-----------|---------|--------|--------|------|------|--------|--------|
| _(none yet)_ | | | | | | | | | | |

---

## Watchlist

> Stocks in a valid RSI tier but score < 6. Re-scored each pre-market and daily-summary run.
> Promote when tier ≠ NONE AND scorer returns ENTER (score ≥ 6).

| Ticker | Sector | Tier | Score | Max | Last Scored | Key Blockers | Notes |
|--------|--------|------|-------|-----|-------------|--------------|-------|
| TEM | Microcap | EB_PULLBACK | 5/10 | 10 | 2026-09-24 | P2 (sector data unavailable), P7 (21.59% from support), P10 (1.03x) | No sector ETF mapping for Microcap — P2 will always fail |
| ETN | Industrials | BULLISH | 5/10 | 10 | 2026-09-24 | P2 (Ind W-RSI 43.57), P7 (dist_support unclear), P10 (—) | New to watchlist |
| LRCX | Technology | BULLISH | 5/10 | 10 | 2026-09-24 | P9, P10 | New to watchlist |
| LLY | Healthcare | BULLISH | 5/10 | 10 | 2026-09-24 | P8, P9 | Down from 6/10 (2026-09-21) — no longer ENTER-qualified |
| PANW | Technology | EB_MOMENTUM | 4/8 | 8 | 2026-09-24 | P9 | New to watchlist |
| ASML | Technology | BULLISH | 4/10 | 10 | 2026-09-24 | P8, P9, P10 | Down from 8/10 (2026-09-21) — decayed out of promoted list |
| CAT | Industrials | BULLISH | 4/10 | 10 | 2026-09-24 | P2 (Ind W-RSI 43.57), P9 | Up from 3/10 (2026-09-21) |
| MA | Financials | BULLISH | 3/10 | 10 | 2026-09-24 | P2 (Fin W-RSI 47.77), P9, P10 | Unchanged (2026-09-21); Financials sector still weak |
| MPWR | Technology | BULLISH | 3/10 | 10 | 2026-09-24 | P7, P9, P10 | New to watchlist |
| V | Financials | BULLISH | 3/10 | 10 | 2026-09-24 | P2 (Fin W-RSI 47.77), P9, P10 | New to watchlist |
| WMT | Consumer_Staples | BULLISH | 3/10 | 10 | 2026-09-24 | P2 (Staples W-RSI 43.43), P8, P9 | New to watchlist |
| TXN | Technology | BULLISH | 3/10 | 10 | 2026-09-24 | P7, P9, P10 | Down from 5/10 (2026-09-21) |
| EQIX | Real_Estate | BULLISH | 3/10 | 10 | 2026-09-24 | P2 (RE W-RSI n/a), P8, P9 | Unchanged (2026-09-21) |
| FTNT | Technology | EB_MOMENTUM | 3/8 | 8 | 2026-09-24 | P8, P9 | New to watchlist |
| AAPL | Technology | EB_MOMENTUM | 3/8 | 8 | 2026-09-24 | P8, P9 | New to watchlist |
| TSM | Technology | EB_MOMENTUM | 3/8 | 8 | 2026-09-24 | P8, P9 | New to watchlist |
| VEEV | Technology | EB_MOMENTUM | 3/8 | 8 | 2026-09-24 | P8, P9 | New to watchlist |
| ABBV | Healthcare | EB_MOMENTUM | 2/8 | 8 | 2026-09-24 | P8, P9, P10 | New to watchlist |
| COP | Energy | BULLISH | 2/10 | 10 | 2026-09-24 | P2, P8, P9, P10 | New to watchlist |
| C | Financials | BULLISH | 2/10 | 10 | 2026-09-24 | P2, P8, P9, P10 | New to watchlist |
| EOG | Energy | BULLISH | 2/10 | 10 | 2026-09-24 | P2, P8, P9, P10 | New to watchlist |
| NBIS | Microcap | BULLISH | 1/10 | 10 | 2026-09-24 | P2, P7, P9, P10 | No sector ETF mapping for Microcap |

**Dropped this run (tier decayed to NONE, removed):** CRWD, DDOG, SCHW, NVDA — no longer in a qualifying RSI tier per today's scan (DDOG and NVDA were filtered pre-tier on near-resistance; CRWD and SCHW did not clear the RSI filters at all).

**Promoted to Active Trade List (2026-09-24):**
| Ticker | Sector | Tier | Score | Promoted On | Notes |
|--------|--------|------|-------|-------------|-------|
| AMGN | Healthcare | BULLISH | 10/10 | 2026-09-24 | PROMOTE — all 5 params pass, strongest setup. See RESEARCH-LOG.md |
| CSCO | Technology | BULLISH | 7/10 | 2026-09-24 | PROMOTE — sector very strong, RSI at classic 40 inflection. See RESEARCH-LOG.md |
| GE | Industrials | BULLISH | 6/10 | 2026-09-24 | PROMOTE — marginal, right at threshold; extra scrutiny at market-open. See RESEARCH-LOG.md |

---

## Weekly Tracker

Week of: 2026-09-21 (Monday)
Entries this week: 0 / 3
Open positions: 0 / 5
Sector loss tracker: (all clear)

### Entries This Week
| Date | Ticker | Tier | Score | Shares | Entry $ |
|------|--------|------|-------|--------|---------|
| _(none yet)_ | | | | | |

---

## Closed Trades

| # | Open Date | Close Date | Ticker | Sector | Tier | Entry $ | Exit $ | Shares | P&L $ | P&L % | R-Multiple | Exit Reason | Mode |
|---|-----------|-----------|--------|--------|------|---------|--------|--------|-------|-------|-----------|-------------|------|
| _(none yet)_ | | | | | | | | | | | | | |

---

### Rules
- Max 5 open positions (Guardrail 8B). Max 3 new entries per week (Guardrail 8E).
- Each position max 5% of equity, risk max 2% of capital per trade.
- **Tier column is mandatory** — midday scan uses it to pick the correct exit rule.
- EB_PULLBACK / BULLISH: T1 hit → close 50%, trail stop to prior swing low.
- EB_MOMENTUM: no fixed T1. Trail stop using 3-bar daily candle low. Exit on trailing stop or BRS only.
- Exit immediately if daily RSI < 40 (Bearish Range Shift) or stop hit (all tiers).
- 2 consecutive losses in a sector → pause that sector until weekly review re-enables it.
