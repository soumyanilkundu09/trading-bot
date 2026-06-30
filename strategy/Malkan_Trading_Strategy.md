# Vishal Malkan — Multi-Timeframe RSI Swing Trading Strategy
### For AI Trading Agent Implementation

> **Channel:** MoonShot by Vishal & Meghana Malkan (formerly Malkansview)
> **Document Purpose:** Full-depth strategy specification for an AI trading workflow agent
> **Trade Direction Covered:** Long (Buy) trades only
> **Asset Universe:** Global stocks — applicable to any major exchange (NSE India, NYSE/NASDAQ US, LSE UK, ASX Australia, etc.)
> **Market Configuration:** Market-specific parameters (benchmark index, VIX, institutional flow data, sector indices) are configured per target market — see Part 3 and the Market Configuration Table

---

## Part 0 — Market Configuration (AI Agent Setup)

Before executing any scan or evaluation, the AI agent must load the correct market configuration. All market-specific data sources, indices, and timing are resolved from this single `target_market` setting.

```json
{
  "target_market": "NSE",        // Options: "NSE", "US", "LSE", "ASX", "EURONEXT"
  "stock_universe": "F&O",       // Options: "F&O", "TOP500", "SP500", "NASDAQ100", "FTSE100", "ASX200"
  "risk_per_trade_pct": 1.5,     // Percentage of capital risked per trade (1–2 recommended)
  "currency": "INR",             // Trade currency: INR, USD, GBP, AUD, EUR
  "session_timezone": "Asia/Kolkata"  // IANA timezone for session timing
}
```

### Market Configuration Lookup Table

| `target_market` | Benchmark Index | Benchmark RSI Source | VIX Source | VIX Danger Level | Institutional Flow | Pre-Market Signal | Session Timezone |
|---|---|---|---|---|---|---|---|
| `NSE` | Nifty 50 | NSE / TradingView | India VIX (NSE) | > 20 | FII/DII (NSE/SEBI daily) | Gift Nifty futures | Asia/Kolkata |
| `US` | S&P 500 (^GSPC) | Yahoo Finance / TradingView | CBOE VIX (^VIX) | > 25 | COT report / institutional dark pool | S&P 500 E-mini Futures (ES) | America/New_York |
| `LSE` | FTSE 100 (^FTSE) | Yahoo Finance / TradingView | FTSE VIX | > 25 | LSE institutional flow / 13F equivalent | FTSE 100 Futures | Europe/London |
| `ASX` | ASX 200 (^AXJO) | Yahoo Finance / TradingView | S&P/ASX 200 VIX | > 22 | ASX institutional flow | SPI 200 Futures | Australia/Sydney |
| `EURONEXT` | Euro Stoxx 50 (^STOXX50E) | Yahoo Finance / TradingView | VSTOXX (^V2TX) | > 28 | ECB / institutional flow | Euro Stoxx 50 Futures | Europe/Paris |

### Sector Index Mapping

| `target_market` | Technology | Financials | Healthcare | Energy | Consumer | Industrials |
|---|---|---|---|---|---|---|
| `NSE` | Nifty IT | Nifty Bank / Nifty Financial Services | Nifty Pharma | Nifty Energy | Nifty FMCG | Nifty Infrastructure |
| `US` | XLK | XLF | XLV | XLE | XLY / XLP | XLI |
| `LSE` | FTSE Tech Index | FTSE Financials | FTSE Health Care | FTSE Oil & Gas | FTSE Consumer | FTSE Industrials |
| `ASX` | ASX Tech | ASX Financials | ASX Health Care | ASX Energy | ASX Consumer | ASX Industrials |
| `EURONEXT` | Euro Stoxx Tech | Euro Stoxx Banks | Euro Stoxx Health | Euro Stoxx Energy | Euro Stoxx Consumer | Euro Stoxx Industrial |

---

## Part 1 — Foundational Concepts (Malkan Terminology)

Understanding these terms precisely is critical before applying the strategy. These are Vishal Malkan's proprietary definitions — they differ significantly from conventional technical analysis vocabulary.

---

### 1.1 The 60-40 RSI Framework

Malkan **rejects** the conventional 70-30 overbought/oversold RSI interpretation. Instead, he defines three market states purely on RSI levels:

| RSI Zone | Market State | Implication |
|---|---|---|
| RSI **> 60** | **Bullish** | Trend is up; buying pressure dominant |
| RSI **40 – 60** | **Sideways / Indecisive** | No clear trend; avoid fresh positions |
| RSI **< 40** | **Bearish** | Trend is down; selling pressure dominant |

**Key Insight:** In a bullish market, RSI oscillates in the **40–80 range** (uses 40 as support). In a bearish market, RSI oscillates in the **20–60 range** (uses 60 as resistance). This asymmetry is the foundation of the Range Shift concept.

---

### 1.2 Bullish Range Shift (BRS)

**Definition:**
A Bullish Range Shift (BRS) occurs when the RSI indicator **shifts its operating range from the bearish zone (20–60) into the bullish zone (40–80)**. This signals a fundamental change in trend — from bearish/sideways to bullish.

**Qualifying Conditions for a Bullish Range Shift:**
1. RSI was previously oscillating below 60 (bearish/sideways range).
2. RSI **breaks above 60** decisively.
3. On a subsequent pullback, RSI now finds **support near the 40 level** (rather than breaking below it).
4. Price makes a higher low while RSI holds above 40.
5. A **bullish candle** (green, ideally with good body) is formed at or near the RSI 40 support zone.

**What Does NOT Qualify:**
- RSI briefly touching 60 and falling back below — this is a failed range shift, not a BRS.
- RSI at 40 without a prior confirmed break above 60 on higher timeframes.
- A red/bearish candle forming at RSI 40 level (signals continued weakness).

**Signal Strength:**
- Weak BRS: RSI breaks 60 and holds 40 once.
- Strong BRS: RSI breaks 60, pulls back to 40, bounces, and breaks 60 again (confirmation).

**Entry Logic:**
- Monthly RSI > 60 + Weekly RSI > 60 = trend confirmed bullish on higher timeframes.
- Daily RSI pulls back to ~40 zone = short-term correction within a larger uptrend.
- Bullish candle at daily RSI 40 = entry signal.
- Stop-loss = low of that bullish candle.
- Target = RSI 60 zone on daily (price equivalent).

---

### 1.3 Bearish Range Shift (BeRS)

**Definition:**
A Bearish Range Shift (BeRS) occurs when the RSI **shifts its operating range from the bullish zone (40–80) into the bearish zone (20–60)**. This signals a change from bullish/sideways to bearish.

