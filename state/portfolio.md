# Portfolio — Open Positions

> Source of truth for currently held positions. Updated by market-open, midday, and daily-summary runs.
> Alpaca is authoritative for fills/prices; this file mirrors it plus strategy metadata (score, targets, thesis).

**Last updated:** (never — initial state)
**Trading mode:** PAPER

## Open Positions

| Ticker | Sector | Tier | Entry Date | Entry $ | Shares | Stop $ | T1 $ | Status | Thesis |
|--------|--------|------|-----------|---------|--------|--------|------|--------|--------|
| _(none yet)_ | | | | | | | | | |

## Closed This Session

| Ticker | Exit Date | Exit $ | P&L $ | P&L % | Reason |
|--------|-----------|--------|-------|-------|--------|
| _(none)_ | | | | | |

---
### Notes
- Max 5 open positions (Guardrail 8B).
- Each position max 5% of equity, risk max 2% of capital.
- **Tier column is mandatory** — midday scan uses it to pick the correct exit rule.
- EB_PULLBACK / BULLISH: T1 hit → close 50%, trail stop to prior swing low.
- EB_MOMENTUM: no fixed T1. Trail stop using 3-bar daily candle low. Exit on trailing stop or BRS only.
- Exit immediately if daily RSI < 40 (Bearish Range Shift) or stop hit (all tiers).
