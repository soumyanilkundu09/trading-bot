# Job 3 — MIDDAY SCAN (runs ~12:30 ET, Mon–Fri)

**Role:** Manage open positions. Cut losers, protect winners, trail stops on momentum. **No new entries.**

> First complete the Mandatory Startup in `agents/prompts/_shared_startup.md`.

## Steps

### 1. Pull live position state
- `python tools/alpaca_client.py --positions` → current price, unrealized P&L per position.
- Reconcile against `state/portfolio.md`. If Alpaca shows a position closed (a bracket stop or target filled since last run), record the exit.
- For each open position, note the **Tier** from `state/portfolio.md`: `EB_PULLBACK`, `EB_MOMENTUM`, or `BULLISH`.

### 2. For each open position, apply exit/management rules

Run `python tools/market_data.py --test <SYM>` to get fresh RSI + volume data.

#### Rules that apply to ALL tiers (check in order — first match acts):

1. **Stop hit / closed by bracket?** → already out; log the exit, compute P&L, move to `state/trade_log.md`.

2. **Daily RSI broken below 40 (Bearish Range Shift)?** → EXIT IMMEDIATELY at market (`close_position(symbol)`). Non-negotiable. Overrides all other rules for all tiers.

3. **High-volume red candle after entry (Bearish Loud Move)?** → exit at market.

4. **Global outlook turned NEGATIVE / VIX spiked above danger?** → reduce position by 50% (`close_position(symbol, percentage=50)`) or exit fully depending on severity. Run `--macro` to check.

#### Rule 5 — Position management (TIER-SPECIFIC):

**For EB_PULLBACK and BULLISH positions:**
- Reached **Target 1** (price at or above `T1` in `state/portfolio.md`, or daily RSI approaching 60)?
  → Close 50% (`close_position(symbol, percentage=50)`), then trail the stop on the remaining half UP to the prior swing low (`replace_stop(symbol, new_stop)`).
- Winner not yet at T1 but comfortably profitable?
  → Consider tightening stop toward breakeven if structure allows (don't choke a healthy trend).

**For EB_MOMENTUM positions:**
- Compute the **3-bar trailing stop**: the low of the 3 most recently completed daily candles (not the live candle).
  ```
  3_bar_low = min(daily_candle[-1].low, daily_candle[-2].low, daily_candle[-3].low)
  ```
- If `3_bar_low > current_stop_in_portfolio` → raise the stop:
  `replace_stop(symbol, 3_bar_low)`, update `state/portfolio.md`, log the change.
- If `3_bar_low ≤ current_stop` → no action needed. A zero-action midday on a Momentum position is correct — do not force a stop update.
- **NEVER close 50% at a fixed price target for Momentum.** The only full-exit triggers are:
  rules 1–4 above (stop hit, BRS RSI<40, high-vol red candle, macro negative).

### 3. Update state
- Update `state/portfolio.md` (new stops, partial exits, status changes).
- For any FULL close: append to `state/trade_log.md` with P&L, R-multiple, exit reason, and tier. Update the sector loss tracker in `state/weekly_tracker.md` (increment consecutive losses on a losing trade, reset on a win).
- If a sector hits 2 consecutive losses → mark it paused in `weekly_tracker.md`.

### 4. Close out
- Commit + push.
- **Telegram:** `🩺 Midday <date>: N open. Actions: <e.g. "Trailed FTNT stop to $X (Momentum 3-bar); T1 hit NVDA — closed 50%">. Portfolio P&L today: <±%>.`
  If no action needed: `🩺 Midday <date>: N positions, all healthy, no action.`

## Guardrails specific to this job
- NEVER opens new positions. Management only.
- Exit-on-RSI-below-40 and stop-hit are non-negotiable, immediate market orders for all tiers.
- No averaging down, ever. A losing position is cut, not reinforced.
- EB Momentum positions: no fixed T1 exit. Trail only. Patience is correct here.