**Qualifying Conditions for a Bearish Range Shift:**
1. RSI was previously oscillating above 40 (bullish range).
2. RSI **breaks below 40** decisively.
3. On a subsequent bounce, RSI now finds **resistance near the 60 level** (cannot cross back above 60).
4. Price makes a lower high while RSI stays below 60.
5. A **bearish candle** (red, ideally with good body) is formed at or near the RSI 60 resistance zone.

**What Does NOT Qualify:**
- RSI briefly dipping below 40 and recovering — this is a false range shift.
- RSI at 60 resistance without a prior break below 40.
- A green/bullish candle forming at RSI 60 level during what appears to be a bounce.

**For the Long Bias Strategy:**
A Bearish Range Shift on any timeframe (Monthly/Weekly/Daily) is a **disqualifier** for long trades. If a BeRS is detected on the Weekly or Monthly, the trade setup should be **rejected entirely**.

---

### 1.4 Bullish Divergence

**Definition:**
Bullish Divergence occurs when **price makes a lower low** but the **RSI makes a higher low**. This is a warning signal that selling momentum is exhausting and a reversal or bounce is imminent.

**Qualifying Conditions for Bullish Divergence:**
1. Price charts a clear **lower low** (LL) — the most recent swing low is below the prior swing low.
2. RSI at the corresponding point shows a **higher low** (HL) — RSI's trough is higher than the prior RSI trough.
3. Both lows should be clearly visible and separated by a meaningful rally in between (not noise).
4. The divergence is **more valid** when it occurs near a key support zone, RSI 40 level, or after a prolonged downtrend.

**Types of Bullish Divergence (Malkan Context):**

| Type | Price | RSI | Reliability |
|---|---|---|---|
| **Regular Bullish Divergence** | Lower Low | Higher Low | Moderate — signals potential reversal |
| **Hidden Bullish Divergence** | Higher Low | Lower Low | High — signals trend continuation in an uptrend |

**Hidden Bullish Divergence** is particularly powerful in Malkan's framework:
- Price makes a **higher low** (already in an uptrend, just correcting).
- RSI makes a **lower low** (momentum appears weak but price holds).
- This confirms the underlying bullish strength; price is likely to resume the uptrend.

**What Does NOT Qualify:**
- Divergence observed over just 2-3 candles (needs at least 2 clear swing points).
- RSI lows that are nearly identical (no meaningful difference).
- Divergence in the middle of a strong downtrend without any other confluence.

---

### 1.5 Bearish Divergence

**Definition:**
Bearish Divergence occurs when **price makes a higher high** but the **RSI makes a lower high**. This signals weakening bullish momentum.

**Qualifying Conditions:**
1. Price makes a clear **higher high** (HH).
2. RSI at the corresponding point shows a **lower high** (LH).
3. Observed near RSI 60–80 zone in a bullish market (resistance area).

**For Long Bias Strategy:**
Bearish divergence appearing on the **Daily chart near a resistance** is a **warning signal** — it suggests the current rally may be exhausting. If Bearish Divergence appears on the entry candle zone, reconsider the trade.

---

### 1.6 Loud Move (High-Volume Directional Candle)

**Definition:**
A "Loud Move" refers to a **significant price move accompanied by exceptionally high volume** — a candle (or cluster of candles) that is meaningfully larger in range AND volume compared to the surrounding candles. It is the market "speaking loudly" about its directional intent.

**Qualifying Conditions for a Bullish Loud Move:**
1. The candle is **green (bullish)**.
2. Volume is **significantly above average** (typically 2x or more the average volume of last 10–20 candles).
3. The candle has a **large real body** (small wicks relative to body), suggesting conviction.
4. Price closes **near the high of the candle** (buyers in control till close).
5. The move occurs at a **key support level, RSI 40 zone, or after a prolonged consolidation**.

**Significance:**
- A bullish loud move at a support level signals institutional/smart money entry.
- It validates the trade setup by confirming demand is genuine, not speculative.
- In the Weekly timeframe, a bullish loud move (High Volume Weekly) is a powerful confirmation.

**Bearish Loud Move:**
- Red candle, high volume, large body, closes near the low.
- Signals institutional selling — avoid long trades if a Bearish Loud Move appears near your entry zone on the daily chart.

---

### 1.7 Adverse Low Move (Prior Red Candle with Low Volume)

**Definition:**
An "Adverse Low Move" refers to a **correction or pullback candle that moves against the primary trend but does so on LOW volume**. In Malkan's framework, this is specifically the **prior day's red candle with low volume** before the entry signal candle.

**Why It Matters:**
- A red candle on **low volume** signals that the selling is **not conviction-based** — sellers are weak.
- It suggests the pullback is a **natural, healthy correction** within the larger bullish trend, not a trend reversal.
- This sets up the ideal scenario: weakness without seller conviction = buyers waiting to step in.

**Qualifying Conditions for Adverse Low Move (Bullish Setup):**
1. The previous day's candle is **red (bearish)**.
2. Volume on that red candle is **below average** (lower than the 10-day or 20-day average volume).
3. Price has not broken below a key support level.
4. RSI has pulled back but is still in the 40–50 zone (not collapsing).

**What Does NOT Qualify:**
- A red candle with high volume (this is a Bearish Loud Move — avoid the trade).
- Multiple consecutive red candles with increasing volume (distribution pattern — avoid).
- A red candle that breaks a key support level (structural damage — avoid).

---

### 1.8 CIP (Consolidation In Price / Critical Inflection Point)

**Definition in Malkan's Context:**
CIP refers to a zone where price **consolidates tightly** (narrow range, low volatility) after a significant move, OR a **critical price level** where supply and demand have historically been balanced.

**Two interpretations:**

1. **Consolidation Pattern (CIP as a zone):**
   - After a strong bullish move, price consolidates in a narrow range.
   - Volume during consolidation is low (drying up).
   - The consolidation acts as a "launch pad" — a breakout from CIP with volume is a strong entry.

2. **Critical Inflection Point (CIP as a price level):**
   - A historical support/resistance level where price has previously reacted significantly.
   - Often coincides with previous swing highs/lows, round numbers, or gap levels.

**Entry at CIP (Daily):**
- Price retraces to a CIP zone on the daily chart.
- RSI is near 40 at this point.
- A bullish candle forms at CIP with rising or above-average volume = entry signal.

---

## Part 2 — The GFS (Grandfather-Father-Son) Framework

This is the foundational multi-timeframe structure that underpins all of Malkan's trade selection.

```
GRANDFATHER (Monthly) → Macro trend direction
FATHER (Weekly)       → Intermediate trend + setup confirmation
SON (Daily)           → Entry timing and precise trigger
```

