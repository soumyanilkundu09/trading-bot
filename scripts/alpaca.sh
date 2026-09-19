#!/bin/bash
# Thin wrapper — passes all args to the Python Alpaca client
python "$(dirname "$0")/../tools/alpaca_client.py" "$@"
