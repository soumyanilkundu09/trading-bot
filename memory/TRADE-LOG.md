# Trade Log — Last Updated: 2026-09-23 08:30 ET (pre-market run)
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
| MRVL | Technology | EB_PULLBACK | 7/10 | 10 | 2026-09-23 | P8 hard gate (green vol 0.88x — no institutional confirm), P7 (3.81% from support) | Scorer ENTER but BLOCKED by P8 hard gate; needs a confirmed high-volume green day |
| TSM | Technology | EB_MOMENTUM | 6/8 | 8 | 2026-09-23 | P8 hard gate (green vol 0.92x), P10 (red vol 1.17x) | Scorer ENTER but BLOCKED by P8 hard gate |
| TEM | Microcap | EB_PULLBACK | 6/10 | 10 | 2026-09-23 | P2 (sector data unavailable), P7 (22.14% from support — chase) | Scorer ENTER but BLOCKED — chased 22% past the BRS/support zone, exceeds 3% max-chase rule |
| CSCO | Technology | BULLISH | 7/10 | 10 | 2026-09-23 | P7 (14.5% from support), P10 (red vol 1.81x — conviction selling) | Scorer ENTER but BLOCKED — Adverse Low Move disqualifier (heavy volume on recent red candles) |
| GE | Industrials | BULLISH | 6/10 | 10 | 2026-09-23 | P2 (Ind W-RSI 43.86), P8 hard gate (green vol 0.81x), P10 (1.15x) | Scorer ENTER but BLOCKED by P8 hard gate + weak sector |
| CRWD | Technology | EB_MOMENTUM | 4/8 | 8 | 2026-09-23 | P9 (0.28% to res — essentially at resistance), P8 (0.96x) | Score dropped from 8/8 (2026-09-21); still extended, wait for pullback |
| ASML | Technology | BULLISH | 5/10 | 10 | 2026-09-23 | P9 (2.36% to res), P10 (1.34x) | Score dropped from 8/10 (2026-09-21); previously promoted but never entered |
| LLY | Healthcare | BULLISH | 5/10 | 10 | 2026-09-23 | P8 (0.87x), P9 (1.43% to res) | Score dropped from 6/10 (2026-09-19); still marginal |
| DDOG | Technology | BULLISH | 5/10 | 10 | 2026-09-23 | P9 (1.84% to res), P10 (1.07x) | Unchanged from 2026-09-21 |
| TXN | Technology | BULLISH | 5/10 | 10 | 2026-09-23 | P9 (0.7% — at resistance), P10 (1.01x) | Unchanged from 2026-09-21 |
| LRCX | Technology | BULLISH | 5/10 | 10 | 2026-09-23 | P9 (3.0% to res), P10 (1.25x) | New to watchlist |
| CAT | Industrials | BULLISH | 3/10 | 10 | 2026-09-23 | P2 (Ind W-RSI 43.86), P9 (2.71% to res), P10 (1.0x) | Industrials sector still deeply below P2 threshold |
| NVDA | Technology | BULLISH (filtered) | — | — | 2026-09-23 | near_resistance (2.58% to $234.75) | Filtered by scanner's own resistance guard before scoring; wait for pullback |
| EQIX | Real_Estate | BULLISH (filtered) | — | — | 2026-09-23 | near_resistance (4.44% to $1106.76); RE sector weak | Filtered by scanner's own resistance guard before scoring |

*Dropped this run (tier decayed to NONE): SCHW, MA — no longer qualify for any RSI tier.*

**Promoted to Active Trade List (2026-09-23):**
| Ticker | Sector | Tier | Score | Promoted On | Notes |
|-------|--------|------|-------|-------------|-------|
| AMGN | Healthcare | BULLISH | 8/10 | 2026-09-23 | PROMOTE — primary idea; clears P8 volume gate and chase guardrail. See RESEARCH-LOG.md for full trade plan |

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