| Timeframe | Role | RSI Level Required |
|---|---|---|
| **Monthly (Grandfather)** | Global trend filter | RSI **> 60** (bullish macro) |
| **Weekly (Father)** | Intermediate trend + momentum | RSI **> 60** (trending) or **> 40** (correcting in uptrend) |
| **Daily (Son)** | Entry signal | RSI **near 40** (pullback = entry zone) |

**Core Logic:**
> If the grandfather is bullish (Monthly RSI > 60), the father confirms (Weekly RSI > 60), and the son corrects to the 40 RSI zone on the daily — this is the ideal long trade setup.

---

## Part 3 — Global Market Outlook Assessment

**This is the MANDATORY pre-filter. If failed, no trade is taken regardless of other parameters.**

### Market Configuration Table

The RSI logic and parameters are identical across all markets. Only the *data sources* change per market. Configure the agent by selecting the target market before running.

| Market | Benchmark Index | Volatility Index | Institutional Flow Data | Pre-Market Signal | Sector Indices |
|---|---|---|---|---|---|
| **India (NSE)** | Nifty 50 | India VIX | FII/DII data (SEBI/NSE) | Gift Nifty / SGX Nifty | Nifty Bank, Nifty IT, Nifty Pharma, etc. |
| **US (NYSE/NASDAQ)** | S&P 500 / Nasdaq 100 | CBOE VIX (^VIX) | COT report / Dark pool flow | S&P 500 Futures (ES) | XLK, XLF, XLV, XLE (SPDR Sector ETFs) |
| **UK (LSE)** | FTSE 100 | FTSE VIX | Institutional order flow | FTSE 100 Futures | FTSE sector indices |
| **Australia (ASX)** | ASX 200 | ASX VIX / S&P/ASX 200 VIX | Institutional flow | SPI 200 Futures | ASX sector indices (Materials, Financials, etc.) |
| **Europe (Euronext)** | Euro Stoxx 50 | VSTOXX | ECB / Institutional flow | Euro Stoxx Futures | Sector-specific Euro indices |

> **AI Agent Instruction:** At startup, the agent must accept a `target_market` parameter (e.g., `"NSE"`, `"US"`, `"LSE"`) and load the corresponding benchmark index, VIX source, and sector index mappings from the table above.

---

### What Is a Positive Global Market Outlook?

The outlook is assessed in two layers:

**Layer 1 — Home Market (the market where the stock is listed):**

| Indicator | Bullish Signal | Bearish/Indecisive Signal |
|---|---|---|
| **Benchmark Index (Monthly RSI)** | RSI > 60, price above key EMAs | RSI < 60 or < 40 |
| **Benchmark Index (Weekly RSI)** | RSI > 60, making higher highs | RSI falling, structure breaking |
| **Market Volatility Index (VIX equivalent)** | Low and stable (VIX < 15 for US/India) | High or spiking (VIX > 20) |
| **Institutional Flow** | Net positive over last 5 sessions | Net selling or mixed |
| **Pre-Market Futures** | Positive (gap-up signal) | Gap down or flat |

**Layer 2 — Global Macro Context (applicable to all markets):**

| Indicator | Bullish Signal | Bearish/Indecisive Signal |
|---|---|---|
| **US S&P 500 (Monthly RSI)** | RSI > 60, uptrend intact | RSI < 60 or falling |
| **Dollar Index (DXY)** | Stable or weakening (good for equities) | Strengthening sharply (risk-off signal) |
| **US 10-Year Bond Yield** | Stable or declining | Spiking rapidly (equity headwind) |
| **Crude Oil / Commodity Prices** | Stable (no shock) | Extreme spike or crash |
| **Global Risk Sentiment** | Risk-on (equities bid, bonds sold) | Risk-off (equities sold, bonds/gold bid) |

**Decision Rule:**
- **Positive Outlook:** Benchmark Monthly RSI > 60 + Weekly RSI > 60 + VIX low + Institutional flow net positive + US markets stable or bullish.
- **Negative Outlook:** Any 2 of the above are bearish — **SKIP ALL TRADES**.
- **Indecisive Outlook:** Mixed signals — **SKIP ALL TRADES**.

---

## Part 4 — The 12-Parameter Trade Filter System

**Master Rule:**
> The Global Market Outlook must be **POSITIVE** AND **Monthly RSI > 60** before evaluating any other parameter. If this fails, the evaluation stops — no trade.

> If the Global Outlook is satisfied, then **at least 8 out of the remaining 11 parameters** must be satisfied to enter the trade.

---

### Parameter 1 — GLOBAL MARKET OUTLOOK POSITIVE + Monthly RSI > 60
**[MANDATORY — Hard Gate]**

**Definition:** The overall market environment must support bullish risk-taking.

**Checks (market-agnostic):**
- Benchmark index (configured per target market) Monthly RSI > 60 ✓
- US S&P 500 monthly trend: bullish or neutral (not falling) ✓
- Market VIX equivalent < 18 (not in fear zone) ✓
- Institutional flow: net positive over last 5 trading sessions ✓
- No major upcoming macro events (central bank policy meeting, earnings season peak, budget/fiscal announcement) that could disrupt ✓
- Dollar Index (DXY): not in a sharp uptrend (risk-on environment) ✓

**Market-Specific VIX Thresholds:**
| Market | Normal (Bullish) | Caution | Danger (Avoid) |
|---|---|---|---|
| India (India VIX) | < 15 | 15–20 | > 20 |
| US (CBOE VIX) | < 18 | 18–25 | > 25 |
| Europe (VSTOXX) | < 20 | 20–28 | > 28 |

**AI Agent Logic:**
```
IF (Benchmark_Monthly_RSI > 60) AND (Global_Outlook == "POSITIVE") AND (VIX < threshold):
    Proceed to parameter evaluation
ELSE:
    SKIP_TRADE → return "Global outlook negative or indecisive — no trade"
```

---

### Parameter 2 — SECTOR STRONG

**Definition:** The stock's sector must be in a bullish trend. A strong stock in a weak sector is a dangerous trade.

**Checks:**
- Identify the stock's sector using the target market's sector classification ✓
- Sector index or sector ETF Monthly RSI > 60 ✓
- Sector index or sector ETF Weekly RSI > 60 ✓
- Sector outperforming or in line with the benchmark index on relative strength ✓
- No adverse news for the sector (regulatory, policy, global headwinds) ✓

