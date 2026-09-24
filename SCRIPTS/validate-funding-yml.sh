#!/usr/bin/env bash
set -euo pipefail
file="${1:-.github/FUNDING.yml}"
test -f "$file" || { echo "Missing $file"; exit 1; }
grep -Eq '^(github|patreon|open_collective|ko_fi|tidelift|community_bridge|liberapay|issuehunt|polar|buy_me_a_coffee|thanks_dev|custom):' "$file" || { echo "No supported FUNDING.yml key found"; exit 1; }
echo "Funding file looks structurally plausible: $file"
