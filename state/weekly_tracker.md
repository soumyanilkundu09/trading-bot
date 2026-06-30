# Weekly Trade Tracker

> Enforces Guardrail 8E: max 3 new position entries per Mon–Fri week.
> Reset every Monday (weekly-review run on Friday resets the counter to 0 for the upcoming week).

**Current week starting (Monday):** _set on first run_
**Weekly trade count:** 0 / 3

## Entries This Week

| Date | Ticker | Score | Shares | Entry $ |
|------|--------|-------|--------|---------|
| _(none yet)_ | | | | |

## Sector Loss Tracker (Guardrail: exit sector after 2 consecutive failed trades)

| Sector | Consecutive Losses | Status |
|--------|--------------------|--------|
| _(none)_ | 0 | active |

---
### Rules
- `weekly_trade_count` increments on each confirmed entry.
- If `weekly_trade_count >= 3` → block new entries, watchlist them for next Monday.
- Reset to 0 every Monday 00:01 ET (handled by Friday weekly-review run).
- 2 consecutive losses in a sector → pause that sector until weekly review re-enables it.
