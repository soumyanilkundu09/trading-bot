# Research Log — Last Run: 2026-09-23 08:30 ET (pre-market)

## Account Snapshot
- Equity: $100,000.00
- Cash: $100,000.00
- Buying power: $400,000.00
- Open P&L: $0.00 (no open positions)

## Global Gate
| Indicator | Value | Threshold | Status |
|---|---|---|---|
| S&P 500 Monthly RSI | 74.43 | > 60 | ✅ |
| S&P 500 Weekly RSI | 64.46 | > 60 (healthy) | ✅ |
| CBOE VIX | 14.14 | < 25 (danger), < 18 normal | ✅ |
| DXY 20d change | +1.95% | < 3% | ✅ |
| US 10Y yield | 4.963% (20d Δ +0.259) | not surging | ✅ |

**Verdict: POSITIVE** — full scan authorized.

*Note: yesterday's (2026-09-22) SPX daily bar came back with NaN OHLC from the yfinance fallback feed (index data only; the RSI calc correctly dropped the incomplete row via `dropna()`), so this Monthly/Weekly RSI reflects data through 2026-09-21 close. Not gate-affecting, but flagged for visibility.*

## Event Risk
- **Fed:** Next FOMC meeting is Oct 27–28, 2026 — no Fed event within 3 days. No conflict with the Sept 16 rate hike noted in the prior log.
- No other major macro events (earnings season peak, budget/fiscal announcements) identified within the 3-day window.

## Risk Factors
- No open positions — no positions near -7% stop.
- **Sector weakness:** Industrials (W-RSI 43.86) and Real_Estate remain well below the 60 threshold required for P2 — this blocks CAT, GE, ETN, EQIX on sector grounds. Financials also weak (W-RSI 48.87) — blocks V, C, and (per last log) SCHW/MA, both of which decayed out of any tier this run.
- **Data coverage caveat:** The S&P 500 Wikipedia ticker list fetch returned HTTP 403 (blocked), so today's scan fell back to `config/universe.json` only (137 tickers) instead of the full ~503-name S&P 500 + universe. Scan quality/breadth is reduced today — treat "no signal" for tickers outside universe.json as "not scanned," not "screened out."
- **Scan stability caveat:** A mid-run rescan showed transient inconsistency (a handful of symbols returned NaN prices / different tier membership), traced to an intermittent Alpaca→yfinance fallback picking up the incomplete 2026-09-22 daily bar. Two of three scans converged cleanly; the converged, reproduced result set is what's used below.

## Scanner Output

**Universe:** 137 tickers (universe.json only — see coverage caveat above). Gate passed: true. Errors: 0.

### EXTREMELY BULLISH PULLBACK (3)
| Ticker | Sector | Price | M-RSI | W-RSI | D-RSI | BRS |
|---|---|---|---|---|---|---|
| MRVL | Technology | 262.31 | 69.61 | 64.97 | 63.96 | ✓ |
| TEM | Microcap | 77.17 | 66.62 | 61.70 | 66.48 | ✓ |
| ETN | Industrials | 442.56 | 62.80 | 60.80 | 60.46 | ✓ |

### EXTREMELY BULLISH MOMENTUM (7)
| Ticker | Sector | Price | M-RSI | W-RSI | D-RSI | BRS |
|---|---|---|---|---|---|---|
| FTNT | Technology | 174.25 | 87.46 | 71.73 | 61.14 | |
| CRWD | Technology | 250.05 | 84.31 | 70.27 | 64.87 | ✓ |
| MRK | Healthcare | 151.07 | 78.11 | 67.52 | 62.25 | |
| TSM | Technology | 452.37 | 71.96 | 67.15 | 64.58 | ✓ |
| ANET | Technology | 205.30 | 73.19 | 65.36 | 59.63 | |
| ABBV | Healthcare | 265.29 | 75.30 | 63.17 | 60.52 | |
| PLTR | Technology | 184.97 | 66.07 | 61.55 | 62.49 | |

### BULLISH (15, re-scored — top movers shown)
DDOG, AMGN, NBIS, ASML, V, LLY, MPWR, LRCX, COP, C, TXN, CSCO, CAT, WMT, GE — see Watchlist in TRADE-LOG.md for full scorecards.

### Filtered (passed RSI, blocked by scanner's own near-resistance filter)
QQQ, INTC, SPY, META, NVDA (2.58% to resistance), EQIX (4.44% to resistance), GOOGL.

## Today's Entry Plan

**Trade/hold decision: ENTER 1 trade (AMGN) / rest WATCHLIST.**

Scored all EB_PULLBACK, EB_MOMENTUM, and BULLISH-tier candidates via `strategy_scorer.py`. Six tickers cleared the ≥6/10 (or ≥6/8) score threshold this run: MRVL (7/10), TEM (6/10), TSM (6/8), AMGN (8/10), CSCO (7/10), GE (6/10). Applying the strategy's execution guardrails beyond the raw score (Part 4 P8 hard gate — "will not execute an order unless volume confirms," and Part 6 "avoid chasing >3% from support/RSI-40 zone," and the Adverse Low Move disqualifier for high-volume selling in the pullback) knocks out five of six:

| Ticker | Score | Blocked by | Detail |
|---|---|---|---|
| MRVL | 7/10 | P8 hard gate | Green-day volume 0.88x (below 20-day avg) — no institutional confirmation on the entry candle |
| TSM | 6/8 | P8 hard gate | Green-day volume 0.92x — same volume-confirmation failure |
| TEM | 6/10 | Chase guardrail | Price is 22.14% above the support/BRS zone that triggered the signal — far beyond the 3% max-chase rule (Part 6) |
| CSCO | 7/10 | Adverse Low Move disqualifier | Last 3–4 red candles averaging 1.81x the 20-day volume — conviction selling in the pullback, not a healthy correction |
| GE | 6/10 | P8 hard gate + weak sector | Green volume 0.81x; Industrials sector W-RSI 43.86, well under the 60 threshold |

**AMGN — ENTER ✅** (BULLISH tier, Healthcare, 8/10)
- Thesis: Monthly RSI 64.6, Weekly RSI 58.4 (BRS confirmed — held 40 as support, back above 60 previously), sector strong (Healthcare W-RSI 62.24 > 60), green-day volume confirmed (1.12x 20-day avg), red-candle volume light (0.87x — healthy pullback), 8.56% room to resistance. Only P7 (distance to support/CIP, 8.39%) missed — a Zone 1 (40–60) support-resistance setup, not a precise pullback-to-40 entry, consistent with BULLISH tier characteristics.
- No earnings within 5 trading days (next AMGN report expected early Nov 2026, per public earnings calendars). No Fed event within 3 days (next FOMC Oct 27–28).
- Entry: $410.37 (last close) | Stop: $398.06 (-3.0%, low of entry candle) | Target 1: $445.49 (50% exit, daily RSI-60 zone) | Target 2: $447.30 (trail remaining 50%)
- R/R to T1: 2.85
- Shares: 12 | Position value: $4,924.44 (4.92% of $100k equity — within 5% cap) | Risk: $147.72 (0.15% of capital, well inside the 2% cap since risk-per-share was small relative to the 3% stop distance)
- Order type: Market, bracket order (per `trading_config.json` defaults), day TIF, equity delivery/CNC only
- This would be entry 1 of 3 for the week of 2026-09-21 (0/3 used so far — pre-market does not place orders; market-open executes and updates the tracker).

All other candidates remain on the watchlist (see TRADE-LOG.md) pending a volume-confirmed green day, a pullback closer to support, or sector recovery.
