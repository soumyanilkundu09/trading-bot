# SETUP — One-Time Infrastructure Guide

Follow these steps once to take the bot from code to a live (paper) autonomous agent.
Everything defaults to **PAPER trading** — no real money until you deliberately flip it.

---

## 1. Python environment

```bash
cd /path/to/Trading
python -m venv .venv
# Windows (PowerShell):  .venv\Scripts\Activate.ps1
# macOS/Linux:           source .venv/bin/activate
pip install -r requirements.txt
```

Verify:
```bash
python -c "import pandas, numpy, yfinance, requests, dotenv; print('deps OK')"
```

---

## 2. Alpaca paper account + API keys

1. Sign up / log in at **https://app.alpaca.markets**.
2. Top-left, switch to **Paper Trading**.
3. Right panel → **API Keys** → **Generate New Key**.
4. Copy the **Key ID** and **Secret Key** (secret is shown once).
5. Your paper account starts with $100,000 by default — you can reset/adjust balance in the dashboard. Set `total_capital` in `config/trading_config.json` to match what you actually want the bot to treat as capital (e.g. 10000).

---

## 3. Telegram bot + chat ID

1. In Telegram, message **@BotFather** → `/newbot` → follow prompts → copy the **BOT TOKEN**.
2. Open a chat with your new bot and send it any message (e.g. "hi"). This is required before it can message you.
3. Get your **chat ID**: open in a browser (replace `<TOKEN>`):
   `https://api.telegram.org/bot<TOKEN>/getUpdates`
   Find `"chat":{"id":<NUMBER>...}` — that number is `TELEGRAM_CHAT_ID`.

---

## 4. Environment secrets

```bash
cp .env.example .env
```
Edit `.env` and fill in: `ALPACA_API_KEY`, `ALPACA_SECRET_KEY`, `TELEGRAM_BOT_TOKEN`, `TELEGRAM_CHAT_ID`.
Leave `ALPACA_BASE_URL` as the paper endpoint. **`.env` is gitignored — never commit it.**

---

## 5. Validate the tools

```bash
python tools/market_data.py --macro                    # S&P/VIX/DXY snapshot
python tools/market_data.py --test AAPL                # full ticker analysis + RSI
python tools/alpaca_client.py --test                   # account + positions + clock
python tools/strategy_scorer.py --ticker AAPL --sector Technology
python tools/telegram_notify.py --test                 # should ping your phone
```
If all four print sensible JSON / a Telegram ping arrives, you're wired up.

---

## 6. GitHub repo (Git is the bot's memory)

```bash
git init
git add -A
git commit -m "Initial trading bot scaffold"
# Create a PRIVATE repo on GitHub named e.g. trading-bot, then:
git remote add origin https://github.com/<you>/trading-bot.git
git branch -M main
git push -u origin main
```
Confirm `.env` is NOT in the pushed files (it must be ignored).

---

## 7. Schedule the 5 cloud routines

Each routine spins up a fresh Claude Code session that clones the repo, runs one prompt
from `agents/prompts/`, and commits state back. Register them with the `/schedule` skill
(or the scheduled-tasks MCP). Use **UTC** cron; the values below are for EDT (summer).

| Job | Prompt file | Cron (UTC, EDT) | ET time | Days |
|-----|-------------|-----------------|---------|------|
| Pre-market | `agents/prompts/01_pre_market.md` | `30 12 * * 1-5` | 08:30 | Mon–Fri |
| Market-open | `agents/prompts/02_market_open.md` | `45 13 * * 1-5` | 09:45 | Mon–Fri |
| Midday | `agents/prompts/03_midday_scan.md` | `30 16 * * 1-5` | 12:30 | Mon–Fri |
| Daily summary | `agents/prompts/04_daily_summary.md` | `15 20 * * 1-5` | 16:15 | Mon–Fri |
| Weekly review | `agents/prompts/05_weekly_review.md` | `15 20 * * 5` | 16:15 | Fri |

> **DST note:** In winter (EST = UTC−5) add 1 hour to each UTC time. Each prompt also calls
> `alpaca_client --clock` and exits cleanly if the market is closed, so a wrong-by-an-hour
> firing is harmless — it just no-ops.

**Routine prompt template** (what each scheduled job sends to the fresh session):
```
You are the autonomous trading agent. Clone/refresh this repo, then execute the
instructions in agents/prompts/<NN_job>.md exactly. Follow _shared_startup.md first.
Stay in PAPER mode. Commit all state and push when done. Send the Telegram summary.
```

---

## 8. Going live (later — deliberate, manual)

Real trading is intentionally hard to enable:
1. In `config/trading_config.json` set `trading_mode: "REAL"` and `alpaca_base_url` to the live endpoint.
2. Put live Alpaca keys in `.env`.
3. Because cron runs are unattended, the agent suppresses live orders unless a human
   has created a `state/REAL_CONFIRMED` marker for the day (per strategy 8A). Decide your
   own confirmation ritual before trusting it with real capital.
4. **Recommendation:** run paper for several weeks and review the weekly grades first.

---

## Troubleshooting
- **`alpaca_client` 403/401** → keys wrong or using live keys against paper URL (or vice-versa).
- **Empty market data** → free Alpaca data is `iex` feed; set `ALPACA_DATA_FEED=iex`. yfinance is the fallback.
- **Telegram silent** → you must message the bot first; re-check `TELEGRAM_CHAT_ID`.
- **yfinance rate limits** → macro calls hit Yahoo; if throttled, rerun in a minute.