**Market-Specific Sector Reference:**
| Market | Sector Data Source |
|---|---|
| India (NSE) | Nifty sectoral indices (Nifty Bank, Nifty IT, Nifty Pharma, Nifty FMCG, etc.) |
| US (NYSE/NASDAQ) | SPDR Sector ETFs (XLK = Tech, XLF = Financials, XLV = Healthcare, XLE = Energy, etc.) |
| UK (LSE) | FTSE sector indices or iShares UK sector ETFs |
| Australia (ASX) | ASX sector indices (Materials, Financials, Healthcare, etc.) |
| Global / Multi-market | MSCI sector indices or iShares Global Sector ETFs |

**Satisfied:** Sector RSI (weekly) > 60 and sector trend is up.
**Not Satisfied:** Sector RSI < 40 or sector making lower highs.

---

### Parameter 3 — WEEKLY RSI > 60

**Definition:** The stock's Weekly RSI must be above 60, confirming it is in the bullish range on the intermediate timeframe.

**What to Check:**
- Pull up weekly chart → apply RSI-14.
- RSI reading must be **above 60**.
- Confirm it has been above 60 for at least 2–3 weeks (not just a spike).

**Satisfied:** Weekly RSI ≥ 60.
**Not Satisfied:** Weekly RSI < 60 (stock is sideways or bearish on weekly).

**Note:** If Weekly RSI is between 60–80, trend is healthy. If > 80, stock may be extended — check for divergence.

---

### Parameter 4 — WEEKLY RSI > 40

**Definition:** This parameter specifically guards against a stock that has had a Bearish Range Shift on the weekly timeframe.

**Context:** This is most relevant when the Weekly RSI has pulled back from > 60 to near 40–60. The parameter confirms that RSI is **holding above 40** (bullish range intact) and has not broken below 40 (which would signal a Bearish Range Shift on the weekly).

**Satisfied:** Weekly RSI ≥ 40 at all times in the current trend.
**Not Satisfied:** Weekly RSI has broken below 40 (Bearish Range Shift on Weekly — strong sell signal).

> **Note:** If Parameter 3 (Weekly RSI > 60) is satisfied, Parameter 4 is automatically satisfied. Parameter 4 acts as a safety net for borderline cases where Weekly RSI is between 40 and 60.

---

### Parameter 5 — WEEKLY RANGE SHIFT / SUPPORT @ 40

**Definition:** Confirms that the stock has completed a **Bullish Range Shift** on the Weekly timeframe and is now using the 40 RSI level as support.

**Checks:**
- Has Weekly RSI previously broken above 60 (BRS established)? ✓
- Has Weekly RSI since pulled back and found support near 40 at least once? ✓
- Is the stock currently bouncing from this 40 support zone? ✓
- OR: Is the stock currently in the 40–60 consolidation zone but the trend is intact? ✓

**Satisfied:** BRS visible on weekly chart — RSI held 40 as support and bounced, OR RSI is above 60 with no test yet (trend too strong).
**Not Satisfied:** Weekly RSI has broken below 40 and cannot recover above 60.

---

### Parameter 6 — HIGH VOLUME WEEKLY (Bullish Loud Move on Weekly)

**Definition:** There must be evidence of at least one significant high-volume bullish candle on the Weekly timeframe in the recent trend, confirming institutional/smart money participation.

**Checks:**
- Look at the weekly chart over the last 8–12 weeks.
- Identify if there is at least one week where:
  - Candle is **green (bullish)** ✓
  - Volume is **significantly above the 10-week average** (ideally 1.5x–2x or more) ✓
  - Price closed **near the week's high** ✓
- The high-volume week should ideally be part of the breakout or initial trending move, not a recent blow-off top.

**Satisfied:** At least one clear high-volume bullish weekly candle exists in the current trend structure.
**Not Satisfied:** All recent bullish weeks have below-average or average volume (weak trend).

---

### Parameter 7 — DAILY AT SUPPORT / CIP / GAP

**Definition:** On the Daily chart, price must currently be at or near a meaningful support level. This defines the ideal entry zone.

**Three Acceptable Support Types:**

1. **Support Level:** A clearly defined price zone where price has previously bounced multiple times. Price should be testing this zone from above.

2. **CIP (Consolidation In Price):** Price has consolidated in a narrow range for several days (low-volatility sideways movement) and is now at the base/bottom of that consolidation. RSI near 40 in this zone.

3. **Gap Support:** An unfilled price gap on the daily chart (a "gap zone" where price previously gapped up). Price has retraced into the gap zone — this acts as strong magnetic support.

**Checks:**
- Draw horizontal support lines on daily chart ✓
- Mark any unfilled gaps ✓
- Mark any CIP zones (areas of low-ATR sideways movement) ✓
- Current price is within 1–2% of one of these zones ✓

**Satisfied:** Price is at or within 2% of a clear support/CIP/gap zone.
**Not Satisfied:** Price is in mid-air between support and resistance with no clear structure nearby.

---

### Parameter 8 — HIGH GREEN VOLUME (DAILY)

**Definition:** On the entry day (or the most recent completed trading day), there must be a high-volume bullish (green) candle on the daily chart, confirming buying interest at the support level.

**Checks:**
- Daily candle is **green (close > open)** ✓
- Volume on this candle is **above the 20-day average volume** (minimum 1.5x, ideally 2x+) ✓
- Candle body is meaningful (not a doji or spinning top) ✓
- Price closed in the **upper 50% of the candle's range** ✓

**Satisfied:** Green daily candle with above-average volume at/near support.
**Not Satisfied:** Red candle OR green candle with below-average volume (no conviction in the bounce).

> This is the "Bullish Loud Move on Daily" — the daily entry trigger candle. This is the most important single-day signal.

---

### Parameter 9 — NOT NEAR PREVIOUS RESISTANCE

**Definition:** Price must not be approaching or at a significant previous resistance level. Entering near resistance increases the probability of the trade being blocked and reversing.

**Checks:**
- Identify all major resistance zones on the daily chart (previous swing highs, round numbers, all-time highs, 52-week highs).
- Current price should have **at least 8–10% upside** before hitting the nearest meaningful resistance.
- If price is within 2–3% of a major resistance, this parameter is NOT satisfied.

**Market-Specific Resistance Thresholds:**
| Stock Type | Minimum Required Upside to Nearest Resistance |
|---|---|
| Large-cap / High-liquidity (NSE Nifty 50, S&P 500 constituents) | ≥ 6–8% |
| Mid-cap | ≥ 8–10% |
| Small-cap / Low-liquidity | ≥ 10–12% |

**Satisfied:** Nearest significant resistance is at least 8–10% above current price (adjusted for stock type).
**Not Satisfied:** Price is within 3–5% of a strong previous high or resistance cluster.

