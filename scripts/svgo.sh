#!/usr/bin/env bash

set -e

IMAGES=$(find content -name '*.svg') ./themes/projektemacher-base/scripts/svgo.sh
