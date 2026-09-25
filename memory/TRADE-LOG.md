# Trade Log — Last Updated: 2026-09-25 05:48 ET (pre-market run)
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
| TSM | Technology | EB_MOMENTUM | 7/8 | 8 | 2026-09-25 | P8 green-vol hard gate (0.91x < 1.0) | Score clears ENTER threshold but blocked by P8 gate; re-check next session |
| MRVL | Technology | EB_MOMENTUM | 7/8 | 8 | 2026-09-25 | P8 green-vol hard gate (0.85x) | Score clears ENTER threshold but blocked by P8 gate; re-check next session |
| VEEV | Technology | EB_MOMENTUM | 7/8 | 8 | 2026-09-25 | P8 green-vol hard gate (0.85x) | Score clears ENTER threshold but blocked by P8 gate; re-check next session |
| COP | Energy | BULLISH | 6/10 | 10 | 2026-09-25 | P2 (Energy W-RSI 59.16), P8 hard gate (0.98x), P10 (1.06x) | Score clears ENTER threshold but blocked by P8 gate |
| GE | Industrials | BULLISH | 6/10 | 10 | 2026-09-25 | P2 (Ind W-RSI 41.98), P8 hard gate (0.95x), P10 (1.1x) | Score clears ENTER threshold but blocked by P8 gate |
| LLY | Healthcare | BULLISH | 5/10 | 10 | 2026-09-25 | P8 (0.93x), P9 (0.35% — at resistance) | Was promoted 09/19; decayed back to watchlist, now at resistance |
| LRCX | Technology | BULLISH | 5/10 | 10 | 2026-09-25 | P9 (4.3% to res), P10 (1.01x) | 1 pt short of ENTER |
| ASML | Technology | BULLISH | 4/10 | 10 | 2026-09-25 | P8 (0.98x), P9 (3.81%), P10 (1.35x) | Was promoted 09/21 at 8/10; decayed to 4/10 this run |
| CAT | Industrials | BULLISH | 4/10 | 10 | 2026-09-25 | P2 (Ind W-RSI 41.98), P9 (2.45% to res) | Industrials sector still below P2 threshold |
| MA | Financials | BULLISH | 3/10 | 10 | 2026-09-25 | P2 (Fin W-RSI 47.73), P8 (1.06x), P10 (1.24x) | Financials sector weaker than 09/21 |
| MPWR | Technology | BULLISH | 3/10 | 10 | 2026-09-25 | P7 (2.58% from support), P9 (4.84%), P10 (1.08x) | Not at support this run |
| CSCO | Technology | BULLISH | 3/10 | 10 | 2026-09-25 | P7 (14.91% from support), P9 (4.23%), P10 (1.58x) | Ran well past support zone |
| EQIX | Real_Estate | BULLISH | 3/10 | 10 | 2026-09-25 | P2 (RE W-RSI 38.11), P8 (0.95x), P9 (1.24%) | RE sector still weak |

**Dropped this run (tier decayed to NONE):** CRWD, SCHW, NVDA (no longer in any qualifying tier), DDOG (filtered — 0.33% to resistance).

**Promoted to Active Trade List (2026-09-25):**
| Ticker | Sector | Tier | Score | Promoted On | Notes |
|--------|--------|------|-------|-------------|-------|
| AMGN | Healthcare | BULLISH | 10/10 | 2026-09-25 | PROMOTE — full 5/5 params passed. See RESEARCH-LOG.md |
| TXN | Technology | BULLISH | 6/10 | 2026-09-25 | PROMOTE — was on watchlist since 09/21; P9 fail (1.0% to res) but other 4 params clean. See RESEARCH-LOG.md |

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
