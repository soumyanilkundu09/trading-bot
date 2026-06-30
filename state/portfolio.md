# Portfolio — Open Positions

> Source of truth for currently held positions. Updated by market-open, midday, and daily-summary runs.
> Alpaca is authoritative for fills/prices; this file mirrors it plus strategy metadata (score, targets, thesis).

**Last updated:** (never — initial state)
**Trading mode:** PAPER

## Open Positions

| Ticker | Sector | Entry Date | Entry $ | Shares | Stop $ | T1 $ | T2 $ | Score | Status | Thesis |
|--------|--------|-----------|---------|--------|--------|------|------|-------|--------|--------|
| _(none yet)_ | | | | | | | | | | |

## Closed This Session

| Ticker | Exit Date | Exit $ | P&L $ | P&L % | Reason |
|--------|-----------|--------|-------|-------|--------|
| _(none)_ | | | | | |

---
### Notes
- Max 5 open positions (Guardrail 8B).
- Each position max 5% of equity, risk max 2% of capital.
- T1 hit → close 50%, trail stop to prior swing low.
- Exit immediately if daily RSI < 40 (Bearish Range Shift) or stop hit.
