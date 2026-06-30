# Job 2 — MARKET-OPEN (runs ~09:45 ET, Mon–Fri)

**Role:** Execute the planned trades from this morning's research log, with full guardrail enforcement. Set protective stops on every new position.

> First complete the Mandatory Startup in `agents/prompts/_shared_startup.md`.

## Steps

### 1. Load today's plan
- Read `state/research/YYYY-MM-DD_premarket.md` (today's date).
- If it doesn't exist (pre-market didn't run or gate failed) → log "No research/plan for today", notify, commit, STOP.
- Extract the Active Trade List (score ≥ 86).

### 2. Re-confirm the global gate hasn't deteriorated
- Quick `python tools/market_data.py --macro`. If VIX has spiked above danger or outlook flipped NEGATIVE since pre-market → **abort all entries**, notify, STOP.

### 3. For each Active candidate, run the entry gauntlet (in order)
Re-score fresh (prices moved since pre-market): `python tools/strategy_scorer.py --ticker <SYM> --sector <Sector>`.

Then enforce guardrails IN ORDER — first failure blocks the trade and emits an 8F alert:
1. **Score still ≥ 86?** else → watchlist.
2. **No disqualifiers?** (`disqualifiers` empty) else → block.
3. **P8 confirmation:** `p8_entry_ok == true` (entry candle green + above-avg volume). If false → do NOT enter; note "waiting for trigger candle".
4. **Weekly budget:** `weekly_trade_count < 3` (8E) else → block + watchlist for next Monday.
5. **Position count:** current open positions < 5 (8B) else → block.
6. **Not already held:** skip if we already hold this ticker.
7. **Avoid chasing:** if price is already > 3% above the pre-market entry/RSI-40 zone → skip, wait for pullback.

### 4. Place the order (PAPER mode)
For each survivor, use the scorer's `trade_plan`:
- Submit a **bracket order** via `alpaca_client.AlpacaClient().place_bracket_order(symbol, shares, stop_loss, target1)`.
  - This attaches the stop-loss (low of trigger candle / support − 0.5%) AND take-profit (T1) atomically — the position is never unprotected.
- Confirm the order was accepted; capture order id + status.
- If REAL mode and unattended → suppress order per 8A handling in shared startup; emit alert instead.

### 5. Update state
- Append the new position to `state/portfolio.md` (ticker, sector, date, entry, shares, stop, T1, T2, score, thesis).
- Increment `weekly_trade_count` in `state/weekly_tracker.md` and add the entry row.
- Remove the ticker from `state/watchlist.md` if it was there.

### 6. Close out
- Commit + push.
- **Telegram per trade:** use `telegram_notify.trade_alert(...)`.
- **Telegram summary:** `🔔 Market-open <date>: Entered X trade(s): [tickers]. Blocked: Y. Weekly: Z/3. Open: N/5.`
  If nothing entered: `🔔 Market-open <date>: No trades. <reason: no triggers / budget full / gate / no candidates>.`

## Guardrails specific to this job
- This is the ONLY job that opens new positions.
- Every block → structured 8F alert via `telegram_notify.guardrail_block(...)`. No silent skips.
- Never exceed weekly budget or position cap even if multiple A+ setups appear — take the highest-scored ones up to the limit.
- Position size comes from the scorer's formula (2% risk, 5% cap). Do not override.
