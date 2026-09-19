# Routine: PRE-MARKET (runs ~08:30 ET, Mon–Fri)

**Role:** Research catalysts, assess the global gate, scan the universe, and write today's ranked trade ideas into `memory/RESEARCH-LOG.md`. **No orders are placed in this routine.**

> First complete the Mandatory Startup in `routines/_shared_startup.md`.

## Steps

### 1. Assess the Global Market Gate (P1 — mandatory)
Run `python tools/market_data.py --macro` and evaluate Part 3's decision rule:
- S&P 500 Monthly RSI > 60? Weekly RSI healthy?
- VIX below danger threshold (< 25)?
- DXY not spiking (> 3% in 20d)? 10Y yield not surging?

Then determine outlook: **POSITIVE / NEGATIVE / INDECISIVE**.
- If **not POSITIVE** → write research log noting "Global gate FAILED — no scanning today, no trades", notify Telegram, commit, and STOP. (This is a correct, common outcome.)

### 2. Pull account snapshot
Run `python tools/alpaca_client.py --account` → equity, buying power, open P&L.
Include this in the research log header.

### 3. Check for upcoming event risk
- Note any FOMC/Fed meeting within 3 days, or major macro events. If a Fed decision is imminent, flag caution in the research log (informs market-open routine).

### 4. Scan the universe (only if gate POSITIVE)
Run the three-tier RSI scanner — it covers S&P 500 (~503 tickers) plus `config/universe.json`:

```
python tools/rsi_scan.py
```

The scanner applies **three tiers** per Malkan's RSI Speedometer:

| Tier | Monthly RSI | Weekly RSI | Daily RSI | BRS |
|------|-------------|------------|-----------|-----|
| **EXTREMELY BULLISH PULLBACK** | > 60 | > 60 and ≤ 65 | 39–45 | or daily BRS |
| **EXTREMELY BULLISH MOMENTUM** | > 60 | > 60 (no cap) | 59–65 | — |
| **BULLISH** | > 60 | > 40 and < 60 | 39–45 | or daily BRS |

Output is JSON with `EXTREMELY_BULLISH_PULLBACK`, `EXTREMELY_BULLISH_MOMENTUM`, and `BULLISH` arrays, each sorted by weekly RSI descending.
Capture `symbol`, `monthly_rsi`, `weekly_rsi`, `daily_rsi`, `daily_brs`, and `price` for each hit.

If the scanner returns `gate_passed: false`, treat the same as Step 1 gate failure — write research log, notify Telegram, commit, STOP.

### 5. Rank, classify, and score
- **Active Trade List — Pullback** (`EXTREMELY_BULLISH_PULLBACK` tier): pullback entry; daily RSI near 40 zone or BRS confirmed.
- **Active Trade List — Momentum** (`EXTREMELY_BULLISH_MOMENTUM` tier): momentum continuation; daily RSI 59–65.
- **Watchlist** (`BULLISH` tier): re-score using `python tools/strategy_scorer.py --ticker <SYM> --sector <Sector> --tier BULLISH`. Update the Watchlist section of `memory/TRADE-LOG.md`.
- Everything else is skipped.

For each trade idea, produce a trade plan: entry ~price, stop, target (T1), R/R, shares, order type.

### 6. Write the research log
**Overwrite** `memory/RESEARCH-LOG.md` with the following structure:

```
# Research Log — Last Run: YYYY-MM-DD HH:MM ET (pre-market)

## Account Snapshot
(equity, buying power, open P&L)

## Global Gate
(indicator table + verdict)

## Event Risk
(any upcoming FOMC / macro events)

## Risk Factors
(sector-level P2 blocks, macro headwinds, any held positions below -7%)

## Scanner Output
(sector ETF snapshot, then 3 tier tables with scores)

## Today's Entry Plan
Trade/hold decision: ENTER X trade(s) / HOLD (no setups)
For each ENTER: full thesis, entry, stop, target, R/R, shares, order type
```

**Notification:** Silent unless urgent — a held position is already below -7% in pre-market, a thesis broke overnight, or a major geopolitical event.
- If urgent: send Telegram alert immediately with details.
- If routine: no Telegram during pre-market; market-open summary covers it.

### 7. Update watchlist in TRADE-LOG.md
Update the **Watchlist** section of `memory/TRADE-LOG.md` with:
- Promoted tickers (score ≥ 6) → mark "PROMOTE" (they appear in Today's Entry Plan)
- Dropped tickers (tier decayed to NONE) → remove the row
- Kept tickers → update last-scored date and any blocker changes

### 8. Close out
- **Commit:** `git add -A && git commit -m "run: pre-market YYYY-MM-DD"` — always commit (even gate failure).
- **Push.**
- **Telegram:** Always send one notification after push. Format:

**If gate POSITIVE and tickers found:**
```
📋 Pre-market YYYY-MM-DD — Gate: ✅ POSITIVE
SPX M/W RSI: XX.X / XX.X | VIX: XX.X

Ticker | Tier         | Score | Decision
-------|--------------|-------|----------
LLY    | BULLISH      |  6/10 | ENTER ✅
SCHW   | BULLISH      |  4/10 | WATCH
MA     | BULLISH      |  3/10 | WATCH
DDOG   | BULLISH      |  3/10 | WATCH
ASML   | EB PULLBACK  |  2/10 | BELOW THRESHOLD

Scanned: N | Entering: X | Watching: Y
```
Sort all tickers by score descending. "ENTER ✅" if score ≥ 6, "WATCH" if below threshold, "BELOW THRESHOLD" if dropped from watchlist. Include tier column so reader knows the setup type at a glance.

**If gate POSITIVE but no tickers:**
```
📋 Pre-market YYYY-MM-DD — Gate: ✅ POSITIVE
SPX M/W RSI: XX.X / XX.X | VIX: XX.X

No setups today. Scanned: N | Watchlist: W tickers (none scored ≥ 6).
```

**If gate FAILED:**
```
📋 Pre-market YYYY-MM-DD — Gate: ❌ FAILED
Reason: <e.g. SPX M-RSI 58.2 < 60 / VIX 28.1 > 25>
No scanning. No trades today.
```

**Urgent add-on** (append to any of the above if urgent conditions are met — held position below -7%, thesis broke overnight, major geopolitical event):
```
⚠️ URGENT: <one-line description of the urgent condition>
```

## Guardrails specific to this routine
- This routine NEVER places orders. Research only.
- Do not "force a thesis" — RSI tiers are the entry filter; do not add stocks that nearly-but-don't-quite pass.
- Respect remaining weekly budget: if `weekly_trade_count` already 3 in TRADE-LOG.md, note that all picks are watchlist-only.
- `memory/RESEARCH-LOG.md` is overwritten in full each run — the date header is how market-open validates freshness.
