# Trade Log — Last Updated: 2026-10-09 06:00 ET (pre-market run)
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
| LRCX | Technology | BULLISH | 6/10 | 10 | 2026-10-09 | P9 (0.33% to res) | Marginal ENTER; Tech concentration with MRVL |
| KLAC | Technology | BULLISH | 6/10 | 10 | 2026-10-09 | P9 (2.74% to res) | Marginal ENTER; Tech concentration with MRVL |
| VEEV | Technology | EB_MOMENTUM | 4/8 | 8 | 2026-10-09 | P9 (1.23% to res) | Wait for resistance break |
| ANET | Technology | EB_MOMENTUM | 4/8 | 8 | 2026-10-09 | P9 (0.21% to res) | At resistance |
| ASML | Technology | BULLISH | 4/10 | 10 | 2026-10-09 | P8, P9 (1.04%), P10 (1.40x) | Dropped from 8/10 last run |
| MPWR | Technology | BULLISH | 4/10 | 10 | 2026-10-09 | P7 (3.31%), P9 (1.23%) | |
| DE | Industrials | BULLISH | 4/10 | 10 | 2026-10-09 | P2 (XLI 41.4), P9 | Industrials weak |
| META | Comm_Services | EB_PULLBACK | 4/10 | 10 | 2026-10-09 | P2 (XLC 50.1), P9 (3.56%) | |
| AMD | Technology | EB_MOMENTUM | 3/8 | 8 | 2026-10-09 | P8, P9 (2.89%) | |
| AAPL | Technology | EB_MOMENTUM | 3/8 | 8 | 2026-10-09 | P8, P9 (0.36%) | |
| C | Financials | BULLISH | 3/10 | 10 | 2026-10-09 | P2 (47.0), P8, P9 | |
| CAT | Industrials | BULLISH | 3/10 | 10 | 2026-10-09 | P2, P9, P10 | |

**Promoted to Active Trade List (2026-10-09):**
| Ticker | Sector | Tier | Score | Promoted On | Notes |
|--------|--------|------|-------|-------------|-------|
| MRVL | Technology | EB_MOMENTUM | 8/8 | 2026-10-09 | PROMOTE — primary idea; see RESEARCH-LOG.md |
| MRK | Healthcare | BULLISH | 7/10 | 2026-10-09 | PROMOTE — tight stop caveat |
| COP | Energy | EB_PULLBACK | 6/10 | 2026-10-09 | PROMOTE (conditional) — marginal P9; enter only on pullback/breakout |

---

## Weekly Tracker

Week of: 2026-10-05 (Monday)
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
