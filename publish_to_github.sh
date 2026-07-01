#!/usr/bin/env bash
set -euo pipefail

repo="${1:-tc-lab-report-skill}"
visibility="${2:-private}"

if ! command -v gh >/dev/null 2>&1; then
  echo "GitHub CLI (gh) is required. Install it first, then run this script again." >&2
  exit 1
fi

gh auth status >/dev/null

if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo "Run this script from inside the tc-lab-report-skill repository." >&2
  exit 1
fi

if [ "$visibility" = "public" ]; then
  vis_flag="--public"
else
  vis_flag="--private"
fi

gh repo create "$repo" "$vis_flag" --source=. --remote=origin --push
