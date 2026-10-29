# Trade Log — Last Updated: 2026-10-29 05:45 ET (pre-market run)
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
| MRVL | Technology | BULLISH | 7/10 | 10 | 2026-10-29 | P2 (Tech W-RSI 58.18), P8 (green vol 0.81x) | PROMOTE — see RESEARCH-LOG.md |
| INTC | Technology | BULLISH | 5/10 | 10 | 2026-10-29 | P2, P7 (6.15% from support), P10 | 1 pt short |
| GOOGL | Communication_Services | BULLISH | 5/10 | 10 | 2026-10-29 | P2 (W-RSI 35.26), P7, P10 | Sector weak |
| CRWD | Technology | EB_PULLBACK | 4/10 | 10 | 2026-10-29 | P2, P7 (11.9%), P8, P10 | Extended |
| CEG | Utilities | BULLISH | 4/10 | 10 | 2026-10-29 | P2 (46.67), P9 (2.3%) | |
| MRK | Healthcare | BULLISH | 4/10 | 10 | 2026-10-29 | P8, P9 (4.96%), P10 (1.44x) | |
| MS | Financials | BULLISH | 4/10 | 10 | 2026-10-29 | P2 (55.37), P9 (0.88%) | |
| TMO | Healthcare | EB_MOMENTUM | 3/10 | 10 | 2026-10-29 | P9 (0.11% to res), P10 | At resistance |
| EQIX | Real_Estate | BULLISH | 3/10 | 10 | 2026-10-29 | P2, P9, P10 | |
| DE | Industrials | BULLISH | 3/10 | 10 | 2026-10-29 | P2, P8, P9 | |
| ANET | Technology | BULLISH | 3/10 | 10 | 2026-10-29 | P2, P9 (0.41%), P10 | |
| ETN | Industrials | BULLISH | 3/10 | 10 | 2026-10-29 | P2, P9, P10 (1.65x) | |
| CSCO | Technology | BULLISH | 3/10 | 10 | 2026-10-29 | P2, P8, P9 | |
| NEM | Materials | BULLISH | 3/10 | 10 | 2026-10-29 | P2, P9 (4.5%), P10 | |
| NVDA | Technology | BULLISH | 3/10 | 10 | 2026-10-29 | P2, P9 (3.18%), P10 | |

Dropped (score ≤ 2 or tier NONE): ASML, LLY, SCHW, MA, CAT, DDOG, TXN, PANW, AMD, V, DHR, XLV, IGV, FCX, C, TSM, ABNB, MU, QQQ.

**Promoted to Active Trade List (2026-10-29):**
| Ticker | Sector | Tier | Score | Promoted On | Notes |
|--------|--------|------|-------|-------------|-------|
| MRVL | Technology | BULLISH | 7/10 | 2026-10-29 | ENTER candidate; re-score live at market-open |

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
