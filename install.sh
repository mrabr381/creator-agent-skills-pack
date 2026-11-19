#!/usr/bin/env bash
# Install the Creator Agent Skills Pack into an agent's skills directory.
#
# Usage:
#   ./install.sh                      # Claude Code default: ~/.claude/skills
#   ./install.sh --dir ~/my-skills    # any other agent: point at its skills folder
#   ./install.sh --dir .claude/skills # project-local install (Claude Code)
#
# The script only copies the six skills/ folders. It never needs a network
# connection, an API key, or any dependency.
set -euo pipefail

TARGET="${HOME}/.claude/skills"

while [ $# -gt 0 ]; do
  case "$1" in
    --dir)
      TARGET="$2"
      shift 2
      ;;
    --help|-h)
      echo "Usage: ./install.sh [--dir <skills-directory>]"
      echo "Default target: ~/.claude/skills"
      exit 0
      ;;
    *)
      echo "Unknown option: $1" >&2
      echo "Usage: ./install.sh [--dir <skills-directory>]" >&2
      exit 2
      ;;
  esac
done

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

mkdir -p "$TARGET"
for skill in "$SCRIPT_DIR"/skills/*/; do
  name="$(basename "$skill")"
  cp -r "$skill" "$TARGET/$name"
  echo "Installed $name -> $TARGET/$name"
done

echo "Done. 6 skills installed to $TARGET"
echo "Verify with: ls $TARGET | grep -E 'youtube-outlier-research|repurpose-episode|seo-geo-audit|digital-product-packaging|thumbnail-title-test|privacy-tool-review'"
