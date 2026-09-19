# Routine: WEEKLY REVIEW (runs ~16:30 ET, Friday only, after close)

**Role:** Compute the week's performance, grade discipline, reset the weekly budget, and propose (not auto-apply) strategy adjustments.

> First complete the Mandatory Startup in `routines/_shared_startup.md`.
> This runs AFTER Friday's daily-summary routine, so EOD state is already reconciled.

## Steps

### 1. Compute weekly stats from `memory/TRADE-LOG.md`
Read the **Closed Trades** and **Open Positions** sections, filter to this week's trades.

- Trades opened this week, trades closed this week.
- Overall: win rate, average R-multiple, total realized P&L ($ and %).
- Best / worst trade, best / worst sector.
- **Tier breakdown** (read `Tier` column from each trade row):

  | Tier | Entries | Wins | Win Rate | Avg R |
  |------|---------|------|----------|-------|
  | EB Pullback | | | | |
  | EB Momentum | | | | |
  | Bullish | | | | |

- Adherence: did any run violate a guardrail? (over weekly budget, position cap, sized wrong, skipped a mandatory exit?)

### 2. Grade the week (A–F)
Grade on **process adherence first, returns second** (Malkan: patience > activity):
- **A:** All rules followed; entries were textbook setups; exits disciplined. (Returns can be flat — zero forced trades is an A.)
- **B:** Rules followed; minor timing/management imperfections.
- **C:** A guardrail was bent, or a thesis was forced in a weak sector.
- **D:** A hard rule was violated (over budget, missed a mandatory RSI<40 exit, oversized).
- **F:** Multiple hard rule violations or significant financial damage from undisciplined trades.

### 3. Sector review
- Review the sector loss tracker in **Weekly Tracker** section of `memory/TRADE-LOG.md`. Any sector paused after 2 consecutive losses → decide whether to re-enable for next week.
  - Re-enable only if the sector ETF has regained **both** weekly RSI > 60 **AND** monthly RSI > 60 (consistent with the global gate).
- Note sectors with momentum to favor next week (ETF in EB Pullback or EB Momentum tier).

### 4. Reset the weekly budget
In the **Weekly Tracker** section of `memory/TRADE-LOG.md`:
- Set `weekly_trade_count` to 0
- Set next week's Monday date
- Clear the entries table
- Keep the sector loss tracker (it persists across weeks until reset by a win or manual re-enable)

### 5. Strategy reflection (propose only — never auto-edit the strategy file)
- If a recurring pattern caused losses (e.g., entering too close to resistance P9 failing, momentum stops too tight), write a concrete suggestion in the weekly log.
- **Tier-specific reflection:** Did Momentum positions (3-bar trailing stop, no fixed T1) outperform Pullback/Bullish positions (fixed T1, partial exit at resistance)? Any pattern worth adjusting?
- **Strategy doc update rule:** If a rule has proven itself across 2+ weeks OR has failed badly, also update `memory/TRADING-STRATEGY.md` in the **same commit** and call out the change explicitly under "Adjustments for Next Week".
- If no change warranted, do NOT touch `memory/TRADING-STRATEGY.md`.

### 6. Append the weekly review to WEEKLY-REVIEW.md
Append the following section to `memory/WEEKLY-REVIEW.md`:

```markdown
## Week of YYYY-MM-DD

### Stats
| Metric | Value |
|--------|-------|
| Entries | N |
| Wins / Losses / Open | N / N / N |
| Win rate | X% |
| Avg R-multiple | X |
| Total realized P&L | $X |
| Best trade | TICKER +$X |
| Worst trade | TICKER -$X |

### Tier Breakdown
| Tier | Entries | Wins | Win Rate | Avg R |
|------|---------|------|----------|-------|
| EB Pullback | | | | |
| EB Momentum | | | | |
| Bullish | | | | |

### Closed Trades This Week
| Ticker | Tier | Entry | Exit | P&L | R | Exit Reason |

### Open Positions at Week End
(snapshot from TRADE-LOG.md Open Positions)

### What Worked
- (3–5 bullets)

### What Didn't Work
- (3–5 bullets)

### Key Lessons
### Adjustments for Next Week
### Overall Grade: X
```

### 7. Close out
- Update `Last Updated` timestamp at the top of `memory/TRADE-LOG.md`.
- Commit + push: `memory/WEEKLY-REVIEW.md`, `memory/TRADE-LOG.md` (budget reset), and `memory/TRADING-STRATEGY.md` if changed.
- **Telegram:** use `telegram_notify.weekly_report(text)` with: grade, # trades (by tier), win rate, weekly P&L, sector notes, budget reset confirmation, any proposal headline.

## Guardrails specific to this routine
- Never auto-modifies the strategy document unless 2+ weeks of evidence (propose, then apply if user-approved, or apply if self-evident pattern over 2+ weeks of data).
- The budget reset is this routine's critical side-effect — confirm it happened in the Telegram message.
- A zero-trade week graded A is a feature, not a bug. Reinforce discipline.
