#!/usr/bin/env bash
# Verify every Stack badge resolves, renders its logo, and links to a real Wikipedia
# article. An unknown simple-icons slug still returns HTTP 200 with no icon, so
# status alone proves nothing.
set -uo pipefail
bad=0
while read -r url; do
  code=$(curl -s -o /dev/null -w "%{http_code}" "$url")
  [ "$code" = "200" ] || { echo "HTTP $code  $url"; bad=1; continue; }
  case "$url" in *"&logo="*)
    curl -s "$url" | grep -q 'data:image' || { echo "NO LOGO  $url"; bad=1; };;
  esac
done < <(python3 "$(dirname "$0")/make_badges.py" | grep -o 'https://img.shields.io/badge/[^)]*')
# Each badge's Wikipedia title must be a real article, not missing or a
# disambiguation page. Query in batches: one request per link gets HTTP 429.
python3 -B - "$(dirname "$0")" <<'EOF' || bad=1
import json, sys, urllib.parse, urllib.request
sys.path.insert(0, sys.argv[1]); from make_badges import GROUPS
titles = sorted({w for _, items in GROUPS for _, _, w in items})
bad = False
for i in range(0, len(titles), 50):
    q = urllib.parse.urlencode({"action": "query", "titles": "|".join(titles[i:i+50]), "redirects": 1,
                                "prop": "pageprops", "ppprop": "disambiguation", "format": "json"})
    req = urllib.request.Request("https://en.wikipedia.org/w/api.php?" + q,
                                 headers={"User-Agent": "alexgaoth-readme-check/1.0"})
    for p in json.load(urllib.request.urlopen(req))["query"]["pages"].values():
        if "missing" in p or "disambiguation" in p.get("pageprops", {}):
            print("NO WIKI  " + p["title"]); bad = True
sys.exit(bad)
EOF
[ $bad -eq 0 ] && echo "all badges OK"
exit $bad
