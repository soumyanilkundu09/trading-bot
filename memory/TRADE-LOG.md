# Trade Log — Last Updated: 2026-10-02 08:30 ET (pre-market run)
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
| NEM | Materials | BULLISH | 6/10 | 10 | 2026-10-02 | P2 (Materials W-RSI 40.18), P8 (0.93x — hard gate), P10 (1.02x) | Scorer ENTER but P8 gate blocks; re-check for green-volume improvement |
| MRVL | Technology | EB_MOMENTUM | 7/8 | 8 | 2026-10-02 | P8 (green vol 0.93x — hard gate) | Blocked by P8; revisit if volume confirms |
| COP | Energy | BULLISH | 4/10 | 10 | 2026-10-02 | Energy sector, see scorer | Daily RSI 45.2 |
| INTC | Technology | EB_PULLBACK | 4/10 | 10 | 2026-10-02 | Daily RSI 61.7 (not pullback) | BRS-path hit only |
| V | Financials | BULLISH | 3/10 | 10 | 2026-10-02 | P2 (Financials weak) | Daily RSI 40.1 |
| LLY | Healthcare | BULLISH | 3/10 | 10 | 2026-10-02 | P9/P10 | Daily RSI 45.1 |

Dropped 2026-10-02 (no longer in tier / score < 3): CRWD, ASML, DDOG, TXN, SCHW, NVDA (now momentum, 2/8), CSCO, MA, CAT, EQIX (2/10), KO (2/10).

**Promoted to Active Trade List (2026-10-02):**
| Ticker | Sector | Tier | Score | Promoted On | Notes |
|--------|--------|------|-------|-------------|-------|
| MU | Technology | EB_MOMENTUM | 8/8 | 2026-10-02 | PROMOTE — see RESEARCH-LOG.md |
| MRK | Healthcare | EB_PULLBACK | 7/10 | 2026-10-02 | PROMOTE — true pullback, daily RSI 45.0 |
| META | Communication | EB_PULLBACK | 8/10 | 2026-10-02 | PROMOTE (low conviction — daily RSI 61, P2 data n/a) |

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
