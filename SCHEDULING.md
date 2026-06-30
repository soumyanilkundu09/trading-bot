# SCHEDULING — Going Autonomous (when ready)

Everything is built, tested, and pushed. This doc is the final checklist to flip the bot
from manual to autonomous. **Not enabled yet — by design.** Do these steps when you've
watched enough manual runs to trust it.

---

## 1. Secrets for the cloud runs (REQUIRED — chosen approach: scheduler env vars)

The scheduled containers clone the repo but **do not** get your local `.env` (it's gitignored).
Every tool reads credentials from environment variables, so provide these 5 as
**secrets / environment variables in the Claude Code scheduled-task configuration**:

| Env var | Value source |
|---------|--------------|
| `ALPACA_API_KEY` | your Alpaca paper key |
| `ALPACA_SECRET_KEY` | your Alpaca paper secret |
| `ALPACA_BASE_URL` | `https://paper-api.alpaca.markets` |
| `TELEGRAM_BOT_TOKEN` | @ultimateSwingTrading_bot token |
| `TELEGRAM_CHAT_ID` | `8690378235` |

Optional: `ALPACA_DATA_URL=https://data.alpaca.markets`, `ALPACA_DATA_FEED=iex`.

> Do NOT commit these. The tools fall back to `.env` locally and to real env vars in the cloud —
> no code change needed either way.

---

## 2. The five routines

Each routine spins up a fresh Claude Code session, clones the repo, and runs ONE prompt.
Times are **UTC** (cron). The ET column is for summer/EDT; see the DST note.

| # | Job | Prompt file | Cron (UTC) | ET | Days |
|---|-----|-------------|-----------|----|------|
| 1 | Pre-market | `agents/prompts/01_pre_market.md` | `30 12 * * 1-5` | 08:30 | Mon–Fri |
| 2 | Market-open | `agents/prompts/02_market_open.md` | `45 13 * * 1-5` | 09:45 | Mon–Fri |
| 3 | Midday | `agents/prompts/03_midday_scan.md` | `30 16 * * 1-5` | 12:30 | Mon–Fri |
| 4 | Daily summary | `agents/prompts/04_daily_summary.md` | `15 20 * * 1-5` | 16:15 | Mon–Fri |
| 5 | Weekly review | `agents/prompts/05_weekly_review.md` | `15 20 * * 5` | 16:15 | Fri |

### Routine prompt (what each scheduled job sends to the fresh session)
```
You are the autonomous trading agent for github.com/soumyanilkundu09/trading-bot.
Pull the latest repo state, then execute agents/prompts/<NN_job>.md exactly,
following agents/prompts/_shared_startup.md first. Stay in PAPER mode.
Commit all state changes and push to main when done. Send the Telegram summary.
```
Replace `<NN_job>` per row (e.g. `01_pre_market`).

### DST note
The UTC times above are for EDT (Mar–Nov). In EST (Nov–Mar) add 1 hour to each UTC time.
Each prompt also calls `alpaca_client --clock` and exits cleanly if the market is closed,
so a wrong-by-an-hour firing just no-ops — safe but you'll get an off-by-an-hour run.

---

## 3. Recommended rollout
1. **Phase 1:** enable routine #1 (pre-market) only. Watch the daily research logs + Telegram for a few days.
2. **Phase 2:** add #3/#4/#5 (management + reporting) — still no new buys if you skip #2.
3. **Phase 3:** add #2 (market-open) — the only job that opens positions. Now fully autonomous (paper).
4. **Phase 4 (much later, deliberate):** consider live mode per SETUP.md §8. Real orders stay
   suppressed in unattended runs unless you build the `state/REAL_CONFIRMED` ritual.

---

## 4. How to register
Use the `/schedule` skill (or scheduled-tasks tooling) in Claude Code. For each routine, provide:
the cron expression, the routine prompt above, the repo, and the 5 env-var secrets from §1.

When you're ready, just say "schedule routine 1" (or all of them) and I'll set them up.
