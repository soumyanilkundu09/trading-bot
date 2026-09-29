# Research Log — Last Run: 2026-09-29 08:30 ET (pre-market)

> Overwritten on every pre-market run. Git history is the archive.
> Market-open routine validates the "Last Run" date matches today before proceeding.

## Account Snapshot
- Equity: $100,000.00 (paper, ACTIVE) | Cash: $100,000.00 | Buying power: $400,000.00
- Open P&L: $0.00 (no open positions) | Weekly entries: 0 / 3 | Open positions: 0 / 5

## Global Gate — FAILED (INDECISIVE/NEGATIVE)

| Indicator | Value | Status |
|-----------|-------|--------|
| SPX Monthly RSI | 73.5 | ✓ > 60 |
| SPX Weekly RSI | 60.65 | ⚠ barely > 60 (was 63.95 on 9/21) |
| VIX | 16.13 | ✓ < 25 (up from 14.87) |
| DXY 20d change | +1.78% | ✓ < 3% |
| 10Y yield | 5.24% (+48bp / 20d) | ✗ SURGING — 19-year high (hit 5.27%), 30Y 5.55% |
| Pre-market futures | S&P -0.07%, Dow -0.14%, Nasdaq flat | ✗ flat/down after Dow -300 on Mon 9/28 |
| Global sentiment | US-Iran uncertainty, energy-driven inflation, ~70% odds of Oct Fed hike | ✗ risk-off |

**Verdict: NOT POSITIVE — no trades today.** On 9/21 the yield was 4.97% with only a soft caution; it has since broken through 5% and surged, weekly RSI has faded to the threshold, and futures/sentiment are negative. That is 2+ bearish signals (Part 3: skip all trades). Sources: [CNBC 9/28](https://www.cnbc.com/2026/09/28/stock-market-today-live-updates.html), [Trading Economics](https://tradingeconomics.com/united-states/government-bond-yield).

## Event Risk
- Fed: hiked 25bp on 9/16; next FOMC Oct 27–28 (none within 3 days), but an October hike is ~70% priced.
- Yield/oil/Iran headlines are the live macro risk.

## Risk Factors
- No held positions → no -7% alerts.
- Universe scan covered 137 tickers (config/universe.json only; S&P 500 constituent fetch has been failing).

## Scanner Output (informational only — NOT actionable, gate failed)
The scanner ran before the gate verdict was finalised. Nothing below is on the entry plan.
- EB Pullback: none. EB Momentum: FTNT, CRWD, TSM, PANW, AAPL, ABBV, PLTR — all scored 2–4/8 (SKIP; near resistance / weak green volume).
- BULLISH tier: 20 hits. Scorer ≥ 6: INTC 10/10, AMGN 8/10, LRCX 6/10 (1% stop, poor R/R). Earnings: LRCX ~Oct 21, INTC Oct 22, AMGN ~Nov 3 (all outside 5-day window).
- If the gate turns POSITIVE again, INTC and AMGN are the first names to re-check.

## Today's Entry Plan
Trade/hold decision: **HOLD (global gate failed — no trades)**
