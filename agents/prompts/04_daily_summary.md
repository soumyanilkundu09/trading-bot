# Job 4 — DAILY SUMMARY (runs ~16:15 ET, Mon–Fri, after close)

**Role:** Snapshot end-of-day portfolio state, re-score the watchlist for tomorrow, send the daily recap. **No new entries.**

> First complete the Mandatory Startup in `agents/prompts/_shared_startup.md`.

## Steps

### 1. EOD portfolio snapshot
- `python tools/alpaca_client.py --account` → equity, day change.
- `python tools/alpaca_client.py --positions` → final unrealized P&L per position.
- Reconcile `state/portfolio.md` with Alpaca (catch any stop/target fills during the afternoon → move closed ones to `state/trade_log.md`). Preserve the `Tier` column when updating rows.

### 2. Re-score the watchlist for tomorrow

For each ticker in `state/watchlist.md`:

**Step A — Re-classify tier:**
Run `classify_ticker(symbol)` (importable from `tools/rsi_scan.py`), or equivalently:
```
python tools/rsi_scan.py --no-sp500
```
and look up the ticker's current tier in the output.

**Step B — If tier is non-NONE, score it:**
```
python tools/strategy_scorer.py --ticker <SYM> --sector <Sector> --tier <TIER>
```

**Promotion / drop logic:**
- Tier ≠ NONE **AND** score ≥ 6 → mark "PROMOTE" for tomorrow's Active Trade List; note the tier. This stock should be prioritised at market-open.
- Tier ≠ NONE **AND** score ≤ 6 → keep on watchlist; update the `Tier` and last-scored date columns.
- Tier = NONE → drop from watchlist (setup decayed — remove the row).

Record the current tier in the watchlist entry so market-open tomorrow can apply the correct gauntlet path (scorer is called with the right `--tier` flag).

If any promoted stock would cause `weekly_trade_count` to reach 3 → note it as "watchlist-only until Monday" instead.

### 3. Compute the day's numbers
- Realized P&L today (from any closes), unrealized P&L, portfolio value vs prior day.
- Open positions count, weekly trade count.

### 4. Write the daily log
Create `logs/YYYY-MM-DD_1615_daily.md`:
- Equity, day change %, realized + unrealized P&L.
- Per-position table with P&L% and Tier.
- Watchlist changes: promotions (with tier), drops (with reason), kept entries.
- Any anomalies (failed orders, data gaps).

### 5. Close out
- Update `state/portfolio.md`, `state/watchlist.md`.
- Commit + push.
- **Telegram:** use `telegram_notify.daily_summary(portfolio_value, day_change_pct, open_count, weekly_trades, positions)`.

## Guardrails specific to this job
- No new entries. Reporting + watchlist maintenance only.
- This job is the daily reconciliation backstop — ensure `portfolio.md` exactly matches Alpaca before committing.
- Never use `strategy_scorer.py` alone to re-score watchlist tickers — always classify tier first with `classify_ticker` / `rsi_scan.py`. A Momentum stock scored without `--tier EXTREMELY_BULLISH_MOMENTUM` will have P7 evaluated incorrectly.
