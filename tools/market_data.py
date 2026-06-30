"""
market_data.py — Market data + technical analysis engine for the Malkan GFS strategy.

Responsibilities:
  - Fetch OHLCV bars (daily / weekly / monthly) for any US ticker.
  - Compute RSI-14 (Wilder smoothing) on each timeframe.
  - Detect Bullish / Bearish Range Shifts.
  - Detect regular + hidden RSI divergence.
  - Locate support/resistance, CIP consolidation zones, and unfilled gaps.
  - Provide macro snapshot (S&P 500, VIX, DXY, 10Y yield) for the global gate.

Data sources:
  - Primary: Alpaca Market Data API (stocks) when ALPACA keys are present.
  - Fallback / indices (^VIX, ^GSPC, DXY, ^TNX): yfinance (Yahoo Finance).

Designed to be imported by strategy_scorer.py AND runnable standalone:
    python tools/market_data.py --test AAPL
    python tools/market_data.py --macro
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from dataclasses import dataclass, asdict, field
from datetime import datetime, timedelta, timezone
from typing import Optional

import numpy as np
import pandas as pd

try:
    from dotenv import load_dotenv
    load_dotenv()
except Exception:
    pass


# --------------------------------------------------------------------------
# RSI (Wilder's smoothing) — the heart of the whole strategy
# --------------------------------------------------------------------------
def rsi_wilder(closes: pd.Series, period: int = 14) -> pd.Series:
    """Classic Wilder RSI. Returns a Series aligned to `closes`."""
    delta = closes.diff()
    gain = delta.clip(lower=0.0)
    loss = -delta.clip(upper=0.0)

    # Wilder's smoothing = EMA with alpha = 1/period
    avg_gain = gain.ewm(alpha=1 / period, min_periods=period, adjust=False).mean()
    avg_loss = loss.ewm(alpha=1 / period, min_periods=period, adjust=False).mean()

    rs = avg_gain / avg_loss.replace(0.0, np.nan)
    rsi = 100.0 - (100.0 / (1.0 + rs))
    # When avg_loss == 0 -> RSI 100; when avg_gain == 0 -> RSI 0
    rsi = rsi.where(avg_loss != 0, 100.0)
    rsi = rsi.where(avg_gain != 0, rsi)
    rsi.loc[(avg_gain == 0) & (avg_loss != 0)] = 0.0
    return rsi


# --------------------------------------------------------------------------
# Data fetching
# --------------------------------------------------------------------------
def _alpaca_keys() -> Optional[tuple[str, str, str]]:
    key = os.getenv("ALPACA_API_KEY")
    secret = os.getenv("ALPACA_SECRET_KEY")
    data_url = os.getenv("ALPACA_DATA_URL", "https://data.alpaca.markets")
    if key and secret:
        return key, secret, data_url
    return None


def fetch_daily_bars_alpaca(symbol: str, days: int = 800) -> Optional[pd.DataFrame]:
    """Fetch daily bars from Alpaca. Returns DataFrame indexed by date or None."""
    creds = _alpaca_keys()
    if creds is None:
        return None
    key, secret, data_url = creds

    import requests

    end = datetime.now(timezone.utc)
    start = end - timedelta(days=days)
    url = f"{data_url}/v2/stocks/{symbol}/bars"
    params = {
        "timeframe": "1Day",
        "start": start.strftime("%Y-%m-%dT00:00:00Z"),
        "end": end.strftime("%Y-%m-%dT00:00:00Z"),
        "limit": 10000,
        "adjustment": "split",
        "feed": os.getenv("ALPACA_DATA_FEED", "iex"),
    }
    headers = {"APCA-API-KEY-ID": key, "APCA-API-SECRET-KEY": secret}

    rows = []
    while True:
        r = requests.get(url, params=params, headers=headers, timeout=30)
        if r.status_code != 200:
            sys.stderr.write(f"[alpaca] {symbol} HTTP {r.status_code}: {r.text[:200]}\n")
            return None
        data = r.json()
        rows.extend(data.get("bars") or [])
        token = data.get("next_page_token")
        if not token:
            break
        params["page_token"] = token

    if not rows:
        return None

    df = pd.DataFrame(rows)
    df["t"] = pd.to_datetime(df["t"])
    df = df.set_index("t").rename(
        columns={"o": "open", "h": "high", "l": "low", "c": "close", "v": "volume"}
    )
    return df[["open", "high", "low", "close", "volume"]].sort_index()


def fetch_daily_bars_yf(symbol: str, period: str = "3y") -> Optional[pd.DataFrame]:
    """Fallback fetch via yfinance. Works for stocks AND indices (^VIX, ^GSPC)."""
    try:
        import yfinance as yf
    except ImportError:
        sys.stderr.write("[yf] yfinance not installed\n")
        return None
    try:
        t = yf.Ticker(symbol)
        df = t.history(period=period, interval="1d", auto_adjust=True)
        if df is None or df.empty:
            return None
        df = df.rename(
            columns={
                "Open": "open",
                "High": "high",
                "Low": "low",
                "Close": "close",
                "Volume": "volume",
            }
        )
        df.index = pd.to_datetime(df.index).tz_localize(None)
        return df[["open", "high", "low", "close", "volume"]].sort_index()
    except Exception as e:
        sys.stderr.write(f"[yf] {symbol} error: {e}\n")
        return None


def fetch_daily_bars(symbol: str) -> Optional[pd.DataFrame]:
    """Try Alpaca first (for stocks), fall back to yfinance."""
    # Indices use yfinance directly
    if symbol.startswith("^") or "=" in symbol or symbol.endswith(".NYB"):
        return fetch_daily_bars_yf(symbol)
    df = fetch_daily_bars_alpaca(symbol)
    if df is None or df.empty:
        df = fetch_daily_bars_yf(symbol)
    return df


def resample(df: pd.DataFrame, rule: str) -> pd.DataFrame:
    """Resample daily bars to weekly ('W-FRI') or monthly ('ME')."""
    agg = {
        "open": "first",
        "high": "max",
        "low": "min",
        "close": "last",
        "volume": "sum",
    }
    out = df.resample(rule).agg(agg).dropna()
    return out


# --------------------------------------------------------------------------
# Technical pattern detection
# --------------------------------------------------------------------------
def _swing_points(series: pd.Series, lookback: int = 3):
    """Return (low_idx_positions, high_idx_positions) of local swing lows/highs."""
    vals = series.values
    lows, highs = [], []
    for i in range(lookback, len(vals) - lookback):
        window = vals[i - lookback : i + lookback + 1]
        if vals[i] == window.min() and vals[i] < vals[i - 1]:
            lows.append(i)
        if vals[i] == window.max() and vals[i] > vals[i - 1]:
            highs.append(i)
    return lows, highs


def detect_range_shift(rsi: pd.Series, lookback: int = 40) -> dict:
    """
    Detect Bullish (BRS) / Bearish (BeRS) Range Shift in recent RSI.
    BRS: RSI was below 60, broke above 60, now holding >= 40 on pullback.
    BeRS: RSI was above 40, broke below 40, now capped < 60 on bounce.
    """
    recent = rsi.dropna().tail(lookback)
    if len(recent) < 10:
        return {"bullish_range_shift": False, "bearish_range_shift": False}

    vals = recent.values
    broke_above_60 = bool((vals > 60).any())
    broke_below_40 = bool((vals < 40).any())
    current = float(vals[-1])
    recent_min = float(vals[-10:].min())
    recent_max = float(vals[-10:].max())

    # Bullish range shift: established >60 break, now using 40 as support
    brs = broke_above_60 and recent_min >= 38 and current >= 40
    # Bearish range shift: broke below 40, now resistance at 60
    bers = broke_below_40 and recent_max <= 62 and current < 60 and current < 50

    return {
        "bullish_range_shift": bool(brs),
        "bearish_range_shift": bool(bers),
        "broke_above_60": broke_above_60,
        "broke_below_40": broke_below_40,
        "current_rsi": round(current, 2),
    }


def detect_divergence(close: pd.Series, rsi: pd.Series, lookback: int = 40) -> dict:
    """
    Detect regular + hidden bullish/bearish divergence over the recent window.
    Regular bullish: price Lower Low, RSI Higher Low.
    Hidden bullish:  price Higher Low, RSI Lower Low.
    """
    c = close.dropna().tail(lookback)
    r = rsi.reindex(c.index).dropna()
    c = c.reindex(r.index)
    if len(c) < 15:
        return {"regular_bullish": False, "hidden_bullish": False, "bearish": False}

    low_pos, high_pos = _swing_points(c, lookback=3)
    res = {"regular_bullish": False, "hidden_bullish": False, "bearish": False}

    if len(low_pos) >= 2:
        p1, p2 = low_pos[-2], low_pos[-1]
        price_ll = c.iloc[p2] < c.iloc[p1]
        price_hl = c.iloc[p2] > c.iloc[p1]
        rsi_hl = r.iloc[p2] > r.iloc[p1]
        rsi_ll = r.iloc[p2] < r.iloc[p1]
        if price_ll and rsi_hl:
            res["regular_bullish"] = True
        if price_hl and rsi_ll:
            res["hidden_bullish"] = True

    if len(high_pos) >= 2:
        q1, q2 = high_pos[-2], high_pos[-1]
        price_hh = c.iloc[q2] > c.iloc[q1]
        rsi_lh = r.iloc[q2] < r.iloc[q1]
        if price_hh and rsi_lh:
            res["bearish"] = True

    return res


def find_support_resistance(df: pd.DataFrame, lookback: int = 120) -> dict:
    """Identify nearest support below and resistance above current price."""
    recent = df.tail(lookback)
    close = float(df["close"].iloc[-1])
    low_pos, high_pos = _swing_points(recent["close"], lookback=3)

    swing_lows = sorted(recent["low"].iloc[low_pos].tolist()) if low_pos else []
    swing_highs = sorted(recent["high"].iloc[high_pos].tolist()) if high_pos else []

    supports = [s for s in swing_lows if s < close]
    resistances = [r for r in swing_highs if r > close]

    nearest_support = max(supports) if supports else float(recent["low"].min())
    nearest_resistance = min(resistances) if resistances else float(recent["high"].max())

    dist_to_support_pct = (close - nearest_support) / close * 100 if close else 0
    dist_to_resistance_pct = (nearest_resistance - close) / close * 100 if close else 0

    return {
        "close": round(close, 2),
        "nearest_support": round(nearest_support, 2),
        "nearest_resistance": round(nearest_resistance, 2),
        "dist_to_support_pct": round(dist_to_support_pct, 2),
        "dist_to_resistance_pct": round(dist_to_resistance_pct, 2),
    }


def find_gaps(df: pd.DataFrame, lookback: int = 60) -> list:
    """Find unfilled gap-up zones in recent daily bars."""
    recent = df.tail(lookback)
    gaps = []
    lows = recent["low"].values
    highs = recent["high"].values
    closes = recent["close"].values
    idx = recent.index
    current = float(closes[-1])
    for i in range(1, len(recent)):
        prev_high = highs[i - 1]
        cur_low = lows[i]
        if cur_low > prev_high:  # gap up
            gap_bottom, gap_top = prev_high, cur_low
            # unfilled if price never came back down into the gap afterwards
            filled = bool((lows[i:] <= gap_bottom).any())
            if not filled:
                gaps.append(
                    {
                        "date": str(idx[i].date()),
                        "gap_bottom": round(float(gap_bottom), 2),
                        "gap_top": round(float(gap_top), 2),
                        "is_support": gap_top < current,
                    }
                )
    return gaps


def detect_cip(df: pd.DataFrame, window: int = 10) -> dict:
    """Detect consolidation (CIP) — recent low-volatility tight range."""
    recent = df.tail(window)
    rng = (recent["high"].max() - recent["low"].min()) / recent["close"].mean() * 100
    atr = (recent["high"] - recent["low"]).mean() / recent["close"].mean() * 100
    is_cip = bool(rng < 6.0 and atr < 2.0)
    return {
        "is_consolidating": is_cip,
        "range_pct": round(float(rng), 2),
        "avg_daily_range_pct": round(float(atr), 2),
    }


def volume_analysis(df: pd.DataFrame, avg_window: int = 20) -> dict:
    """Analyze the latest candle and the prior candle vs average volume."""
    if len(df) < avg_window + 2:
        avg_window = max(5, len(df) - 2)
    avg_vol = float(df["volume"].iloc[-avg_window - 1 : -1].mean())

    last = df.iloc[-1]
    prev = df.iloc[-2]

    def candle(c):
        body = abs(c["close"] - c["open"])
        rng = max(c["high"] - c["low"], 1e-9)
        return {
            "green": bool(c["close"] > c["open"]),
            "volume": float(c["volume"]),
            "vol_vs_avg": round(float(c["volume"]) / avg_vol, 2) if avg_vol else 0,
            "close_in_upper_half": bool((c["close"] - c["low"]) / rng > 0.5),
            "body_pct_of_range": round(float(body / rng), 2),
        }

    return {
        "avg_volume": round(avg_vol, 0),
        "last_candle": candle(last),
        "prev_candle": candle(prev),
    }


# --------------------------------------------------------------------------
# Full analysis bundle for one ticker
# --------------------------------------------------------------------------
@dataclass
class TickerAnalysis:
    symbol: str
    ok: bool
    price: float = 0.0
    monthly_rsi: float = 0.0
    weekly_rsi: float = 0.0
    daily_rsi: float = 0.0
    daily_rsi_prev: float = 0.0
    range_shift_weekly: dict = field(default_factory=dict)
    range_shift_daily: dict = field(default_factory=dict)
    divergence_daily: dict = field(default_factory=dict)
    support_resistance: dict = field(default_factory=dict)
    gaps: list = field(default_factory=list)
    cip: dict = field(default_factory=dict)
    volume: dict = field(default_factory=dict)
    error: str = ""


def analyze_ticker(symbol: str) -> TickerAnalysis:
    df = fetch_daily_bars(symbol)
    if df is None or len(df) < 60:
        return TickerAnalysis(symbol=symbol, ok=False, error="insufficient data")

    daily = df
    weekly = resample(df, "W-FRI")
    monthly = resample(df, "ME")

    daily_rsi = rsi_wilder(daily["close"])
    weekly_rsi = rsi_wilder(weekly["close"])
    monthly_rsi = rsi_wilder(monthly["close"])

    def last_valid(s: pd.Series) -> float:
        s = s.dropna()
        return round(float(s.iloc[-1]), 2) if len(s) else 0.0

    return TickerAnalysis(
        symbol=symbol,
        ok=True,
        price=round(float(daily["close"].iloc[-1]), 2),
        monthly_rsi=last_valid(monthly_rsi),
        weekly_rsi=last_valid(weekly_rsi),
        daily_rsi=last_valid(daily_rsi),
        daily_rsi_prev=round(float(daily_rsi.dropna().iloc[-2]), 2)
        if len(daily_rsi.dropna()) > 1
        else 0.0,
        range_shift_weekly=detect_range_shift(weekly_rsi),
        range_shift_daily=detect_range_shift(daily_rsi),
        divergence_daily=detect_divergence(daily["close"], daily_rsi),
        support_resistance=find_support_resistance(daily),
        gaps=find_gaps(daily),
        cip=detect_cip(daily),
        volume=volume_analysis(daily),
    )


def get_sector_rsi(etf_symbol: str) -> dict:
    """Return weekly + monthly RSI for a sector ETF."""
    df = fetch_daily_bars(etf_symbol)
    if df is None or len(df) < 60:
        return {"symbol": etf_symbol, "ok": False}
    weekly = resample(df, "W-FRI")
    monthly = resample(df, "ME")
    return {
        "symbol": etf_symbol,
        "ok": True,
        "weekly_rsi": round(float(rsi_wilder(weekly["close"]).dropna().iloc[-1]), 2),
        "monthly_rsi": round(float(rsi_wilder(monthly["close"]).dropna().iloc[-1]), 2),
    }


def macro_snapshot() -> dict:
    """Global gate inputs: S&P 500 RSI, VIX, DXY, 10Y yield."""
    out = {}

    spx = fetch_daily_bars_yf("^GSPC")
    if spx is not None and len(spx) > 60:
        out["sp500_monthly_rsi"] = round(
            float(rsi_wilder(resample(spx, "ME")["close"]).dropna().iloc[-1]), 2
        )
        out["sp500_weekly_rsi"] = round(
            float(rsi_wilder(resample(spx, "W-FRI")["close"]).dropna().iloc[-1]), 2
        )
        out["sp500_price"] = round(float(spx["close"].iloc[-1]), 2)

    vix = fetch_daily_bars_yf("^VIX")
    if vix is not None and len(vix):
        out["vix"] = round(float(vix["close"].iloc[-1]), 2)

    dxy = fetch_daily_bars_yf("DX-Y.NYB")
    if dxy is not None and len(dxy) > 20:
        out["dxy"] = round(float(dxy["close"].iloc[-1]), 2)
        out["dxy_20d_change_pct"] = round(
            float((dxy["close"].iloc[-1] / dxy["close"].iloc[-20] - 1) * 100), 2
        )

    tnx = fetch_daily_bars_yf("^TNX")
    if tnx is not None and len(tnx) > 20:
        # ^TNX is already quoted in percent (e.g. 4.39 == 4.39%).
        out["us_10y_yield"] = round(float(tnx["close"].iloc[-1]), 3)
        out["us_10y_20d_change"] = round(
            float(tnx["close"].iloc[-1] - tnx["close"].iloc[-20]), 3
        )

    return out


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser(description="Malkan market data engine")
    ap.add_argument("--test", metavar="SYMBOL", help="Analyze a single ticker")
    ap.add_argument("--macro", action="store_true", help="Print macro snapshot")
    ap.add_argument("--sector", metavar="ETF", help="Sector ETF RSI")
    args = ap.parse_args()

    if args.macro:
        print(json.dumps(macro_snapshot(), indent=2))
    elif args.sector:
        print(json.dumps(get_sector_rsi(args.sector), indent=2))
    elif args.test:
        a = analyze_ticker(args.test.upper())
        print(json.dumps(asdict(a), indent=2, default=str))
    else:
        ap.print_help()


if __name__ == "__main__":
    main()
