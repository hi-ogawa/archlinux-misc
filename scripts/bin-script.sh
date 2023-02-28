#!/bin/bash
set -eu -o pipefail

# __USAGE__
#   bash bin-script.sh https://github.com/hi-ogawa/misc/raw/43f4dee863e6e924570b2a7747b1344b0d911a6c/scripts/bin-script.sh bin-script.sh

# __DEPS__
#   curl

# __ARGS__
url="$1"
filename="$2"

dst_dir="$HOME/.local/bin"
dst_path="$dst_dir/$filename"

# download to .local/bin
echo ":: writing to $dst_path"
mkdir -p "$dst_dir"
curl -sSfL "$url" > "$dst_path"

# make it executable
chmod +x "$dst_path"
