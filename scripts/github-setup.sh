#!/bin/sh

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

$SCRIPT_DIR/../themes/projektemacher-base/scripts/github/setup-dependencies.sh
$SCRIPT_DIR/../themes/projektemacher-base/scripts/github/python-dependencies.sh
$SCRIPT_DIR/../themes/projektemacher-base/scripts/github/docker-images.sh
$SCRIPT_DIR/../themes/projektemacher-base/scripts/github/setup-inkscape.sh
$SCRIPT_DIR/../themes/projektemacher-base/scripts/github/dart-sass.sh
