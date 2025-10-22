#!/usr/bin/env bash

set -e

IMAGES=$(find content -name '*.svg')

if [ -n "$IMAGES" ] ; then
  IMAGES=$IMAGES ./themes/projektemacher-base/scripts/svgo.sh
else
  echo "No SVG Files found!"
fi
