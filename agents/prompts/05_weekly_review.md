# Job 5 — WEEKLY REVIEW (runs ~16:15 ET, Friday only, after close)

**Role:** Compute the week's performance, grade discipline, reset the weekly budget, and propose (not auto-apply) strategy adjustments.

> First complete the Mandatory Startup in `agents/prompts/_shared_startup.md`.
> This runs AFTER Friday's daily-summary job, so EOD state is already reconciled.

## Steps

### 1. Compute weekly stats from `state/trade_log.md`
- Trades opened this week, trades closed this week.
- Win rate, average R-multiple, total realized P&L ($ and %).
- Best / worst trade, best / worst sector.
- Adherence: did any run violate a guardrail? (over weekly budget, position cap, sized wrong, skipped a mandatory exit?)

### 2. Grade the week (A–D)
Grade on **process adherence first, returns second** (Malkan: patience > activity):
- **A:** All rules followed; entries were textbook setups; exits disciplined. (Returns can be flat — zero forced trades is an A.)
- **B:** Rules followed; minor timing/management imperfections.
- **C:** A guardrail was bent, or a thesis was forced in a weak sector.
- **D:** A hard rule was violated (over budget, missed a mandatory RSI<40 exit, oversized).

### 3. Sector review
- Review the sector loss tracker. Any sector paused after 2 consecutive losses → decide whether to re-enable for next week (only if the sector ETF has regained weekly RSI > 60).
- Note sectors with momentum to favor next week.

### 4. Reset the weekly budget
- In `state/weekly_tracker.md`: set `weekly_trade_count` to 0, set next week's Monday date, clear the entries table. Keep the sector loss tracker (it persists across weeks until reset by a win or manual re-enable).

### 5. Strategy reflection (propose only — never auto-edit the strategy file)
- If a recurring pattern caused losses (e.g., entering too close to resistance, P9 failures), write a concrete suggestion to the weekly log. Do NOT modify `strategy/Malkan_Trading_Strategy.md` — surface the proposal to the human for approval.

### 6. Write the weekly log
Create `logs/YYYY-MM-DD_weekly_review.md` with all stats, grade, sector notes, and any proposals.

### 7. Close out
- Commit + push.
- **Telegram:** use `telegram_notify.weekly_report(text)` with: grade, # trades, win rate, weekly P&L, sector notes, budget reset confirmation, any proposal headline.

## Guardrails specific to this job
- Never auto-modifies the strategy document. Proposals go to the human.
- The budget reset is this job's critical side-effect — confirm it happened in the Telegram message.
- A zero-trade week graded A is a feature, not a bug. Reinforce discipline.
