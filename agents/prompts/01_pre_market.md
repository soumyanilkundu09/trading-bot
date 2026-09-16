# Job 1 — PRE-MARKET (runs ~08:30 ET, Mon–Fri)

**Role:** Research catalysts, assess the global gate, scan the universe, and write today's ranked trade ideas. **No orders are placed in this job.**

> First complete the Mandatory Startup in `agents/prompts/_shared_startup.md`.

## Steps

### 1. Assess the Global Market Gate (P1 — mandatory)
Run `python tools/market_data.py --macro` and evaluate Part 3's decision rule:
- S&P 500 Monthly RSI > 60? Weekly RSI healthy?
- VIX below danger threshold (< 25)?
- DXY not spiking (> 3% in 20d)? 10Y yield not surging?

Then determine outlook: **POSITIVE / NEGATIVE / INDECISIVE**.
- If **not POSITIVE** → write research log noting "Global gate FAILED — no scanning today, no trades", notify Telegram, commit, and STOP. (This is a correct, common outcome.)

### 2. Check for upcoming event risk
- Note any FOMC/Fed meeting within 3 days, or major macro events. If a Fed decision is imminent, flag caution in the research log (informs market-open job).

### 3. Scan the universe (only if gate POSITIVE)
Run the two-tier RSI scanner — it covers S&P 500 (~503 tickers) plus `config/universe.json`:

```
python tools/rsi_scan.py
```

The scanner applies **three conditions only** per Malkan's RSI Speedometer:

| Tier | Monthly RSI | Weekly RSI | Daily RSI or BRS |
|------|-------------|------------|-----------------|
| **EXTREMELY BULLISH** | > 60 | > 60 and ≤ 65 | Daily RSI 39–45 **or** daily Bullish Range Shift |
| **BULLISH** | > 60 | > 40 and < 60 | Daily RSI 39–45 **or** daily Bullish Range Shift |

Output is JSON with `EXTREMELY_BULLISH` and `BULLISH` arrays, each sorted by weekly RSI descending.
Capture `symbol`, `monthly_rsi`, `weekly_rsi`, `daily_rsi`, `daily_brs`, and `price` for each hit.

If the scanner returns `gate_passed: false`, treat the same as Step 1 gate failure — write research log, notify Telegram, commit, STOP.

### 4. Rank and classify
- **Active Trade List** (`EXTREMELY_BULLISH` tier): eligible for execution at market-open.
- **Watchlist** (`BULLISH` tier): revisit; update `state/watchlist.md`.
- Everything else is skipped.

### 5. Write the research log
Create `state/research/YYYY-MM-DD_premarket.md` with:
- Global outlook + macro snapshot (the numbers).
- Event-risk flags.
- **Extremely Bullish table** (Monthly RSI>60, Weekly RSI 60-65, Daily 39-45 or BRS): ticker, price, M-RSI, W-RSI, D-RSI, BRS flag.
- **Bullish table** (Monthly RSI>60, Weekly RSI 40-60, Daily 39-45 or BRS): same columns.
- Anything market-open should know (e.g., "AAPL daily BRS confirmed — prioritise at open").

### 6. Close out
- Update `state/watchlist.md`.
- Commit + push.
- **Telegram:** `📋 Pre-market <date>: Outlook POSITIVE. Scanned N. Extremely Bullish: X [tickers]. Bullish: Y [tickers].`
  If gate failed: `📋 Pre-market <date>: Global gate FAILED (<reason>). No trades today.`

## Guardrails specific to this job
- This job NEVER places orders. Research only.
- Do not "force a thesis" — the RSI tiers are the entry filter; do not add stocks that nearly-but-don't-quite pass.
- Respect remaining weekly budget when sizing the Active list (if `weekly_trade_count` already 3, note that all picks are watchlist-only).
