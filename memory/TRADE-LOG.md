# Trade Log — Last Updated: 2026-10-14 08:30 ET (pre-market run)
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
| DDOG | Technology | EB_PULLBACK | 4/10 | 10 | 2026-10-14 | P7 (4.39% from support), P9 (2.31% to res) | Wait for pullback to support |
| DE | Industrials | BULLISH | 3/10 | 10 | 2026-10-14 | P2 (Ind W-RSI 41.7), P9 (1.54%), P10 | Industrials sector weak |
| ETN | Industrials | BULLISH | 3/10 | 10 | 2026-10-14 | P2, P8, P9 (1.39% to res) | Industrials sector weak |
| NEM | Materials | BULLISH | 3/10 | 10 | 2026-10-14 | P2 (45.5), P8, P9 | Materials sector weak |
| LRCX | Technology | BULLISH | 3/10 | 10 | 2026-10-14 | P7 (5.5% from support), P9 (0.19% to res) | At resistance |
| AAPL | Technology | EB_MOMENTUM | 3/8 | 8 | 2026-10-14 | P9 (0.1% to res), P10 | Wait for resistance break |

**Promoted to Active Trade List (2026-10-14):**
| Ticker | Sector | Tier | Score | Promoted On | Notes |
|--------|--------|------|-------|-------------|-------|
| NBIS | Technology | BULLISH | 9/10 | 2026-10-14 | PROMOTE — ENTER; tight 0.52% stop, see RESEARCH-LOG.md |
| MRK | Healthcare | BULLISH | 7/10 | 2026-10-14 | PROMOTE — ENTER; P2/P10 fail |

_Dropped 2026-10-14 (tier decayed / no longer in scan or score below threshold):_ CRWD, TXN, SCHW, NVDA, CSCO, MA, CAT, EQIX, ASML, LLY, ABNB.

---

## Weekly Tracker

Week of: 2026-10-12 (Monday)
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
