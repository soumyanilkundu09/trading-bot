# Job 2 — MARKET-OPEN (runs ~09:45 ET, Mon–Fri)

**Role:** Score and execute the planned trades from this morning's research log, with full guardrail enforcement. Set protective stops on every new position.

> First complete the Mandatory Startup in `agents/prompts/_shared_startup.md`.

## Steps

### 1. Load today's plan
- Read `state/research/YYYY-MM-DD_premarket.md` (today's date).
- If it doesn't exist (pre-market didn't run or gate failed) → log "No research/plan for today", notify, commit, STOP.
- Extract three candidate lists:
  - **Active — EB Pullback**: all rows from the EXTREMELY BULLISH PULLBACK table
  - **Active — EB Momentum**: all rows from the EXTREMELY BULLISH MOMENTUM table
  - **Active — Bullish**: all rows from the BULLISH table
- All three are eligible for same-day entry (subject to the gauntlet in Step 3).

### 2. Re-confirm the global gate hasn't deteriorated
- Quick `python tools/market_data.py --macro`. If VIX has spiked above danger or outlook flipped NEGATIVE since pre-market → **abort all entries**, notify, STOP.

### 3. For each candidate across all three lists, run the entry gauntlet (in order)
Apply these checks to every candidate regardless of tier — first failure blocks the trade and emits an 8F guardrail alert:

1. **Re-classify**: run `classify_ticker(symbol)` (or `python tools/rsi_scan.py --no-sp500 --ticker <SYM>`) fresh. Confirm the ticker still returns its expected tier. If tier has changed to NONE → skip with reason "setup decayed".

2. **Score**: run the 5-parameter scorer with the live Alpaca price:
   ```
   python tools/strategy_scorer.py --ticker <SYM> --sector <Sector> --tier <TIER> --live
   ```
   - Score must be **≥ 6** to proceed.
   - For EB Momentum: P7 is automatically skipped (max score = 8); threshold remains ≥ 6.
   - If score ≤ 6 → skip with reason "scorer failed (score=X/Y, failed: [params])".

3. **Not chasing**: live price must be ≤ 3% above yesterday's close. If chasing → watchlist, do not enter.

4. **Weekly budget**: `weekly_trade_count < 3` (Guardrail 8E) → else block + watchlist for next Monday.

5. **Position cap**: current open positions < 5 (Guardrail 8B) → else block.

6. **Not already held**: skip if we already hold this ticker in `state/portfolio.md`.

Only candidates clearing all 6 checks proceed to Step 4. Use the `trade_plan` from the scorer for the order.

### 4. Place the order (PAPER mode)
For each survivor, use the scorer's `trade_plan`:

**EB Pullback and Bullish:**
- Submit a **bracket order** via `AlpacaClient().place_bracket_order(symbol, shares, stop_loss, target1)`.
- Stop = entry candle low (from `trade_plan.stop_loss`). T1 = nearest resistance (from `trade_plan.target1`).
- This attaches stop-loss AND take-profit atomically — position is never unprotected.

**EB Momentum:**
- Submit a **stop-only order** (no fixed T1 bracket): `AlpacaClient().place_order(symbol, shares, stop_loss)`.
- `trade_plan.trailing_stop_only == True` confirms this path.
- The trailing stop is managed dynamically in the midday-scan job (3-bar candle low).
- No fixed take-profit is set — the position rides until the trailing stop is hit or a hard-exit rule fires.

Confirm the order was accepted; capture order id + status. If REAL mode and unattended → suppress order per 8A handling in shared startup; emit alert instead.

### 5. Update state
- Append the new position to `state/portfolio.md`. Include the **Tier** field for each new row:
  - `EB_PULLBACK`, `EB_MOMENTUM`, or `BULLISH`
- Increment `weekly_trade_count` in `state/weekly_tracker.md` and add the entry row.
- Remove the ticker from `state/watchlist.md` if it was there.

### 6. Close out
- Commit + push.
- **Telegram per trade:** use `telegram_notify.trade_alert(...)`.
- **Telegram summary:** `🔔 Market-open <date>: Entered X trade(s): [TICKER(TIER), ...]. Blocked: Y. Weekly: Z/3. Open: N/5.`
  If nothing entered: `🔔 Market-open <date>: No trades. <reason: no triggers / budget full / gate / no candidates>.`

## Guardrails specific to this job
- This is the ONLY job that opens new positions.
- Every block → structured 8F alert via `telegram_notify.guardrail_block(...)`. No silent skips.
- Never exceed weekly budget or position cap even if multiple A+ setups appear — take the highest-scored ones up to the limit.
- Position size comes from the scorer's `trade_plan` (2% risk, 5% cap). Do not override.
- EB Momentum positions MUST use stop-only orders — never set a fixed bracket T1 for momentum.
