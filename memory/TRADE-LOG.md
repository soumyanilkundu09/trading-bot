# Trade Log — Last Updated: 2026-09-22 05:45 ET (pre-market run)
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
| CSCO | Technology | BULLISH | 5/10 | 10 | 2026-09-22 | P9 (2.46% to res), P10 (1.22x) | 1 pt short of ENTER; watch for resistance clearance |
| MPWR | Technology | BULLISH | 5/10 | 10 | 2026-09-22 | P9 (near res), P10 | 1 pt short of ENTER |
| CRWD | Technology | EB_MOMENTUM | 4/8 | 8 | 2026-09-22 | P9 (near resistance) | Was 8/8 ENTER (blocked on chase) 2026-09-21; pulled back and score dropped — re-check after further consolidation |
| NVDA | Technology | BULLISH (filtered) | 4/10 | 10 | 2026-09-22 | Scanner: near_resistance (3.28%); scorer: P7 (4.83% from support), P9 (1.39% to res) | Extended; wait for pullback to support |
| SCHW | Financials | BULLISH | 4/10 | 10 | 2026-09-22 | P2 (Fin W-RSI 54.61 < 60), P9 (1.01% to res) | Needs Financials sector recovery |
| DDOG | Technology | BULLISH | 4/10 | 10 | 2026-09-22 | P8, P9 (2.46%), P10 | Score dropped from 5/10 |
| AMGN | Healthcare | BULLISH | 4/10 | 10 | 2026-09-22 | P7 (from support), P9 | New to watchlist |
| KO | Consumer_Staples | BULLISH | 3/10 | 10 | 2026-09-22 | P2, P9, P10 | New to watchlist |
| NBIS | Technology | BULLISH | 3/10 | 10 | 2026-09-22 | P7, P9 (0.40% to res), P10 | New to watchlist |
| ASML | Technology | BULLISH | 3/10 | 10 | 2026-09-22 | P7, P9, P10 | Score collapsed from 8/10 (2026-09-21 promotion never executed — Open Positions still empty); demoted back to watchlist |
| BRK.B | Financials | BULLISH | 3/10 | 10 | 2026-09-22 | P2, P9, P10 | New to watchlist |
| CAT | Industrials | BULLISH | 3/10 | 10 | 2026-09-22 | P2 (Ind W-RSI 43.35), P8, P9 (2.67% to res) | Industrials sector deeply below P2 threshold |
| WMT | Consumer_Staples | BULLISH | 3/10 | 10 | 2026-09-22 | P2, P8, P9 | New to watchlist |
| EQIX | Real_Estate | BULLISH (filtered) | 3/10 | 10 | 2026-09-22 | Scanner: near_resistance (4.65%); scorer: P2 (RE W-RSI 42.30), P8, P9 (0.22% — at resistance) | Data center play; RE sector weak |

**Dropped 2026-09-22 (tier decayed to NONE):** MA — no longer qualifies for any RSI tier, removed from watchlist.
**Not carried to watchlist 2026-09-22 (score 0–2, multiple hard failures):** COP (0/10), ETN (1/10), XOM (2/10), META (2/10), ANET (2/10), TSM (2/10) — scanned, scored, not promising enough to track.

**Promoted to Active Trade List (2026-09-22):**
| Ticker | Sector | Tier | Score | Promoted On | Notes |
|--------|--------|------|-------|-------------|-------|
| MRVL | Technology | EB_PULLBACK | 9/10 | 2026-09-22 | PROMOTE — primary idea; only P8 failed. See RESEARCH-LOG.md |
| LRCX | Technology | BULLISH | 7/10 | 2026-09-22 | PROMOTE — P7/P10 failed (chasing strength, not textbook pullback). See RESEARCH-LOG.md |
| MU | Technology | EB_PULLBACK | 6/10 | 2026-09-22 | PROMOTE — P9 fail (mildest miss of the 6/10 group). See RESEARCH-LOG.md |

**Qualified but budget-blocked (2026-09-22 — score ≥6, weekly budget 3/3 already allocated to the above):**
| Ticker | Sector | Tier | Score | Key Blockers | Notes |
|--------|--------|------|-------|--------------|-------|
| TXN | Technology | BULLISH | 6/10 | P9 (0.94% to res) | Next in line if an entered position exits early this week |
| LLY | Healthcare | BULLISH | 6/10 | P9 (0.45% — essentially at resistance) | Weakest R:R of the six ENTER-qualified names |
| MS | Financials | BULLISH | 6/10 | P2 (Fin sector weak), P8, P10 | Lowest priority — sector-strength gate also fails |

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
