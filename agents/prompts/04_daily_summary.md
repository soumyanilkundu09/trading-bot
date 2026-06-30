# Job 4 — DAILY SUMMARY (runs ~16:15 ET, Mon–Fri, after close)

**Role:** Snapshot end-of-day portfolio state, re-score the watchlist for tomorrow, send the daily recap. **No new entries.**

> First complete the Mandatory Startup in `agents/prompts/_shared_startup.md`.

## Steps

### 1. EOD portfolio snapshot
- `python tools/alpaca_client.py --account` → equity, day change.
- `python tools/alpaca_client.py --positions` → final unrealized P&L per position.
- Reconcile `state/portfolio.md` with Alpaca (catch any stop/target fills during the afternoon → move closed ones to `state/trade_log.md`).

### 2. Re-score the watchlist for tomorrow
- For each ticker in `state/watchlist.md`, re-run `python tools/strategy_scorer.py --ticker <SYM> --sector <Sector>`.
- If any now scores ≥ 86 with no disqualifiers AND weekly budget would allow → mark it "PROMOTE" so tomorrow's pre-market/market-open prioritizes it. Note it in tomorrow context.
- Drop stale watchlist names whose setup has decayed (score < 65 or disqualified).

### 3. Compute the day's numbers
- Realized P&L today (from any closes), unrealized P&L, portfolio value vs prior day.
- Open positions count, weekly trade count.

### 4. Write the daily log
Create `logs/YYYY-MM-DD_1615_daily.md`:
- Equity, day change %, realized + unrealized P&L.
- Per-position table with P&L%.
- Watchlist changes / promotions.
- Any anomalies (failed orders, data gaps).

### 5. Close out
- Update `state/portfolio.md`, `state/watchlist.md`.
- Commit + push.
- **Telegram:** use `telegram_notify.daily_summary(portfolio_value, day_change_pct, open_count, weekly_trades, positions)`.

## Guardrails specific to this job
- No new entries. Reporting + watchlist maintenance only.
- This job is the daily reconciliation backstop — ensure `portfolio.md` exactly matches Alpaca before committing.
