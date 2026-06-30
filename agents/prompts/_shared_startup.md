# Shared Startup Sequence (referenced by all 5 jobs)

Every scheduled run is a FRESH Claude Code session with no memory of prior runs.
All state lives in Git. Execute this startup sequence at the top of EVERY job before doing job-specific work.

## Mandatory Startup (Guardrail 8D — do not skip, do not reorder)

1. **Read the strategy.** Read `strategy/Malkan_Trading_Strategy.md` in full. If missing/unreadable → HALT, send Telegram alert "Strategy file not found — halting", exit. Do NOT fall back to assumptions.
2. **Load config.** Read `config/market_config.json`, `config/trading_config.json`, `config/universe.json`.
3. **Confirm trading mode (8A).** Read `trading_config.json` → `trading_mode`.
   - If `PAPER` → proceed (default, safe).
   - If `REAL` → this autonomous agent must NOT trade live without a human-typed confirmation phrase in the session. Since cron runs are unattended, **treat REAL as PAPER-blocked**: log "REAL mode requested but no human confirmation in unattended run — orders suppressed", notify Telegram, and continue in read-only/no-order mode unless a prior committed `state/REAL_CONFIRMED` file exists for today.
4. **Load state.** Read `state/portfolio.md`, `state/weekly_tracker.md`, `state/watchlist.md`.
5. **Check the clock.** Run `python tools/alpaca_client.py --clock`. If the US market is closed today (holiday/weekend) and the job requires live action, log "market closed — nothing to do", optionally notify, commit nothing, exit cleanly.
6. **Verify credentials.** If `python tools/alpaca_client.py --account` errors → send Telegram alert with the error and HALT (cannot operate without broker access).

## Mandatory Close-out (every job ends with this)

1. Write a run log to `logs/YYYY-MM-DD_HHMM_<job>.md` summarizing what happened, decisions, and any errors.
2. `git add -A && git commit -m "run: <job> YYYY-MM-DD HH:MM ET"` — commit ALL state + logs.
3. `git push` (if a remote is configured).
4. Send the job's Telegram summary via `python tools/telegram_notify.py` or the template functions.
5. If any step failed, the Telegram message MUST say so explicitly. Silent failure is not allowed.

## Hard Rules (enforced before EVERY order — never overridden by score)
- Equity delivery ONLY. No options, no futures, no leverage, no penny stocks (8C).
- Max 5 open positions (8B).
- Max 5% of equity per position; risk max 2% of capital per trade (8B).
- Max 3 new entries per Mon–Fri week (8E).
- Exit a sector after 2 consecutive failed trades in it.
- A week with zero trades is a valid, correct outcome. Patience > activity.
- Every blocked trade emits a structured guardrail alert (8F). No silent skips.
