# Trade Log — Last Updated: 2026-10-12 05:50 ET (pre-market run)
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
| MRK | Healthcare | EB_PULLBACK | 5/10 | 10 | 2026-10-12 | P9 (3.23% to res), P10 (1.09x) | 1 pt short |
| ANET | Technology | EB_MOMENTUM | 4/8 | 8 | 2026-10-12 | P9 | |
| META | Comm_Services | BULLISH | 4/10 | 10 | 2026-10-12 | P2 | |
| MPWR | Technology | BULLISH | 4/10 | 10 | 2026-10-12 | P7 (4.4% from support), P9 | |
| PANW | Technology | EB_MOMENTUM | 3/8 | 8 | 2026-10-12 | P8, P9 | |
| CVX | Energy | EB_MOMENTUM | 3/8 | 8 | 2026-10-12 | P8, P9 | |
| C | Financials | BULLISH | 3/10 | 10 | 2026-10-12 | P2 (Fin W-RSI 49.3) | |
| CAT | Industrials | BULLISH | 3/10 | 10 | 2026-10-12 | P2 (Ind 42.5), P9 | |
| CRWD | Technology | EB_MOMENTUM | 2/8 | 8 | 2026-10-12 | P8 (0.73x), P9, P10 | dropped from 8/8 |
| XOM | Energy | EB_MOMENTUM | 2/8 | 8 | 2026-10-12 | P9 (0.36% to res) | |
| ASML | Technology | BULLISH | 2/10 | 10 | 2026-10-12 | P7, P8, P9; earnings Oct 14 | avoid |
| JNJ, ETN, NEM, EQIX, WMT | various | BULLISH | 2/10 | 10 | 2026-10-12 | P2, P8, P9 | |
| ABNB | Consumer_Disc | BULLISH | 0/10 | 10 | 2026-10-12 | P2, P7, P8, P9 | |

**Promoted to Active Trade List (2026-10-12):**
| Ticker | Sector | Tier | Score | Promoted On | Notes |
|--------|--------|------|-------|-------------|-------|
| MRVL | Technology | EB_MOMENTUM | 8/8 | 2026-10-12 | PROMOTE — primary; see RESEARCH-LOG.md |
| AMAT | Technology | BULLISH | 6/10 | 2026-10-12 | PROMOTE |
| AVGO | Technology | BULLISH | 6/10 | 2026-10-12 | PROMOTE |
| LRCX | Technology | BULLISH | 6/10 | 2026-10-12 | PROMOTE (backup; earnings ~Oct 21) |

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
