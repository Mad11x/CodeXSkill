#!/usr/bin/env bash
set -euo pipefail

SOURCE_DIR="${SOURCE_DIR:-$HOME/.codex/skills/comment-template}"
REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TARGET_DIR="$REPO_DIR/comment-template"

if [[ ! -d "$SOURCE_DIR" ]]; then
  echo "Source skill not found: $SOURCE_DIR" >&2
  exit 1
fi

mkdir -p "$TARGET_DIR"

rsync -a --delete \
  --exclude '.DS_Store' \
  "$SOURCE_DIR/" "$TARGET_DIR/"

cd "$REPO_DIR"

if git diff --quiet --exit-code -- comment-template && git diff --quiet --cached --exit-code -- comment-template; then
  echo "No skill changes to sync."
  exit 0
fi

git add comment-template
git commit -m "Sync comment-template skill"
git push origin main

echo "Synced comment-template skill to GitHub."
