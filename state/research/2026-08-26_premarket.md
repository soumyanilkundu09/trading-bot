# Pre-Market Research — 2026-08-26

## Global Outlook: POSITIVE

| Indicator | Value | Check |
|---|---|---|
| S&P 500 Monthly RSI | 69.87 | > 60 ✓ |
| S&P 500 Weekly RSI | 63.16 | healthy, > 60 ✓ |
| VIX | 15.70 | < 18 normal band ✓ |
| DXY | 99.12 (20d chg -0.89%) | not spiking (> 3% threshold) ✓ |
| US 10Y Yield | 4.654% (20d chg -0.009) | not surging ✓ |

Gate: **PASSED** — proceed to scan.

## Event Risk

- Next FOMC meeting: **September 15–16, 2026** (rate decision Sept 16, 2:00pm ET). More than 3 weeks out — no near-term event-risk flag.

## Scan Summary

- Universe scanned: 100 tickers (`config/universe.json`, full run via `tools/scan.py`).
- Pre-screen passed (Monthly RSI > 60, Daily RSI in band): 16 names — AAPL, CSCO, INTC, TXN, PANW, AXP, C, UNH, CAT, GE, RTX, LMT, NEE, SO, DUK, O.
- Fully scored: all 16.
- **Active Trade List (score ≥ 80): none.**
- **Watchlist (65–79): none.**

### Full scoring detail

| Ticker | Sector | Score | Decision | Disqualifiers |
|---|---|---|---|---|
| PANW | Technology | 64 | Skip (just under watchlist threshold) | — |
| CSCO | Technology | 62 | Skip | — |
| AAPL | Technology | 58 | Skip | — |
| UNH | Healthcare | 58 | Skip | — |
| DUK | Utilities | 58 | Skip | — |
| GE | Industrials | 52 | Disqualified | Last 4 red candles on high volume (1.07x avg) — conviction selling |
| O | Real Estate | 46 | Skip | — |
| INTC | Technology | 48 | Disqualified | Daily RSI < 38, falling through 40 with no BRS/divergence |
| CAT | Industrials | 44 | Skip | — |
| LMT | Industrials | 42 | Disqualified | Bearish Range Shift on Weekly; Bearish Divergence on Daily near resistance; red candles on high volume |
| TXN | Technology | 40 | Disqualified | Daily RSI < 38, falling through 40 with no BRS/divergence |
| RTX | Industrials | 40 | Disqualified | Bearish Divergence on Daily near resistance; red candles on high volume |
| NEE | Utilities | 38 | Disqualified | Daily RSI < 38, falling through 40 with no BRS/divergence |
| AXP | Financials | 36 | Disqualified | Bearish Range Shift on Weekly; red candles on high volume |
| C | Financials | 36 | Skip | — |
| SO | Utilities | 28 | Disqualified | Bearish Loud Move; red candles on high volume; Daily RSI < 38 falling through 40 |

## Notes for market-open

- No candidates cleared the ≥65 watchlist bar today. Closest misses: **PANW (64)** and **CSCO (62)**, both Technology — worth a quick re-check at daily-summary in case today's session firms up P8/P10.
- Weekly trade budget: 0/3 used. Open positions: 0/5. No capacity constraints — the null result is purely a setup-quality gap, not a guardrail block.
- No sector-wide disqualification observed; misses were idiosyncratic (weekly BRS breaks, high-volume red candles / distribution, RSI falling through 40 without divergence).
