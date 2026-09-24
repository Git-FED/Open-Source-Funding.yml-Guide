#!/usr/bin/env bash
set -euo pipefail
for file in README.md GUIDES/sidebar-card-setup.md COMPARISONS/fee-comparison.md; do test -f "$file" || exit 1; done
echo "Core guide files exist. Use lychee or a hosted link checker for network validation."
