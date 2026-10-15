# Trade Log — Last Updated: 2026-10-15 08:30 ET (pre-market run)
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
| CRWD | Technology | EB_PULLBACK | 4/10 | 10 | 2026-10-15 | P2 (Tech W-RSI 58.83), P7 (5.8% from support), P8, P10 | Was 8/8 momentum last month; now pulled back |
| DE | Industrials | BULLISH | 3/10 | 10 | 2026-10-15 | P2 (Ind W-RSI 39.69), P9 (1.37%), P10 | At support (1.0%) |
| NVDA | Technology | BULLISH | 3/10 | 10 | 2026-10-15 | P2 (58.83), P8, P9 (1.52%) | At support gap (0.16%) |
| FCX | Materials | BULLISH | 3/10 | 10 | 2026-10-15 | P2 (45.33), P8, P9 | |
| CEG | Utilities | BULLISH | 3/10 | 10 | 2026-10-15 | P2 (43.06), P9, P10 | |
| META | Communication_Services | EB_PULLBACK | 2/10 | 10 | 2026-10-15 | P2 (47.85), P7, P9 (1.14%) | |
| DDOG | Technology | BULLISH | 2/10 | 10 | 2026-10-15 | P2, P7 (7.4%), P9 (0.58%) | |
| ABNB | Consumer_Discretionary | BULLISH | 2/10 | 10 | 2026-10-15 | P2 (44.47), P8, P9, P10 | |
| ANET | Technology | BULLISH | 2/10 | 10 | 2026-10-15 | P2, P7 (3.96%), P9 | |
| TSM | Technology | BULLISH | 2/10 | 10 | 2026-10-15 | P2, P8, P9, P10 | |
| ETN | Industrials | BULLISH | 2/10 | 10 | 2026-10-15 | P2 (39.69), P8, P9, P10 | |
| MRVL | Technology | BULLISH | 1/10 | 10 | 2026-10-15 | P2, P7 (9.1%), P9, P10 | |
| WMT | Consumer_Staples | BULLISH | 1/10 | 10 | 2026-10-15 | P2 (56.96), P7, P9, P10 | Daily RSI 69 (BRS) — extended |

**Dropped 2026-10-15 (no scanner tier):** ASML, LLY, TXN, SCHW, CSCO, MA, CAT.

**Promoted to Active Trade List (2026-10-15):**
| Ticker | Sector | Tier | Score | Promoted On | Notes |
|--------|--------|------|-------|-------------|-------|
| JNJ | Healthcare | BULLISH | 9/10 | 2026-10-15 | PROMOTE — primary idea; only P10 fails. See RESEARCH-LOG.md |
| EQIX | Real_Estate | BULLISH | 6/10 | 2026-10-15 | PROMOTE (marginal) — P2 sector weak, earnings Oct 28 |

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
