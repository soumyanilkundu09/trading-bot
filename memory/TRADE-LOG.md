# Trade Log — Last Updated: 2026-11-04 04:45 ET (pre-market run)
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
| MRK | Healthcare | BULLISH | 5/10 | 10 | 2026-11-04 | P9 (2.37% to res), P10 (1.0x) | Gap support 0.78%; 1 pt short |
| CRWD | Technology | BULLISH | 4/10 | 10 | 2026-11-04 | P2 (XLK W-RSI 47.2), P7, P8, P10 | Dropped from EB_MOMENTUM; now BULLISH tier |
| TSM | Technology | BULLISH | 4/10 | 10 | 2026-11-04 | P2, P7, P8, P10 (1.27x) | Daily RSI 39.3, no BRS |
| JNJ | Healthcare | BULLISH | 4/10 | 10 | 2026-11-04 | P8, P9 (1.22%), P10 | At support |
| C | Financials | BULLISH | 3/10 | 10 | 2026-11-04 | P2 (Fin W-RSI 59.6), P8, P9 | CIP support |
| DE | Industrials | BULLISH | 3/10 | 10 | 2026-11-04 | P2, P8, P9 | At support |
| ABNB | Consumer_Discretionary | BULLISH | 3/10 | 10 | 2026-11-04 | P2, P9, P10 | |
| KO | Consumer_Staples | EB_MOMENTUM | 3/8 | 8 | 2026-11-04 | P9 (0.62% to res), P10 | At resistance |
| PM | Consumer_Staples | EB_MOMENTUM | 2/8 | 8 | 2026-11-04 | P8, P9, P10 | |

**Promoted to Active Trade List (2026-11-04):**
| Ticker | Sector | Tier | Score | Promoted On | Notes |
|--------|--------|------|-------|-------------|-------|
| MU | Technology | BULLISH | 7/10 | 2026-11-04 | PROMOTE (conditional) — tight 0.56% stop, marginal gate; see RESEARCH-LOG.md |

> Dropped 2026-11-04 (no longer in tier / stale): ASML, LLY, NVDA, DDOG, TXN, SCHW, CSCO, MA, CAT, PANW (0/10), EQIX (W-RSI 49.9 — scanner BULLISH but unscored).

---

## Weekly Tracker

Week of: 2026-11-02 (Monday)
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
