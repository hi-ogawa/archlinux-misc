#!/bin/bash
set -eu -o pipefail

# __USAGE__
#   bash bin-script.sh https://github.com/hi-ogawa/misc/raw/master/scripts/bin-script.sh

# __DEPS__
#   curl

# __ARGS__
src="$1"
filename="${2:-"$(basename "$1")"}"

dst_dir="$HOME/.local/bin"
dst_path="$dst_dir/$filename"

echo ":: creating $dst_path"
mkdir -p "$dst_dir"

# copy or download
if [[ -f "$src" ]]; then
  cp -f "$src" "$dst_path"
else
  curl -sSfL "$src" > "$dst_path"
fi

# make it executable
chmod +x "$dst_path"
