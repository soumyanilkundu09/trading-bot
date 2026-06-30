# Autonomous Trading Bot — Claude *is* the Bot

A fully autonomous, 24/7 swing-trading agent for **US equities** built on Vishal Malkan's
multi-timeframe RSI **GFS (Grandfather-Father-Son)** strategy. There is no long-running Python
process — **every scheduled run is a fresh Claude Code session** that reads Git-committed state,
decides, places orders via Alpaca (paper), writes new state, commits, and notifies you on Telegram.

## Design principles
- **Stateless runs** — each firing is independent; a failure self-heals on the next tick.
- **Git as memory** — all state is markdown committed to `main`. Free versioning, diffs, audit trail.
- **Hard rules as gates** — guardrails are enforced in code (`strategy_scorer.py`, `alpaca_client.py`) before any order, not left to interpretation.

## Daily rhythm (5 cron jobs, weekdays, US/Eastern)
```
08:30  Pre-market    → assess global gate, scan universe, write ranked trade ideas   (no orders)
09:45  Market-open   → execute qualified trades, attach stops + targets               (only job that buys)
12:30  Midday        → cut losers (RSI<40 / stop), trail winners, partial T1 exits     (manages)
16:15  Daily summary → reconcile vs Alpaca, re-score watchlist, Telegram recap         (reports)
16:15  Weekly review → Friday only: stats, grade, reset weekly budget, proposals       (reflects)
```

## Repository layout
```
config/      market_config.json · trading_config.json · universe.json
strategy/    Malkan_Trading_Strategy.md   ← the bible; read at the start of every run
tools/       market_data.py · alpaca_client.py · strategy_scorer.py · telegram_notify.py
agents/prompts/  _shared_startup.md + 01..05 job prompts (one per cron job)
state/       portfolio.md · watchlist.md · weekly_tracker.md · trade_log.md · research/
logs/        per-run logs, committed each firing
SETUP.md     one-time infrastructure guide
```

## The strategy in one breath
Global gate (S&P monthly RSI > 60, VIX calm) **must** pass. Then each candidate is scored on
**10 weighted parameters (108 pts)**: monthly/weekly/daily RSI alignment, sector strength,
support/CIP/gap entry zone, distance from resistance, volume confirmation, range-shift/divergence.
**≥86 → full position, 65–85 → half/watchlist, <86 disqualified → skip.** Long-only, equity-only.

## Guardrails (non-negotiable, code-enforced)
- PAPER mode by default; live requires deliberate manual enablement.
- No options, no futures, no leverage, no penny stocks — equity delivery only.
- ≤ 5 open positions · ≤ 5% equity per position · ≤ 2% capital risk per trade.
- ≤ 3 new entries per week · exit a sector after 2 consecutive losses.
- Patience > activity — a zero-trade week can be the right answer.

## Quick start
See **[SETUP.md](SETUP.md)**. TL;DR: `pip install -r requirements.txt`, fill `.env`,
validate the four tools, push to a private GitHub repo, register the 5 routines via `/schedule`.

## Tools (also runnable by hand)
```bash
python tools/market_data.py --macro
python tools/market_data.py --test NVDA
python tools/strategy_scorer.py --ticker NVDA --sector Technology
python tools/alpaca_client.py --test
python tools/telegram_notify.py --test
```

> ⚠️ Educational/personal-automation project. Not financial advice. Trading risks real capital —
> validate thoroughly in paper mode before considering live use.
