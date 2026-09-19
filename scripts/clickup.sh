#!/bin/bash
# ClickUp task management integration
# Usage: ./scripts/clickup.sh <command> [args]
# Requires CLICKUP_API_TOKEN in .env

CLICKUP_API="https://api.clickup.com/api/v2"

case "$1" in
  list)
    curl -s "$CLICKUP_API/team" \
      -H "Authorization: $CLICKUP_API_TOKEN" | python -m json.tool
    ;;
  task)
    # Create a task: ./scripts/clickup.sh task "Task name" "list_id"
    curl -s -X POST "$CLICKUP_API/list/$3/task" \
      -H "Authorization: $CLICKUP_API_TOKEN" \
      -H "Content-Type: application/json" \
      -d "{\"name\": \"$2\"}" | python -m json.tool
    ;;
  *)
    echo "Usage: $0 {list|task} [args]"
    exit 1
    ;;
esac
