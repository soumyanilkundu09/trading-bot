"""
telegram_notify.py — Send notifications to the user's Telegram chat.

Reads from environment (.env):
  TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID

Usage (CLI):
    python tools/telegram_notify.py --test
    python tools/telegram_notify.py --message "Hello from the bot"
    echo "piped message" | python tools/telegram_notify.py --stdin

Usage (import):
    from telegram_notify import send_message, trade_alert, guardrail_block
"""

from __future__ import annotations

import argparse
import os
import sys

import requests

try:
    from dotenv import load_dotenv
    load_dotenv()
except Exception:
    pass

API = "https://api.telegram.org"


def _creds() -> tuple[str, str]:
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    if not token or not chat_id:
        raise RuntimeError(
            "Missing TELEGRAM_BOT_TOKEN / TELEGRAM_CHAT_ID. Set them in .env (see SETUP.md)."
        )
    return token, chat_id


def send_message(text: str, parse_mode: str = "Markdown") -> dict:
    """Send a message. Long messages are chunked to Telegram's 4096-char limit."""
    token, chat_id = _creds()
    url = f"{API}/bot{token}/sendMessage"
    out = {}
    for chunk in _chunk(text, 4000):
        r = requests.post(
            url,
            json={"chat_id": chat_id, "text": chunk, "parse_mode": parse_mode,
                  "disable_web_page_preview": True},
            timeout=30,
        )
        if r.status_code >= 400:
            # Retry without markdown if parse error
            r = requests.post(
                url, json={"chat_id": chat_id, "text": chunk}, timeout=30
            )
        out = r.json()
    return out


def _chunk(text: str, size: int):
    if len(text) <= size:
        yield text
        return
    lines = text.split("\n")
    buf = ""
    for ln in lines:
        if len(buf) + len(ln) + 1 > size:
            yield buf
            buf = ""
        buf += ln + "\n"
    if buf:
        yield buf


# --------------------------------------------------------------------------
# Pre-formatted templates
# --------------------------------------------------------------------------
def trade_alert(stock: str, sector: str, score: int, plan: dict, mode: str = "PAPER") -> dict:
    msg = (
        f"🟢 *TRADE EXECUTED* ({mode})\n"
        f"*{stock}*  ·  {sector}\n"
        f"Score: *{score}/108*\n"
        f"━━━━━━━━━━━━━━\n"
        f"Entry: ${plan.get('entry')}\n"
        f"Stop:  ${plan.get('stop_loss')}  ({plan.get('stop_loss_pct')}%)\n"
        f"T1:    ${plan.get('target1')}  (R:R {plan.get('reward_risk_t1')})\n"
        f"T2:    ${plan.get('target2')}\n"
        f"Shares: {plan.get('shares')}  (${plan.get('position_value')}, "
        f"{plan.get('position_pct_of_capital')}% of capital)\n"
        f"Risk: ${plan.get('risk_amount')} ({plan.get('risk_pct_used')}%)"
    )
    return send_message(msg)


def guardrail_block(stock: str, score: int, rule: str, reason: str, next_action: str) -> dict:
    msg = (
        f"🛑 *TRADE BLOCKED — GUARDRAIL*\n"
        f"Stock: *{stock}*\n"
        f"Score: {score}/108\n"
        f"Blocked by: {rule}\n"
        f"Reason: {reason}\n"
        f"Next: {next_action}"
    )
    return send_message(msg)


def daily_summary(portfolio_value: float, day_change_pct: float, open_count: int,
                  weekly_trades: int, positions: list | None = None) -> dict:
    lines = [
        f"📊 *DAILY SUMMARY*",
        f"Portfolio: *${portfolio_value:,.2f}*  ({day_change_pct:+.2f}%)",
        f"Open positions: {open_count}/5",
        f"Weekly trades: {weekly_trades}/3",
    ]
    if positions:
        lines.append("━━━━━━━━━━━━━━")
        for p in positions:
            lines.append(f"{p['symbol']}: {p.get('unrealized_plpc', 0):+.2f}%  (${p.get('unrealized_pl', 0):+.0f})")
    return send_message("\n".join(lines))


def weekly_report(text: str) -> dict:
    return send_message(f"🗓️ *WEEKLY REVIEW*\n{text}")


def main():
    ap = argparse.ArgumentParser(description="Telegram notifier")
    ap.add_argument("--test", action="store_true")
    ap.add_argument("--message", help="Message text to send")
    ap.add_argument("--stdin", action="store_true", help="Read message from stdin")
    args = ap.parse_args()

    try:
        if args.test:
            res = send_message("✅ Trading bot Telegram test — connection OK.")
        elif args.stdin:
            res = send_message(sys.stdin.read())
        elif args.message:
            res = send_message(args.message)
        else:
            ap.print_help()
            return
        print("OK" if res.get("ok") else f"FAILED: {res}")
    except Exception as e:
        print(f"ERROR: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
