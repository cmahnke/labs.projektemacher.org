#!/usr/bin/env bash

IMAGES=$(find content -maxdepth 4 \( -name '*.jpg' -o -name '*.jxl' \) -a ! -name '*-*') ./themes/projektemacher-base/scripts/iiif.sh
