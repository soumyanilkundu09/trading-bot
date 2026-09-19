# Routine: DAILY SUMMARY (runs ~16:15 ET, Mon–Fri, after close)

**Role:** Snapshot end-of-day portfolio state, re-score the watchlist for tomorrow, send the daily recap. **No new entries.**

> First complete the Mandatory Startup in `routines/_shared_startup.md`.

## Steps

### 1. EOD portfolio snapshot
- `python tools/alpaca_client.py --account` → equity, day change.
- `python tools/alpaca_client.py --positions` → final unrealized P&L per position.
- Reconcile the **Open Positions** section of `memory/TRADE-LOG.md` with Alpaca (catch any stop/target fills during the afternoon → move closed rows to the **Closed Trades** section). Preserve the `Tier` column when updating rows.

### 2. Re-score the watchlist for tomorrow

For each ticker in the **Watchlist** section of `memory/TRADE-LOG.md`:

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
- Tier ≠ NONE **AND** score < 6 → keep on watchlist; update the `Tier`, `Score`, and `Last Scored` columns.
- Tier = NONE → drop from watchlist (setup decayed — remove the row).

Record the current tier in the watchlist entry so market-open tomorrow can apply the correct gauntlet path (scorer is called with the right `--tier` flag).

If any promoted stock would cause `weekly_trade_count` to reach 3 → note it as "watchlist-only until Monday" instead.

### 3. Compute the day's numbers
- Realized P&L today (from any closes), unrealized P&L, portfolio value vs prior day.
- Open positions count, weekly trade count.

### 4. Append EOD snapshot to TRADE-LOG.md
Append a **dated EOD snapshot section** at the bottom of `memory/TRADE-LOG.md`:

```markdown
## EOD Snapshot — YYYY-MM-DD
| Ticker | Tier | Entry $ | Close $ | Stop $ | Unrealized P&L $ | Unrealized P&L % | R |
|--------|------|---------|---------|--------|-----------------|-----------------|---|

**Account:** Equity $X | Day change: ±X% | Realized today: $X
**Open positions:** N/5 | Entries this week: N/3

Notes: (plain-English paragraph — what moved, what held, any thesis changes, watchlist promotions/drops)
```

**This commit is mandatory** — even with no open positions or no activity. Tomorrow's day P&L calculation depends on today's closing prices persisting.

### 5. Close out
- Update `Last Updated` timestamp at the top of `memory/TRADE-LOG.md`.
- Commit + push `memory/TRADE-LOG.md` (always).
- **Telegram:** use `telegram_notify.daily_summary(portfolio_value, day_change_pct, open_count, weekly_trades, positions)`.

## Guardrails specific to this routine
- No new entries. Reporting + watchlist maintenance only.
- This routine is the daily reconciliation backstop — ensure `memory/TRADE-LOG.md` Open Positions exactly matches Alpaca before committing.
- Never use `strategy_scorer.py` alone to re-score watchlist tickers — always classify tier first with `classify_ticker` / `rsi_scan.py`. A Momentum stock scored without `--tier EXTREMELY_BULLISH_MOMENTUM` will have P7 evaluated incorrectly.
