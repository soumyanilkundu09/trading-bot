# Trade Log — Last Updated: 2026-09-28 05:48 ET (pre-market run)
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
| CRWD | Technology | EB_MOMENTUM | 4/8 | 8 | 2026-09-28 | P9 (4.66% to res) | Chase blocker cleared; still short on score |
| MU | Technology | EB_MOMENTUM | 4/8 | 8 | 2026-09-28 | P9 (0.66% — near resistance) | Closest EB_MOMENTUM name to ENTER |
| PLTR | Technology | EB_MOMENTUM | 4/8 | 8 | 2026-09-28 | P9 (2.66% to res) | New to list |
| TSM | Technology | EB_MOMENTUM | 3/8 | 8 | 2026-09-28 | P8 (0.91x), P9 (0.5% — at res) | New to list |
| ANET | Technology | EB_MOMENTUM | 3/8 | 8 | 2026-09-28 | P9 (2.38% to res), P10 (1.16x) | New to list |
| MRVL | Technology | EB_MOMENTUM | 3/8 | 8 | 2026-09-28 | P8 (0.86x), P9 (1.55% to res) | New to list |
| QQQ | ETF | EB_MOMENTUM | 2/8 | 8 | 2026-09-28 | P2 (sector n/a), P9 (0.04% — at res) | Index ETF; P2 not applicable |
| DDOG | Technology | EB_PULLBACK | 3/10 | 10 | 2026-09-28 | P7 (7.02% from support), P9 (1.01% to res), P10 (1.02x) | Tier upgraded from BULLISH to EB_PULLBACK; score fell |
| LLY | Healthcare | BULLISH | 5/10 | 10 | 2026-09-28 | P8 (0.96x), P9 (0.31% — at res) | Fell out of promotion; 1 pt short |
| CSCO | Technology | BULLISH | 5/10 | 10 | 2026-09-28 | P9 (4.49% to res), P10 (1.53x) | 1 pt short of ENTER |
| CAT | Industrials | BULLISH | 4/10 | 10 | 2026-09-28 | P2 (Ind W-RSI 44.07), P9 (0.47% — at res) | Industrials sector still below P2 threshold |
| ASML | Technology | BULLISH | 4/10 | 10 | 2026-09-28 | P8 (0.91x), P9 (0.34% — at res), P10 (1.34x) | Fell out of promotion |
| MA | Financials | BULLISH | 3/10 | 10 | 2026-09-28 | P2 (Fin W-RSI 49.07), P9 (1.55% to res), P10 (1.23x) | Financials sector still weak |
| COP | Energy | BULLISH | 3/10 | 10 | 2026-09-28 | P2 (Energy W-RSI 57.71), P8 (0.99x), P9 (0.78% — at res) | New to list |
| JPM | Financials | BULLISH | 3/10 | 10 | 2026-09-28 | P2 (Fin W-RSI 49.07), P9 (0.13% — at res), P10 (1.38x) | New to list |
| MPWR | Technology | BULLISH | 3/10 | 10 | 2026-09-28 | P7 (4.76% from support), P9 (1.48% to res), P10 (1.05x) | New to list |
| COST | Consumer_Staples | BULLISH | 3/10 | 10 | 2026-09-28 | P2 (Staples W-RSI 42.2), P9 (2.49% to res), P10 (1.3x) | New to list |
| GOOGL | Communication_Services | BULLISH | 2/10 | 10 | 2026-09-28 | P2 (Comm W-RSI 51.58), P8 (0.95x), P9 (0.21% — at res), P10 | New to list |
| C | Financials | BULLISH | 2/10 | 10 | 2026-09-28 | P2 (Fin W-RSI 49.07), P8 (0.95x), P9 (0.74% to res), P10 | New to list |
| EQIX | Real_Estate | BULLISH | 2/10 | 10 | 2026-09-28 | P2 (RE W-RSI 37.69), P8 (0.95x), P9 (3.84% to res), P10 | RE sector still weak |
| WMT | Consumer_Staples | BULLISH | 2/10 | 10 | 2026-09-28 | P2 (Staples W-RSI 42.2), P8 (0.91x), P9 (1.27% to res), P10 | New to list |
| GE | Industrials | BULLISH | 1/10 | 10 | 2026-09-28 | P2 (Ind W-RSI 44.07), P7 (2.65% from support), P9 (3.08% to res), P10 | Multi-parameter fail; consider dropping if score doesn't improve |

**Dropped this run (tier decayed to NONE):**
- NVDA — no longer in any scanner tier
- SCHW — no longer in any scanner tier

**Promoted to Active Trade List (2026-09-28):**
| Ticker | Sector | Tier | Score | Promoted On | Notes |
|--------|--------|------|-------|-------------|-------|
| AMGN | Healthcare | BULLISH | 8/10 | 2026-09-28 | PROMOTE — today's entry idea. Passed P2/P8/P9/P10; missed P7 (not at precision support). See RESEARCH-LOG.md |

ASML and LLY (previously promoted 2026-09-21) fell back to regular Watchlist above — no longer scoring ENTER this run.

---

## Weekly Tracker

Week of: 2026-09-28 (Monday)
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
