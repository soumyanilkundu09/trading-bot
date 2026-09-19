# Project Context

> Static reference for Claude Code sessions. Keep this file updated when key decisions change.

## What This Bot Does
AI trading agent implementing Vishal Malkan's RSI GFS (Grandfather-Father-Son) swing strategy.
Runs five scheduled routines Mon–Fri. Paper trading by default; REAL requires explicit confirmation.

## Key Files
| File | Purpose |
|------|---------|
| `memory/TRADING-STRATEGY.md` | Full strategy spec — read this first on every run |
| `memory/TRADE-LOG.md` | Open positions, watchlist, weekly tracker, closed trades |
| `memory/RESEARCH-LOG.md` | Latest pre-market scan output — overwritten each run |
| `memory/WEEKLY-REVIEW.md` | Cumulative weekly review entries |
| `config/trading_config.json` | Capital, risk %, trading mode (PAPER/REAL) |
| `config/market_config.json` | Risk controls, sector ETFs |
| `config/universe.json` | Stock universe to scan |

## Routines (in order)
| Time ET | Routine | File |
|---------|---------|------|
| 08:30 Mon–Fri | Pre-market scan | `routines/pre-market.md` |
| 09:45 Mon–Fri | Market-open execution | `routines/market-open.md` |
| 12:30 Mon–Fri | Midday position management | `routines/midday.md` |
| 16:15 Mon–Fri | Daily summary + watchlist rescore | `routines/daily-summary.md` |
| 16:30 Fri only | Weekly review | `routines/weekly-review.md` |

## Python Tools (`tools/`)
- `rsi_scan.py` — 3-tier RSI scanner (EB Pullback, EB Momentum, Bullish)
- `strategy_scorer.py` — 5-parameter 10-pt entry scorer
- `market_data.py` — price, RSI, volume, support/resistance data
- `alpaca_client.py` — Alpaca API wrapper (orders, positions, account)
- `telegram_notify.py` — Telegram alerts

## Shell Wrappers (`scripts/`)
- `alpaca.sh` — wraps `python tools/alpaca_client.py`
- `perplexity.sh` — research queries via Perplexity API
- `clickup.sh` — task management integration

## Security Constraints (NEVER override)
- `.env` must never be committed
- Secrets are environment variables: ALPACA_API_KEY, ALPACA_SECRET_KEY, ALPACA_BASE_URL, TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID
- `trading_mode: "PAPER"` default. REAL mode requires human phrase "CONFIRM REAL TRADING" + `state/REAL_CONFIRMED` file for unattended runs
- Financial actions in paper mode only unless explicitly enabled

## Current Status (as of 2026-09-19)
- No open positions
- 0/3 weekly trades used (week of 2026-09-15)
- LLY promoted to Active Trade List — monitor for Monday market-open entry
- Only Healthcare sector (XLV W-RSI 60.76) passes P2 threshold today
