# Trading Bot — Agent Rulebook

AI trading agent implementing Vishal Malkan's RSI GFS swing strategy. Paper trading by default.

## What This Bot Does
Runs five scheduled routines Mon–Fri that collectively scan the market, execute trades, manage positions, and review performance — all committed to Git so any run can pick up exactly where the last left off.

## Memory Files (read these first)
| File | Read when |
|------|-----------|
| `memory/TRADING-STRATEGY.md` | Every run — the full strategy spec |
| `memory/TRADE-LOG.md` | Every run — open positions, watchlist, weekly tracker, closed trades |
| `memory/RESEARCH-LOG.md` | Market-open run — today's pre-market scan and entry plan |
| `memory/WEEKLY-REVIEW.md` | Weekly review run — cumulative weekly performance log |
| `memory/PROJECT-CONTEXT.md` | New session or onboarding — project overview and key file map |

## Routines
| Slash command | Time ET | Routine file | What it does |
|---------------|---------|-------------|-------------|
| `/pre-market` | 08:30 Mon–Fri | `routines/pre-market.md` | Scan, score, write RESEARCH-LOG.md |
| `/market-open` | 09:45 Mon–Fri | `routines/market-open.md` | Execute trades from today's plan |
| `/midday` | 12:30 Mon–Fri | `routines/midday.md` | Manage positions, trail stops |
| `/daily-summary` | 16:15 Mon–Fri | `routines/daily-summary.md` | EOD snapshot, rescore watchlist |
| `/weekly-review` | 16:30 Fri | `routines/weekly-review.md` | Week stats, reset budget, strategy review |

Every routine starts with `routines/_shared_startup.md` (git pull, read strategy, load config, check mode, load state, verify clock + credentials).

## Python Tools (`tools/`)
- `rsi_scan.py` — 3-tier RSI scanner
- `strategy_scorer.py` — 5-parameter 10-pt entry scorer
- `market_data.py` — price, RSI, volume, support/resistance
- `alpaca_client.py` — Alpaca API wrapper
- `telegram_notify.py` — Telegram alerts

## Non-Negotiable Security Rules
- `.env` is never committed. Secrets in env vars only.
- `trading_mode: "PAPER"` is the default. REAL requires explicit human phrase in session.
- Never place live orders in unattended runs unless `state/REAL_CONFIRMED` exists for today.

## How to Run a Routine Manually
1. Open this project in Claude Code
2. Type `/pre-market` (or whichever routine you want)
3. Claude reads the slash command file, then follows the full routine instructions

## Git Is the Audit Trail
No date-stamped log files. Every agent run commits its output to `memory/` files in-place. `git log` and `git diff` are your audit trail and rollback mechanism.
