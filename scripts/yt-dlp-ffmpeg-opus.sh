#!/bin/bash
set -eu -o pipefail

if [ "$#" -ne 2 ]; then
  echo "Usage: $0 <video-url> <output-name>"
  exit 1
fi

INPUT="$1"
OUTPUT="$2.opus"

TMP_DIR=$(mktemp -d)
TMP_FILE="$TMP_DIR/tmp.webm"
trap 'rm -rf "$TMP_DIR"' EXIT

yt-dlp "$INPUT" --no-playlist -f 'ba[ext=webm]' -o "$TMP_FILE"
ffmpeg -hide_banner -i "$TMP_FILE" -c copy "$OUTPUT"
