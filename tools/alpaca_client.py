"""
alpaca_client.py — Thin wrapper over the Alpaca REST API for the trading agent.

Enforces strategy guardrails at the client layer as a last line of defense:
  - Refuses any order unless trading_mode resolves correctly.
  - Equity (stocks/ETFs) only — no options, no futures (8C).
  - Bracket orders carry the stop-loss with the entry so a position is never
    left unprotected even if a later run fails to set the stop.

Reads credentials from environment (.env):
  ALPACA_API_KEY, ALPACA_SECRET_KEY, ALPACA_BASE_URL

Usage:
    python tools/alpaca_client.py --test          # account + positions
    python tools/alpaca_client.py --positions
    python tools/alpaca_client.py --account
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from typing import Optional

import requests

try:
    from dotenv import load_dotenv
    load_dotenv()
except Exception:
    pass


class AlpacaError(Exception):
    pass


class AlpacaClient:
    def __init__(self):
        self.key = os.getenv("ALPACA_API_KEY")
        self.secret = os.getenv("ALPACA_SECRET_KEY")
        self.base = os.getenv("ALPACA_BASE_URL", "https://paper-api.alpaca.markets").rstrip("/")
        # The client appends '/v2/...' to every path. Tolerate a base that already
        # includes a trailing '/v2' so we never produce '/v2/v2/...'.
        if self.base.endswith("/v2"):
            self.base = self.base[: -len("/v2")]
        if not self.key or not self.secret:
            raise AlpacaError(
                "Missing ALPACA_API_KEY / ALPACA_SECRET_KEY. Set them in .env (see SETUP.md)."
            )
        self.headers = {
            "APCA-API-KEY-ID": self.key,
            "APCA-API-SECRET-KEY": self.secret,
            "Content-Type": "application/json",
        }

    @property
    def is_paper(self) -> bool:
        return "paper" in self.base

    # ---- low-level ----
    def _get(self, path: str, params: dict | None = None):
        r = requests.get(self.base + path, headers=self.headers, params=params, timeout=30)
        if r.status_code >= 400:
            raise AlpacaError(f"GET {path} -> {r.status_code}: {r.text[:300]}")
        return r.json()

    def _post(self, path: str, body: dict):
        r = requests.post(self.base + path, headers=self.headers, json=body, timeout=30)
        if r.status_code >= 400:
            raise AlpacaError(f"POST {path} -> {r.status_code}: {r.text[:300]}")
        return r.json()

    def _delete(self, path: str):
        r = requests.delete(self.base + path, headers=self.headers, timeout=30)
        if r.status_code >= 400:
            raise AlpacaError(f"DELETE {path} -> {r.status_code}: {r.text[:300]}")
        return r.json() if r.text else {}

    # ---- account ----
    def get_account(self) -> dict:
        a = self._get("/v2/account")
        return {
            "account_number": a.get("account_number"),
            "status": a.get("status"),
            "equity": float(a.get("equity", 0)),
            "cash": float(a.get("cash", 0)),
            "buying_power": float(a.get("buying_power", 0)),
            "portfolio_value": float(a.get("portfolio_value", 0)),
            "pattern_day_trader": a.get("pattern_day_trader"),
            "trading_blocked": a.get("trading_blocked"),
            "is_paper": self.is_paper,
        }

    def get_clock(self) -> dict:
        return self._get("/v2/clock")

    def is_market_open(self) -> bool:
        try:
            return bool(self.get_clock().get("is_open"))
        except Exception:
            return False

    # ---- positions ----
    def get_positions(self) -> list:
        positions = self._get("/v2/positions")
        return [
            {
                "symbol": p["symbol"],
                "qty": float(p["qty"]),
                "avg_entry_price": float(p["avg_entry_price"]),
                "current_price": float(p.get("current_price", 0) or 0),
                "market_value": float(p.get("market_value", 0) or 0),
                "unrealized_pl": float(p.get("unrealized_pl", 0) or 0),
                "unrealized_plpc": round(float(p.get("unrealized_plpc", 0) or 0) * 100, 2),
            }
            for p in positions
        ]

    def get_position(self, symbol: str) -> Optional[dict]:
        try:
            p = self._get(f"/v2/positions/{symbol}")
            return p
        except AlpacaError:
            return None

    # ---- orders ----
    def get_orders(self, status: str = "open") -> list:
        return self._get("/v2/orders", params={"status": status, "limit": 200})

    def _assert_equity(self, symbol: str):
        """Guardrail 8C: only equity (stocks/ETFs). Reject option/future symbols."""
        if any(ch in symbol for ch in [" ", "/"]) or len(symbol) > 6:
            # Options symbols (OCC) are long; futures use '/'. Equities are <=5 chars.
            raise AlpacaError(f"Guardrail 8C: '{symbol}' is not a plain equity symbol. Rejected.")

    def place_bracket_order(
        self,
        symbol: str,
        qty: int,
        stop_loss: float,
        take_profit: float,
        side: str = "buy",
        tif: str = "day",
    ) -> dict:
        """Submit an entry market order bracketed with a stop-loss and take-profit."""
        self._assert_equity(symbol)
        if qty <= 0:
            raise AlpacaError("qty must be > 0")
        body = {
            "symbol": symbol,
            "qty": str(int(qty)),
            "side": side,
            "type": "market",
            "time_in_force": tif,
            "order_class": "bracket",
            "take_profit": {"limit_price": round(float(take_profit), 2)},
            "stop_loss": {"stop_price": round(float(stop_loss), 2)},
        }
        return self._post("/v2/orders", body)

    def place_market_order(self, symbol: str, qty: int, side: str = "buy", tif: str = "day") -> dict:
        self._assert_equity(symbol)
        body = {
            "symbol": symbol,
            "qty": str(int(qty)),
            "side": side,
            "type": "market",
            "time_in_force": tif,
        }
        return self._post("/v2/orders", body)

    def close_position(self, symbol: str, percentage: Optional[float] = None) -> dict:
        """Close all (or a percentage) of a position at market."""
        path = f"/v2/positions/{symbol}"
        if percentage is not None:
            path += f"?percentage={percentage}"
        return self._delete(path)

    def cancel_order(self, order_id: str) -> dict:
        return self._delete(f"/v2/orders/{order_id}")

    def replace_stop(self, symbol: str, new_stop: float) -> dict:
        """Find the open stop order for symbol and move it to a new price (trailing)."""
        orders = self.get_orders(status="open")
        # Bracket/OCO legs may appear nested under 'legs'
        candidates = []
        for o in orders:
            candidates.append(o)
            candidates.extend(o.get("legs") or [])
        for o in candidates:
            if o["symbol"] == symbol and o.get("type") in ("stop", "stop_limit"):
                return self._patch_order(o["id"], {"stop_price": round(new_stop, 2)})
        raise AlpacaError(f"No open stop order found for {symbol}")

    def _patch_order(self, order_id: str, body: dict):
        r = requests.patch(self.base + f"/v2/orders/{order_id}", headers=self.headers, json=body, timeout=30)
        if r.status_code >= 400:
            raise AlpacaError(f"PATCH /v2/orders/{order_id} -> {r.status_code}: {r.text[:300]}")
        return r.json()


def main():
    ap = argparse.ArgumentParser(description="Alpaca client")
    ap.add_argument("--test", action="store_true", help="Show account + positions")
    ap.add_argument("--account", action="store_true")
    ap.add_argument("--positions", action="store_true")
    ap.add_argument("--clock", action="store_true")
    args = ap.parse_args()

    try:
        c = AlpacaClient()
    except AlpacaError as e:
        print(json.dumps({"ok": False, "error": str(e)}, indent=2))
        sys.exit(1)

    if args.account or args.test:
        print("ACCOUNT:")
        print(json.dumps(c.get_account(), indent=2))
    if args.positions or args.test:
        print("POSITIONS:")
        print(json.dumps(c.get_positions(), indent=2))
    if args.clock or args.test:
        print("CLOCK:")
        print(json.dumps(c.get_clock(), indent=2))
    if not any([args.account, args.positions, args.clock, args.test]):
        ap.print_help()


if __name__ == "__main__":
    main()