---

### Parameter 10 — DAILY PREVIOUS CANDLE RED WITH LOW VOLUME (Adverse Low Move)

**Definition:** The candle immediately before the entry signal candle must be **red (bearish) with below-average volume**. This confirms the pullback is a weak, low-conviction correction — not a reversal.

**Checks:**
- The candle just before the entry candle is **red (close < open)** ✓
- Volume on this red candle is **below the 20-day average volume** ✓
- Price did not break below the key support level on this red candle ✓
- RSI on this candle was pulling back toward 40, not breaking below it ✓

**Satisfied:** Prior candle is red with low volume.
**Not Satisfied:** Prior candle is red with high volume (danger — strong selling), OR prior candle is green (no pullback to enter).

> This is the "Adverse Low Move" concept — the market breathed in (corrected weakly) before the entry candle confirms the next move up.

---

### Parameter 11 — DAILY RSI @ 40 (Inflection Point)

**Definition:** The Daily RSI must be near the 40 level — the key inflection point of the bullish range. This is where the GFS strategy dictates an entry.

**Checks:**
- Daily RSI is currently in the range of **38–45** (at or near the 40 support zone) ✓
- RSI has been declining from above 60 (correction) — not declining from below 60 through a Bearish Range Shift ✓
- RSI is showing early signs of turning up (flattening or uptick from the 40 zone) ✓

**Satisfied:** Daily RSI between 38 and 45, approaching or just touched the 40 level.
**Not Satisfied:** RSI has broken below 40 (Bearish Range Shift on daily — avoid), OR RSI is far from 40 (trade is too early or too late).

---

### Parameter 12 — BULLISH RANGE SHIFT / DAILY DIVERGENCE

**Definition:** The Daily chart must show either (a) a completed Bullish Range Shift, OR (b) Bullish Divergence at the RSI 40 zone. Either confirms that the downside momentum is exhausted and a bounce/uptrend continuation is imminent.

**Sub-condition A — Bullish Range Shift on Daily:**
- RSI was previously below 40 (bearish range on daily).
- RSI has now broken above 40 (Bullish Range Shift event confirmed).
- Price is consolidating or pulling back slightly after the BRS.
- RSI pulls back to ~40 (now acting as support) — entry on the bounce candle.

**Sub-condition B — Bullish Divergence on Daily:**
- Price makes a **Lower Low** at the current RSI 40 zone compared to a prior low.
- RSI makes a **Higher Low** (does not confirm the lower price low).
- A bullish candle forms at this lower-low price level, RSI is at 40.
- This divergence signals that sellers are losing strength even as price tests a new low.

**Best Case:** Both BRS and Divergence appear together (extremely strong setup).

**Satisfied:** Either BRS OR Bullish Divergence (or both) visible on daily chart at the 40 RSI zone.
**Not Satisfied:** No range shift visible and no divergence — RSI falling straight down through 40 with no divergence (avoid).

---

## Part 5 — The Master Decision Framework

```
┌─────────────────────────────────────────────────────────────┐
│             TRADE EVALUATION FLOWCHART                       │
└─────────────────────────────────────────────────────────────┘

STEP 1: GLOBAL GATE (MANDATORY)
├── Global Market Outlook = POSITIVE? 
├── Benchmark Index Monthly RSI > 60?  [configured per target market]
│   YES → Proceed to STEP 2
│   NO  → ❌ NO TRADE (stop evaluation)

STEP 2: STOCK SCAN & SECTOR CHECK
├── Stock sector RSI weekly > 60?
│   YES → Proceed to STEP 3
│   NO  → ❌ SKIP STOCK

STEP 3: SCORE THE 10 WEIGHTED PARAMETERS (excluding P1 gate and P8 implicit)
│
├── P2:  Sector Strong                        [✓=12 / ✗=0]
├── P3:  Weekly RSI > 60                      [✓=12 / ✗=0]
├── P4:  Weekly RSI > 40                      [✓=10 / ✗=0]
├── P5:  Weekly Range Shift / Support @ 40    [✓= 6 / ✗=0]
├── P6:  High Green Volume Weekly             [✓= 8 / ✗=0]
├── P7:  Daily at Support / CIP / Gap         [✓=12 / ✗=0]
├── P9:  Not Near Previous Resistance         [✓=14 / ✗=0]
├── P10: Daily Prev Candle Red, Low Volume    [✓=10 / ✗=0]
├── P11: Daily RSI @ 40                       [✓=12 / ✗=0]
└── P12: Bullish Range Shift / Divergence     [✓=12 / ✗=0]

TOTAL SCORE: ___ / 108

STEP 3b: CHECK IMPLICIT CONDITION (P8 — not scored but mandatory for execution)
└── Entry candle: Green AND above-average volume?
    YES → Allow execution   NO → DO NOT execute (wait for next candle)

STEP 4: DECISION
├── Score ≥ 86  → ✅ ENTER TRADE — Full position
├── Score 65–85 → ⚠️  WATCHLIST / Half position — revisit next session
└── Score < 65  → ❌ SKIP STOCK
```

---

## Part 6 — Trade Execution Rules

### Entry
- **Entry Trigger:** Buy at the close of the high-volume green daily candle (Parameter 8), or at the open of the next candle if confirmed after close.
- **Preferred Entry:** At daily support/CIP zone when RSI is 38–45.
- **Avoid chasing:** If price has already moved 3%+ from the support/RSI 40 zone, wait for the next pullback.

### Stop-Loss
- Place stop-loss at the **low of the entry candle** (the high green volume daily candle).
- Alternatively, just below the **key support level** identified in Parameter 7.
- Maximum stop-loss: **5–7% from entry price** (avoid wide stops on lower liquidity stocks).

### Targets
- **Target 1 (Partial Exit — 50%):** RSI 60 on daily chart (the next resistance zone).
- **Target 2 (Trailing — 50%):** Previous swing high OR RSI 80 zone (for strong momentum trades).
- Trail stop-loss to the previous swing low once Target 1 is hit.

### Position Sizing
- Risk per trade: **2% of total capital** (hard limit per Guardrail 8B).
- Max portfolio allocation per position: **5% of total capital** (hard limit per Guardrail 8B).
- Formula: `Position Size = (Capital × 2%) / (Entry Price − Stop-Loss Price)`, capped at `Capital × 5% / Entry Price`.
- Score 65–85 (half position): use 1% risk cap instead of 2%.

### Trade Management
- If price closes below the stop-loss candle's low → **Exit immediately (no averaging down)**.
- If RSI on daily crosses below 40 after entry → **Exit immediately (Bearish Range Shift — trend change)**.
- If Global Market Outlook turns **Negative or Indecisive** after entry → **Exit or reduce position by 50%**.

