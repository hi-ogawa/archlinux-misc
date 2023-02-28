#!/bin/bash
set -eu -o pipefail

# __USAGE__
#   bash translate-ocr.sh fra eng

# __DEPS__
#   gnome-screenshot
#   mogrify
#   tesseract
#   xdg-open
#   file

# __ARGS__
src_lang="$1"
dst_lang="$2"

# cf. https://github.com/tesseract-ocr/tessdoc/blob/master/ImproveQuality.md
function Preprocess() {
    local img_file="$1"
    local gray_level

    # Gray scale
    mogrify -set colorspace Gray "$img_file"

    # Enhance contrast
    mogrify -auto-level "$img_file"

    # Detect light/dack background
    gray_level=$(convert "$img_file" -resize 1x1 -format '%[fx:int(100 * u)]' info:)

    # Invert if dark background
    if test "$gray_level" -lt 50; then
        mogrify -negate "$img_file"
    fi

    # Enlarge image
    mogrify -modulate 100,0 -resize 400% "${img_file}"
}

function Main() {
    local text=""
    local img_file

    img_file=$(mktemp --suffix=.png)

    # shellcheck disable=SC2064
    trap "rm '${img_file}'" EXIT

    # Take screenshot
    gnome-screenshot -a -f "$img_file"
    if [ "$(file -b "$img_file")" = "empty" ]; then
        echo "gnome-screenshot failed"
        exit 1
    fi

    # Preprocess image to improve OCR accuracy
    Preprocess "$img_file"

    # Run OCR
    text=$(tesseract "${img_file}" stdout -l "${src_lang}")
    if [ -z "${text}" ]; then
        echo "tesseract failed"
        exit 1
    fi

    # Open google translate
    xdg-open "https://translate.google.com/?op=translate&sl=${src_lang:0:2}&tl=${dst_lang:0:2}&text=${text}"
}

Main
