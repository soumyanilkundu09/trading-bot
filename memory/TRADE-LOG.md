# Trade Log — Last Updated: 2026-10-26 05:45 ET (pre-market run)
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
| MRK | Healthcare | EB_PULLBACK | 5/10 | 10 | 2026-10-26 | Earnings Oct 29 (event risk) | Revisit after earnings |
| CEG | Utilities | BULLISH | 4/10 | 10 | 2026-10-26 | P2 (XLU W-RSI 46.95) | Daily RSI 40.65 in zone |
| TSM | Technology | BULLISH | 3/10 | 10 | 2026-10-26 | P2 (XLK 52.7) | Daily RSI 41.3 |
| CSCO | Technology | BULLISH | 3/10 | 10 | 2026-10-26 | P2 (XLK 52.7) | Daily RSI 41.8 |
| KO | Consumer_Staples | EB_MOMENTUM | 3/8 | 8 | 2026-10-26 | See RESEARCH-LOG | Staples sector passes P2 |
| HCA | Healthcare | EB_MOMENTUM | 3/8 | 8 | 2026-10-26 | See RESEARCH-LOG | |
| DE | Industrials | BULLISH | 2/10 | 10 | 2026-10-26 | P2 (XLI W-RSI 36.7) | |
| DHR | Healthcare | EB_MOMENTUM | 2/8 | 8 | 2026-10-26 | See RESEARCH-LOG | |
| PANW | Technology | BULLISH | 0/10 | 10 | 2026-10-26 | P2, P7, P9 | |
| DDOG | Technology | BULLISH | 0/10 | 10 | 2026-10-26 | P2, P7, P9 (0.45% to res) | Deteriorated from 5/10 |

Dropped (tier decayed to NONE): CRWD (1/10, no longer a pullback entry), AAPL (1/8), TXN, SCHW, NVDA, MA, CAT, EQIX, ASML, LLY.

**Promoted to Active Trade List (2026-10-26) — conditional on FOMC caution:**
| Ticker | Sector | Tier | Score | Promoted On | Notes |
|--------|--------|------|-------|-------------|-------|
| MRVL | Technology | BULLISH | 8/10 | 2026-10-26 | PROMOTE — see RESEARCH-LOG.md |
| MPC | Energy | EB_MOMENTUM | 7/8 | 2026-10-26 | PROMOTE — see RESEARCH-LOG.md |

---

## Weekly Tracker

Week of: 2026-10-26 (Monday)
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