---

## Part 7 — Disqualifiers (Instant Reject Conditions)

Even if 8+ parameters are satisfied, **immediately reject the trade** if any of the following are true:

| Disqualifier | Reason |
|---|---|
| Market VIX > threshold (see Part 3 table) | Fear in market — avoid |
| Bearish Range Shift on Monthly or Weekly | Macro structure broken |
| Stock making 52-week lows (or multi-year lows) | Strong downtrend, no bottom confirmed |
| Bearish Divergence on Daily near resistance | Momentum exhaustion at entry |
| Sector under regulatory/policy risk | External headwind |
| Red daily candle with HIGH volume on entry day | Bearish Loud Move — sellers in control |
| Stock near 52-week high with RSI > 80 (extended) | Overbought, high risk of reversal |
| Institutional investors (FII/DII/Hedge Funds) net selling 5+ consecutive sessions | Smart money exit |
| Earnings / results announcement within 5 trading days | Event risk (applies to all markets) |
| Major central bank event within 3 days (Fed, RBI, ECB, BoE, RBA) | Macro event risk |
| Currency shock in home market (sharp local currency depreciation > 2% in a week) | Risk-off for foreign investors |

---

## Part 8 — Trading Guardrails & Risk Controls

These are hard rules enforced by the AI agent at all times. They cannot be overridden by a high parameter score or a strong setup. They exist to protect capital and prevent misuse.

---

### 8A — Trading Mode

**Default: PAPER TRADING. Real trading requires an explicit, deliberate toggle.**

| Mode | Behaviour | How to Activate |
|---|---|---|
| **PAPER (default)** | All signals logged and simulated — no real orders placed | Active on every startup automatically |
| **REAL** | Live orders sent to broker API | Set `trading_mode: "REAL"` in config AND type the confirmation phrase below |

**AI Agent Startup Protocol:**
```
ON STARTUP:
  → Load trading_mode from config (default: "PAPER")
  → IF trading_mode == "REAL":
       PROMPT: "You are about to enable REAL trading with live capital.
                Type exactly: CONFIRM REAL TRADING to proceed."
       WAIT for exact phrase match
       IF not matched → revert to PAPER and notify user
  → Log active mode to session log
  → NOTE: REAL mode is session-scoped; reverts to PAPER on next startup
```

---

### 8B — Capital & Position Limits

| Rule | Limit | Example (₹10L / $10K portfolio) |
|---|---|---|
| **Max allocation per position** | 5% of total portfolio | ₹50,000 / $500 max per trade |
| **Risk per trade (max loss)** | 2% of total capital | ₹20,000 / $200 max loss per trade |
| **Max simultaneous open positions** | 5 positions | Never hold more than 5 stocks at once |
| **Max new entries per calendar week** | 3 trades | Resets every Monday; tracked by agent |

**Position Size Calculation (agent applies this formula on every entry):**
```
risk_amount        = total_capital × 0.02
raw_position_size  = risk_amount / (entry_price − stop_loss_price)
max_position_value = total_capital × 0.05
final_shares       = MIN(raw_position_size, FLOOR(max_position_value / entry_price))

GUARDRAIL CHECKS (all must pass before order):
  ✓ final_shares × entry_price ≤ total_capital × 0.05   [5% cap]
  ✓ open_positions_count < 5                             [position limit]
  ✓ weekly_trade_count < 3                               [weekly budget]
  IF any check fails → BLOCK entry, alert user
```

---

### 8C — Instrument Restrictions

| Allowed | Not Allowed |
|---|---|
| Equity cash / delivery (CNC mode) | Futures (stock futures, index futures — any expiry) |
| Sector / index ETFs (delivery only) | Options (calls, puts, spreads, any derivatives) |
| | Intraday / MIS / margin / leveraged trades |
| | Leveraged ETFs (2x, 3x products) |
| | Penny stocks (market cap < $100M / ₹500 Cr) |

**Reason:** This strategy has a 5–20 day swing holding period. Futures carry expiry risk and margin calls incompatible with this timeframe. Options require timing precision this framework does not provide. Leverage amplifies losses beyond the 2% risk-per-trade ceiling.

**Agent Rule:** Before placing any order, verify the instrument type. Reject with log entry if it is not equity delivery.

---

### 8D — Strategy Document Read Requirement

The agent must read the strategy file at the start of every session before any scanning or trading action.

```
AGENT STARTUP SEQUENCE (mandatory order — do not skip steps):

  STEP 1 → Read Malkan_Trading_Strategy.md (this file)
  STEP 2 → Confirm all 12 parameters are parsed
  STEP 3 → Load market config (target_market, stock_universe, timezone)
  STEP 4 → Confirm trading mode (PAPER / REAL) per 8A protocol
  STEP 5 → Load weekly_trade_count (new entries made this Mon–Fri)
  STEP 6 → Load open_positions list
  STEP 7 → Proceed to Pre-Market Routine (Part 10)

IF strategy file is missing or unreadable:
  → HALT all operations immediately
  → Alert: "Strategy file not found. Cannot proceed without strategy definition."
  → Do NOT fall back to assumptions, memory, or defaults
```

---

### 8E — Weekly Trade Budget Tracking

```
WEEKLY BUDGET: 3 new position entries per Monday–Friday week

ON EACH POTENTIAL NEW ENTRY:
  IF weekly_trade_count >= 3:
      LOG:   "Weekly budget exhausted (3/3). Next window: [next Monday]."
      ALERT: user with blocked stock name and parameter score
      ACTION: add to watchlist; re-evaluate next Monday
      → DO NOT ENTER
  ELSE:
      → Proceed with full entry evaluation
      → On confirmed execution: weekly_trade_count += 1

RESET: Every Monday at 00:01 local market timezone (from market config)
```

---

### 8F — Guardrail Violation Alert Format

Any blocked trade must produce a structured alert. Silent skipping is not allowed.

```
╔═══════════════════════════════════════════════════════════╗
║  TRADE BLOCKED — GUARDRAIL VIOLATION                     ║
╠═══════════════════════════════════════════════════════════╣
║  Stock       : [TICKER] — [EXCHANGE]                     ║
║  Score       : [XX] / 108  (setup qualified on score)    ║
║  Blocked by  : [Rule name, e.g. "8C — Instrument Type"]  ║
║  Reason      : [Specific reason]                         ║
║  Next action : [e.g. "Watchlisted for next Monday"]      ║
╚═══════════════════════════════════════════════════════════╝
```

