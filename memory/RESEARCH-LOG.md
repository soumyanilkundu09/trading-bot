# Research Log — Last Run: 2026-11-13 04:45 ET (pre-market)
*(Scheduled unattended run, Friday. Market opens 09:30 ET today. Macro data = Thursday 2026-11-12 close.)*

> This file is **overwritten on every pre-market run**. Git history is the archive.
> Market-open routine validates the "Last Run" date matches today before proceeding.

---

## Account Snapshot
- Equity: $100,000.00 (paper, ACTIVE, `is_paper: true`)
- Cash: $100,000.00 | Buying power: $400,000.00
- Open P&L: $0.00 (no open positions at broker)
- Trading mode: PAPER
- Weekly entries (week of 2026-11-09): 0 / 3 | Open positions: 0 / 5

---

## Global Gate (P1) — ❌ FAILED (INDECISIVE)

| Indicator | Value | Strategy threshold | Status |
|-----------|-------|--------------------|--------|
| SPX Monthly RSI | 75.37 | > 60 | ✓ |
| SPX Weekly RSI | 53.50 | > 60 (Part 3 decision rule) | ✗ Sideways zone (40–60) — was 63.95 on 2026-09-21 |
| VIX | 18.69 | < 18 normal; 18–25 caution; > 25 danger | ⚠ Caution band (not "low") |
| DXY | 103.18 (+1.18% / 20d) | < 3% spike | ✓ |
| US 10Y yield | 5.103% (+0.5bp / 20d) | stable / not surging | ⚠ Above 5% — the level the 09-21 log flagged for gate re-evaluation; elevated but not spiking |
| SPX price | 7,592.40 | — | ~2% below 09-21 level (7,746.96) |

**Verdict: INDECISIVE → no scanning today, no trades.**
Part 3 requires Monthly RSI > 60 **and Weekly RSI > 60** + low VIX for a POSITIVE outlook; "mixed signals → SKIP ALL TRADES". Weekly RSI is in the 40–60 sideways zone and VIX sits in the caution band, with 10Y above 5% as a further headwind — two-plus non-bullish signals, so the gate fails per the strategy (not a near-miss to force through).

> Note: `tools/rsi_scan.py`'s built-in gate uses `SPX_W > 50`, looser than the strategy's > 60. It would have "passed" today. The strategy file is authoritative; consider aligning the scanner threshold.

---

## Event Risk
- Not evaluated in depth (gate failed → routine stops at Step 1). No open positions to protect.
- Next FOMC expected early-mid December — not within 3 days.

---

## Risk Factors
- No held positions → no -7% conditions; no urgent alert.
- Macro: SPX weekly momentum has faded from bullish (>60) to sideways; 10Y > 5%; VIX drifting up into caution.
- **State staleness:** prior committed run was 2026-09-21. TRADE-LOG watchlist scores (ASML, LLY, CRWD, etc.) are ~8 weeks old and should be treated as expired until re-scored on a gate-pass day.
- Environment: Python deps were not pre-installed in this session (installed from `requirements.txt` at run start).

---

## Scanner Output
Not run — global gate failed.

---

## Today's Entry Plan
**Trade/hold decision: HOLD — Global gate FAILED (INDECISIVE). No scanning today, no trades.**
Market-open routine: nothing to execute. Watchlist not re-scored this run.
