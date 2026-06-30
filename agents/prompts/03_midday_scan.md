# Job 3 — MIDDAY SCAN (runs ~12:30 ET, Mon–Fri)

**Role:** Manage open positions. Cut losers, protect winners, honor exit rules. **No new entries.**

> First complete the Mandatory Startup in `agents/prompts/_shared_startup.md`.

## Steps

### 1. Pull live position state
- `python tools/alpaca_client.py --positions` → current price, unrealized P&L per position.
- Reconcile against `state/portfolio.md`. If Alpaca shows a position closed (a bracket stop or target filled since last run), record the exit.

### 2. For each open position, apply exit/management rules (Part 6 + cheat sheet)
Re-analyze the ticker: `python tools/market_data.py --test <SYM>`.

Check in order:
1. **Stop hit / closed by bracket?** → it's already out; log the exit, compute P&L, move to trade_log.
2. **Daily RSI broken below 40?** → Bearish Range Shift. EXIT IMMEDIATELY at market (`close_position(symbol)`). This overrides everything.
3. **High-volume red candle after entry (Bearish Loud Move)?** → exit.
4. **Global outlook turned NEGATIVE / VIX spiked above danger?** → reduce position by 50% or exit (run `--macro` to check).
5. **Reached Target 1 (near nearest resistance / RSI ~60)?** → close 50% (`close_position(symbol, percentage=50)`), then trail the stop on the remaining half UP to the prior swing low (`replace_stop(symbol, new_stop)`).
6. **Winner not yet at T1 but comfortably profitable?** → consider tightening stop toward breakeven if structure allows (don't choke a healthy trend).

### 3. Update state
- Update `state/portfolio.md` (new stops, partial exits, status).
- For any FULL close, append to `state/trade_log.md` with P&L, R-multiple, exit reason; and update the sector loss tracker in `state/weekly_tracker.md` (increment consecutive losses on a losing trade, reset on a win).
- If a sector hits 2 consecutive losses → mark it paused in `weekly_tracker.md`.

### 4. Close out
- Commit + push.
- **Telegram:** `🩺 Midday <date>: N open. Actions: <e.g. "Trailed NVDA stop to $X; exited AMD (RSI<40, −1.8%)">. Portfolio P&L today: <±%>.`
  If no action needed: `🩺 Midday <date>: N positions, all healthy, no action.`

## Guardrails specific to this job
- NEVER opens new positions. Management only.
- Exit-on-RSI-below-40 and stop-hit are non-negotiable, immediate, market orders.
- No averaging down, ever. A losing position is cut, not reinforced.