---

## Part 9 — Parameter Weighting for AI Agent

All weights are user-defined and reflect the relative importance of each signal in the trade decision. The mandatory Global Outlook gate (P1) has no score — it is a binary pass/fail gate that must be cleared before any scoring begins.

| Parameter | Weight | Group | Rationale |
|---|---|---|---|
| P2: Sector Strong | **12** | Weekly / Macro | Sector tailwind amplifies individual stock moves |
| P3: Weekly RSI > 60 | **12** | Weekly / Macro | Primary trend confirmation — stock is in bullish range |
| P4: Weekly RSI > 40 | **10** | Weekly / Macro | Guards against a completed Bearish Range Shift on weekly |
| P5: Weekly Range Shift / Support @ 40 | **6** | Weekly / Macro | BRS on weekly = structural bullishness confirmed |
| P6: High Green Volume Weekly | **8** | Weekly / Macro | Institutional participation in the weekly trend |
| P7: Daily at Support / CIP / Gap | **12** | Daily / Entry | Entry zone precision — price at the right level |
| P8: High Green Volume Daily | **—** | Daily / Entry | Implicit confirming condition (subsumed by P7 entry zone + P11 RSI; not separately scored) |
| P9: Not Near Resistance | **14** | Daily / Risk | Risk/reward filter — highest weight; entering near resistance kills R:R |
| P10: Daily Prev Candle Red, Low Volume | **10** | Daily / Entry | Adverse Low Move — confirms sellers are weak |
| P11: Daily RSI @ 40 | **12** | Daily / Entry | GFS Son trigger — the precise inflection point |
| P12: BRS / Daily Divergence | **12** | Daily / Entry | Momentum exhaustion confirmation — reversal/continuation signal |
| **Total** | **108** | | |

> **P8 Note:** High Green Volume on the Daily (entry candle) is a **required qualitative condition** for trade execution. If the entry candle is not green with above-average volume, the trade is not taken regardless of the score. It is not scored separately because it is implicit in executing on the correct setup.

---

### Scoring Thresholds

Total possible score: **108 points** (10 scored parameters).

| Score | Action | Reasoning |
|---|---|---|
| **≥ 86 points** | ✅ **Full position** | ≥ 8 average-weight parameters passing |
| **65 – 85 points** | ⚠️ **Half position / Watchlist** | Strong setup but not fully confirmed — revisit next session |
| **< 65 points** | ❌ **Skip** | Setup is not mature enough |

**Partial score quick reference:**
- All 10 pass → 108 pts (maximum)
- Best 8 of 10 pass (dropping P5:6 + P6:8) → 94 pts → Full position
- Best 8 of 10 pass (dropping P5:6 + P4:10) → 92 pts → Full position
- Weakest 8 of 10 pass (dropping P9:14 + P12:12) → 82 pts → Half position

---

## Part 10 — Scanning Workflow for AI Agent

### Market Session Timing Reference

| Market | Pre-Market Check | Market Open | Market Close |
|---|---|---|---|
| India (NSE) | Before 9:00 AM IST | 9:15 AM IST | 3:30 PM IST |
| US (NYSE/NASDAQ) | Before 9:00 AM ET | 9:30 AM ET | 4:00 PM ET |
| UK (LSE) | Before 7:30 AM GMT | 8:00 AM GMT | 4:30 PM GMT |
| Australia (ASX) | Before 9:45 AM AEST | 10:00 AM AEST | 4:00 PM AEST |

> **AI Agent Instruction:** All time references below use `[MARKET_OPEN - 30 min]` and `[MARKET_CLOSE + 15 min]` as relative anchors. The agent resolves these to wall-clock time based on the configured `target_market`.

---

### Daily Pre-Market Routine (Run at: Market Open − 30 min)

```
1. CHECK GLOBAL OUTLOOK
   → Fetch: Benchmark index Monthly RSI  [configured per target_market]
   → Fetch: Benchmark index Weekly RSI
   → Fetch: S&P 500 / US market close (prior session — global macro anchor)
   → Fetch: Market VIX equivalent  [India VIX / CBOE VIX / VSTOXX — per target_market]
   → Fetch: Institutional flow data  [FII/DII for NSE; COT / dark pool flow for US; etc.]
   → Fetch: Pre-market futures  [Gift Nifty for NSE; ES/NQ futures for US; SPI for ASX]
   → Fetch: DXY (Dollar Index) — relevant for all markets
   → Fetch: US 10-Year yield — macro signal
   → DECISION: Positive / Negative / Indecisive

2. IF POSITIVE → RUN STOCK SCANNER
   → Universe: [configured per target_market]
       NSE India   → NSE F&O stocks (top 200) or Nifty 500 cash
       US Markets  → S&P 500 / Nasdaq 100 / Russell 2000 (configurable)
       UK (LSE)    → FTSE 100 / FTSE 250
       Australia   → ASX 200 / ASX 300
   → Filter 1: Monthly RSI > 60
   → Filter 2: Weekly RSI > 60
   → Filter 3: Daily RSI between 35 and 48
   → Output: Candidate list

3. FOR EACH CANDIDATE → SCORE PARAMETERS P2 to P12
   → Pull: Sector RSI (weekly)  [use market-specific sector index/ETF]
   → Pull: Weekly volume data (last 10 weeks)
   → Pull: Daily chart data (support levels, CIP zones, unfilled gaps)
   → Pull: Daily candle data (today's + previous candle)
   → Pull: RSI values (Monthly, Weekly, Daily)
   → Calculate divergence (price lows vs RSI lows over last 10–20 days)
   → Check distance to nearest resistance
   → Score each parameter → Total score

4. RANK CANDIDATES by weighted score (out of 108)
   → Score ≥ 86  → Active Trade List (Full position eligible)
   → Score 65–85 → Watchlist (revisit next session)
   → Score < 65  → Skip

4b. GUARDRAIL PRE-CHECK (before adding to Active Trade List)
   → weekly_trade_count < 3?           (8E)
   → open_positions_count < 5?         (8B)
   → Instrument is equity delivery?    (8C)
   → Entry candle green + high volume? (P8 implicit)
   IF any check fails → move to Blocked list with alert (8F)

5. FOR ACTIVE TRADE LIST → CALCULATE ENTRY/SL/TARGET
   → Entry: Close of today's session or open of next session
   → Stop-Loss: Low of trigger candle (or key support − 0.5%)
   → Target 1: Daily RSI 60 equivalent price (50% exit)
   → Target 2: Previous swing high (trail remaining 50%)
   → Position Size: apply formula from 8B (2% risk, 5% cap)

6. ALERT → Send trade alert with:
   → Stock name, exchange, sector
   → Parameter scorecard (which passed / failed)
   → Entry price, Stop-Loss, Target 1, Target 2
   → Position size recommendation
```

