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
For each ticker in `config/universe.json`, run the scorer. Practical approach:
- Score candidates with: `python tools/strategy_scorer.py --ticker <SYM> --sector <SectorName>`
- The scorer pre-filters via the analysis; collect results where `gate_passed` is true and `decision` in (`ENTER_FULL`, `WATCHLIST_HALF`).
- To keep runtime/cost reasonable, you may pre-screen with `--test` (analyze_ticker) and only fully score names whose Monthly RSI > 60, Weekly RSI > 60, and Daily RSI in 35–48.
- Batch them; capture each result's score, decision, passed/failed params, disqualifiers, and trade_plan.

### 4. Rank and classify
- **Active Trade List** (score ≥ 86, no disqualifiers): eligible for execution at market-open.
- **Watchlist** (65–85): revisit; update `state/watchlist.md`.
- **Skip** (< 65 or disqualified): note briefly.

### 5. Write the research log
Create `state/research/YYYY-MM-DD_premarket.md` with:
- Global outlook + macro snapshot (the numbers).
- Event-risk flags.
- Active Trade List table: ticker, sector, score, entry/SL/T1/T2, position size, key thesis, which params passed/failed.
- Watchlist table.
- Anything market-open should know (e.g., "AAPL only enters if P8 confirms green+volume at open").

### 6. Close out
- Update `state/watchlist.md`.
- Commit + push.
- **Telegram:** `📋 Pre-market <date>: Outlook <POSITIVE/…>. Scanned N. Active: X [tickers]. Watch: Y. Top: <ticker> (<score>).`
  If gate failed: `📋 Pre-market <date>: Global gate FAILED (<reason>). No trades today.`

## Guardrails specific to this job
- This job NEVER places orders. Research only.
- Do not "force a thesis" — if the whole sector (sector ETF weekly RSI < 60) is rolling over, drop its candidates even if an individual name looks ok.
- Respect remaining weekly budget when sizing the Active list (if `weekly_trade_count` already 3, note that all picks are watchlist-only).
