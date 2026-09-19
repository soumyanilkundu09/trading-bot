# Trade Log — Last Updated: 2026-09-19 (pre-market run)
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
| SCHW | Financials | BULLISH | 4/10 | 10 | 2026-09-19 | P2 (Fin W-RSI 54.54 < 60), P9 (1.01% to res) | Closest Financials pick; need sector ETF recovery |
| MA | Financials | BULLISH | 3/10 | 10 | 2026-09-19 | P2 (Fin W-RSI 54.54), P8 (green vol 0.95x), P9 (1.98% to res) | At support/gap zone (P7 pass); watch for sector recovery |
| DDOG | Technology | BULLISH | 3/10 | 10 | 2026-09-19 | P2 (Tech W-RSI 56.98), P9 (2.04% to res), P10 (red vol 1.08x) | Needs Tech sector ETF to cross 60 |
| ASML | Technology | BULLISH | 2/10 | 10 | 2026-09-19 | P2 (Tech W-RSI 56.98), P8, P9 (6.55% — nearest to P9 pass) | Best P9 distance in Tech universe — first to pass if Tech ETF recovers |
| CAT | Industrials | BULLISH | 3/10 | 10 | 2026-09-19 | P2 (Ind W-RSI 43.0), P8, P9 (2.67% to res) | Industrials sector deeply below P2 threshold |
| EQIX | Real_Estate | BULLISH | 3/10 | 10 | 2026-09-19 | P2 (RE W-RSI 41.84), P8, P9 (2.51% to res) | Data center play; RE sector weak |

**Promoted to Active Trade List (2026-09-19):**
| Ticker | Sector | Tier | Score | Promoted On | Notes |
|--------|--------|------|-------|-------------|-------|
| LLY | Healthcare | BULLISH | 6/10 | 2026-09-19 | ENTER signal — see Monday market-open plan in RESEARCH-LOG.md |

---

## Weekly Tracker

Week of: 2026-09-15 (Monday)
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
