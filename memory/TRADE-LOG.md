# Trade Log — Last Updated: 2026-09-21 05:41 ET (pre-market run)
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
| DDOG | Technology | BULLISH | 5/10 | 10 | 2026-09-21 | P9 (2.04% to res), P10 (red vol 1.08x) | Tech sector now strong (XLK W-RSI 63.37); close to promotion |
| KEYS | Technology | BULLISH | 5/10 | 10 | 2026-09-21 | P8 (green vol 0.98x), P9 (1.18% to res) | Near-miss on P9; watch for pullback |
| ADI | Technology | BULLISH | 5/10 | 10 | 2026-09-21 | P8 (green vol 0.98x), P9 (0.22% to res) | Right at resistance — needs breakout or deeper pullback |
| APH | Technology | BULLISH | 5/10 | 10 | 2026-09-21 | P8 (green vol 0.94x), P9 (1.87% to res) | Tech sector tailwind; volume lagging |
| TXN | Technology | BULLISH | 5/10 | 10 | 2026-09-21 | P9 (0.23% to res), P10 (red vol 1.01x) | Right at resistance |
| BE | Industrials | BULLISH | 5/10 | 10 | 2026-09-21 | P2 (Ind W-RSI 43.0), P7 (3.45% to support), P10 (red vol 1.12x) | Industrials sector weak; strong daily RSI (57.5) offsets |
| SCHW | Financials | BULLISH | 4/10 | 10 | 2026-09-21 | P2 (Fin W-RSI 54.54), P9 (1.01% to res) | Closest Financials pick; need sector ETF recovery |
| GL | Financials | BULLISH | 4/10 | 10 | 2026-09-21 | P2 (Fin W-RSI 54.54), P9 (0.72% to res) | Right at resistance |
| NVDA | Technology | BULLISH | 4/10 | 10 | 2026-09-21 | P7 (2.57% to support), P9 (1.27% to res) | Mega-cap; tight range near resistance |
| MA | Financials | BULLISH | 3/10 | 10 | 2026-09-21 | P2 (Fin W-RSI 54.54), P8 (vol 0.95x), P9 (1.98% to res) | At support/gap zone (P7 pass); watch for sector recovery |
| CAT | Industrials | BULLISH | 3/10 | 10 | 2026-09-21 | P2 (Ind W-RSI 43.0), P8 (vol 0.95x), P9 (2.67% to res) | Industrials sector deeply below P2 threshold |
| EQIX | Real_Estate | BULLISH | 3/10 | 10 | 2026-09-21 | P2 (RE W-RSI 41.84), P8 (vol 0.86x), P9 (2.51% to res) | Data center play; RE sector weak |

**Promoted to Active Trade List (2026-09-21) — entering today (weekly budget 3/3):**
| Ticker | Sector | Tier | Score | Promoted On | Notes |
|--------|--------|------|-------|-------------|-------|
| LH | Healthcare | EXTREMELY_BULLISH_PULLBACK | 9/10 | 2026-09-21 | ENTER — see today's plan in RESEARCH-LOG.md |
| FLEX | Technology | BULLISH | 9/10 | 2026-09-21 | ENTER — see today's plan in RESEARCH-LOG.md |
| JBL | Technology | BULLISH | 9/10 | 2026-09-21 | ENTER — see today's plan in RESEARCH-LOG.md |

**PROMOTE — score ≥6 but blocked by weekly budget (8E), carry to next available window:**
| Ticker | Sector | Tier | Score | Last Scored | Notes |
|--------|--------|------|-------|-------------|-------|
| CRWD | Technology | EXTREMELY_BULLISH_MOMENTUM | 8/8 | 2026-09-21 | Full score, momentum tier — top pick if a budget slot frees up |
| ASML | Technology | BULLISH | 8/10 | 2026-09-21 | Was 2/10 on 2026-09-19; Tech sector recovery drove the jump |
| WDC | Technology | BULLISH | 8/10 | 2026-09-21 | New entrant this run |
| HPQ | Technology | EXTREMELY_BULLISH_MOMENTUM | 7/8 | 2026-09-21 | Momentum tier |
| TRGP | Energy | EXTREMELY_BULLISH_PULLBACK | 6/10 | 2026-09-21 | Fails P9 only (1.35% to resistance — tight) |
| LLY | Healthcare | BULLISH | 6/10 | 2026-09-21 | Fails P9 only (1.52% to resistance) |

---

## Weekly Tracker

Week of: 2026-09-21 (Monday)
Entries this week: 0 / 3 (LH, FLEX, JBL planned for today's market-open — see RESEARCH-LOG.md)
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
