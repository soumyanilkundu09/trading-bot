# Trade Log — Last Updated: 2026-10-27 05:50 ET (pre-market run)
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
| DE | Industrials | BULLISH | 4/10 | 10 | 2026-10-27 | P2 (Ind W-RSI 41.2), P9 (0.4% to res) | At resistance; sector weak |
| CSCO | Technology | BULLISH | 4/10 | 10 | 2026-10-27 | P2 (Tech 55.02), P9 (1.11%) | |
| NEM | Materials | BULLISH | 4/10 | 10 | 2026-10-27 | P2 (53.0), P9 (1.31%) | Daily RSI 39.4, no BRS |
| CEG | Utilities | BULLISH | 4/10 | 10 | 2026-10-27 | P2 (46.95), P9 (4.62%) | |
| PFE | Healthcare | EB_MOMENTUM | 4/8 | 8 | 2026-10-27 | P9 (2.18% to res) | |
| TSM | Technology | BULLISH | 3/10 | 10 | 2026-10-27 | P2, P9 (0.21%), P10 | |
| AMD | Technology | BULLISH | 3/10 | 10 | 2026-10-27 | P2, P9, P10 | |
| MU | Technology | BULLISH | 3/10 | 10 | 2026-10-27 | P2, P9, P10 | |
| NVDA | Technology | BULLISH | 3/10 | 10 | 2026-10-27 | P2, P9, P10 | |
| PSX | Energy | EB_MOMENTUM | 3/8 | 8 | 2026-10-27 | P8, P9 | |
| KO | Consumer_Staples | EB_MOMENTUM | 3/8 | 8 | 2026-10-27 | P9, P10 | |

**Promoted to Active Trade List:** none (2026-10-27).

**Dropped 2026-10-27 (no longer in any tier or scored ≤2):** CRWD, DDOG, TXN, SCHW, MA, CAT, ASML, LLY (tier decayed / not in scan output); LMT, PANW, DHR, EQIX, MRVL scored ≤2 and are not tracked.

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
