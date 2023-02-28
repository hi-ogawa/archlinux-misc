#!/bin/bash
set -eu -o pipefail

# __USAGE__
#   bash translate-clip.bash fr en

# __DEPS__
#   xclip
#   xdg-open

# __ARGS__
src_lang="${1}"
dst_lang="${2}"

text="$(xclip -o)"
if [ -z "$text" ]; then
  echo "no text is selected"
  exit 1
fi

xdg-open "https://translate.google.com/?op=translate&sl=${src_lang}&tl=${dst_lang}&text=${text}"
