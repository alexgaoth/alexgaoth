#!/usr/bin/env bash
# Verify every Stack badge resolves AND renders its logo. An unknown simple-icons
# slug still returns HTTP 200 with no icon, so status alone proves nothing.
set -uo pipefail
bad=0
while read -r url; do
  code=$(curl -s -o /dev/null -w "%{http_code}" "$url")
  [ "$code" = "200" ] || { echo "HTTP $code  $url"; bad=1; continue; }
  case "$url" in *"&logo="*)
    curl -s "$url" | grep -q 'data:image' || { echo "NO LOGO  $url"; bad=1; };;
  esac
done < <(python3 "$(dirname "$0")/make_badges.py" | grep -o 'https://img.shields.io/badge/[^)]*')
[ $bad -eq 0 ] && echo "all badges OK"
exit $bad
