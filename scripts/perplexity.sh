#!/bin/bash
# Research queries via Perplexity API
# Usage: ./scripts/perplexity.sh "query text"
# Requires PERPLEXITY_API_KEY in .env

if [ -z "$1" ]; then
  echo "Usage: $0 \"query text\""
  exit 1
fi

curl -s "https://api.perplexity.ai/chat/completions" \
  -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
  -H "Content-Type: application/json" \
  -d "{\"model\": \"sonar\", \"messages\": [{\"role\": \"user\", \"content\": \"$1\"}]}" \
  | python -c "import sys, json; data=json.load(sys.stdin); print(data['choices'][0]['message']['content'])"
