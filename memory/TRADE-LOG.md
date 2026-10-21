# Trade Log — Last Updated: 2026-10-21 05:45 ET (pre-market run)
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
| JNJ | Healthcare | BULLISH | 4/10 | 10 | 2026-10-21 | P8 (0.87x), P9 (1.89%), P10 (1.49x) | BRS; red-candle volume heavy |
| NEM | Materials | BULLISH | 4/10 | 10 | 2026-10-21 | P2 (Mat W-RSI 52.2), P9 (1.91%) | BRS; near resistance |
| TSM | Technology | BULLISH | 3/10 | 10 | 2026-10-21 | P2 (54.3), P9 (0.02% — at res), P10 (1.25x) | Wait for breakout/pullback |
| FCX | Materials | BULLISH | 3/10 | 10 | 2026-10-21 | P2, P8 (0.95x), P9 (3.38%) | No BRS |
| NVDA | Technology | BULLISH | 3/10 | 10 | 2026-10-21 | P2 (54.3), P8 (0.99x), P9 (3.9%) |  |
| CSCO | Technology | BULLISH | 3/10 | 10 | 2026-10-21 | P2, P8 (0.78x), P9 (4.51%) | Weak green volume |
| GOOGL | Communication_Services | BULLISH | 3/10 | 10 | 2026-10-21 | P2 (46.6), P8 (0.84x), P9 (1.33%) | At gap support |
| CEG | Utilities | BULLISH | 3/10 | 10 | 2026-10-21 | P2 (43.9), P9 (2.05%), P10 (1.06x) |  |
| DDOG | Technology | BULLISH | 2/10 | 10 | 2026-10-21 | P2, P7 (2.7%), P9 (0.63%) | Fell from 5/10 |
| DE | Industrials | BULLISH | 2/10 | 10 | 2026-10-21 | P2 (39.3), P8, P9 (0.8%), P10 |  |

**Promoted to Active Trade List:** none (2026-10-21). Prior promotions (ASML, LLY) decayed out of scan tiers — dropped. Not watchlisted: CRWD (0/10), EQIX (1/10), QQQ (2/10, ETF), FTNT (1/10), TMO (4/8). SCHW, MA, CAT, TXN no longer in a scan tier — removed.

---

## Weekly Tracker

Week of: 2026-10-19 (Monday)
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