---

### Post-Market Routine (Run at: Market Close + 15 min)

```
1. UPDATE OPEN POSITIONS
   → Check if any position hit Stop-Loss → mark closed
   → Check if Daily RSI has broken below 40 → exit immediately
   → Check Global Outlook change (VIX spike, institutional flow reversal) → reduce/exit
   → Trail stop-loss to prior swing low if Target 1 achieved

2. RE-SCORE WATCHLIST
   → Re-evaluate each watchlist stock against all 10 weighted parameters
   → If score improves to ≥ 86 → promote to Active Trade List for next session
   → Re-apply all guardrail checks before promoting

3. LOG ALL DECISIONS
   → Date, Market, Exchange, Stock ticker, Sector
   → Parameter scorecard (P1–P12 with pass/fail)
   → Entry, SL, Target, Actual outcome
   → Running P&L and win-rate by market / sector
```

---

## Part 11 — Quick Reference Cheat Sheet

```
╔══════════════════════════════════════════════════════════════════╗
║        MALKAN STRATEGY — QUICK REFERENCE (GLOBAL)               ║
╠══════════════════════════════════════════════════════════════════╣
║ STARTUP: Read strategy.md → Load config → Set PAPER mode        ║
╠══════════════════════════════════════════════════════════════════╣
║ CONFIG:  target_market → benchmark, VIX, sectors, timezone      ║
╠══════════════════════════════════════════════════════════════════╣
║ GATE (mandatory — score nothing if this fails):                  ║
║  • Global Outlook POSITIVE                                       ║
║  • Benchmark Monthly RSI > 60                                    ║
║  • Market VIX below threshold                                    ║
╠══════════════════════════════════════════════════════════════════╣
║ WEIGHTED SCORE (out of 108):                                     ║
║  P2  Sector Strong                    12 pts                     ║
║  P3  Weekly RSI > 60                  12 pts                     ║
║  P4  Weekly RSI > 40                  10 pts                     ║
║  P5  Weekly Range Shift / RSI@40       6 pts                     ║
║  P6  High Green Volume Weekly          8 pts                     ║
║  P7  Daily at Support / CIP / Gap     12 pts                     ║
║  P9  Not Near Resistance              14 pts  ← highest          ║
║  P10 Prev Candle Red + Low Vol        10 pts                     ║
║  P11 Daily RSI @ 40                   12 pts                     ║
║  P12 Bullish RS / Divergence          12 pts                     ║
║                                      ─────                       ║
║  TOTAL                               108 pts                     ║
╠══════════════════════════════════════════════════════════════════╣
║ DECISION:                                                        ║
║  Score ≥ 86  → ✅ Full position (+ P8 green candle check)       ║
║  Score 65–85 → ⚠️  Half position / Watchlist                    ║
║  Score < 65  → ❌ Skip                                           ║
╠══════════════════════════════════════════════════════════════════╣
║ GUARDRAILS (hard limits — cannot be overridden):                 ║
║  • PAPER mode by default; REAL requires explicit confirmation    ║
║  • Max 5% portfolio per position                                 ║
║  • Risk 2% capital per trade (1% for half-position)             ║
║  • Max 3 new trades per week (Mon–Fri, resets Monday)           ║
║  • Equity delivery ONLY — no futures, no options                ║
║  • Read strategy.md before every session                        ║
╠══════════════════════════════════════════════════════════════════╣
║ EXECUTION:                                                       ║
║  ENTRY: Close of trigger candle / next session open              ║
║  SL:    Low of trigger candle                                    ║
║  T1:    Daily RSI 60 zone → exit 50%                            ║
║  T2:    Previous swing high → trail 50%                         ║
╠══════════════════════════════════════════════════════════════════╣
║ EXIT IMMEDIATELY IF:                                             ║
║  • Daily RSI breaks below 40 (Bearish Range Shift)              ║
║  • Market VIX spikes above threshold                             ║
║  • High-volume red candle after entry (Bearish Loud Move)       ║
║  • Institutional flow net seller 3+ consecutive sessions        ║
║  • Benchmark index gap-down > 2% on macro event                 ║
╚══════════════════════════════════════════════════════════════════╝
```

---

## Sources & References

- [A Complete Guide To 5-Star RSI Strategy Ft. Vishal B Malkan — ElearnMarkets](https://blog.elearnmarkets.com/a-5-star-rsi-strategy/)
- [MoonShot by Vishal & Meghana (Malkansview) — YouTube Channel](https://www.youtube.com/channel/UCKxWWqBQZYKTA01GkyQdMHA)
- [RSI Divergence Explained Simply | Vishal B Malkan — YouTube](https://www.youtube.com/watch?v=Wvq1TZh8aF0)
- [3X3 Swing Trading | RSI Divergence | Vishal B Malkan — YouTube](https://www.youtube.com/watch?v=gfr5n6B5QJk)
- [3x3 Swing Trading | Volatility Divergence Strategy | Vishal B Malkan — YouTube](https://www.youtube.com/watch?v=TYB7GJODt-k)
- [Grandfather Father Son Strategy | Vishal Malkan Explanation — YouTube](https://www.youtube.com/watch?v=W1HrDl70Lhk)
- [GFS Strategy by Vishal Malkan RSI Indicator — rajuginni.com](https://rajuginni.com/trading/gfs-strategy/)
- [RSI Range Shift — Vishal Malkan Daily TF Scanner — Chartink](https://chartink.com/screener/rsi-range-shift-vishal-malkan-daily-tf-2)
- [Vishal Malkan Bearish Swing Trade RSI Range Shift Screener — Chartink](https://chartink.com/screener/vishal-malkan-bearish-swing-trade-rsi-range-shift-screener-cash)
- [Grandfather Father Son Strategy — Medium](https://medium.com/@msa.sid/the-grandfather-father-son-strategy-mastering-high-income-trading-skills-88dbc1e60a35)
- [Learn RSI Swing Trading Strategy by Vishal Malkan — Upsurge.club](https://www.upsurge.club/course/rsi-swing-trading-strategy-by-vishal-malkan)
- [Hidden RSI Divergence: A Guide For Swing Trading Success — ElearnMarkets](https://blog.elearnmarkets.com/hidden-rsi-divergence-for-swing-trading/)
- [Divergence Trading Strategy | RSI Series | Vishal B Malkan — YouTube](https://www.youtube.com/watch?v=cQ-y1oULkBw)
