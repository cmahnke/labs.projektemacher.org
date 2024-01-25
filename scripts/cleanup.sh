#!/bin/sh

./themes/projektemacher-base/scripts/cleanup.sh
#find content/ -iname '*.glb' -o -iname '*.gltf'
./scripts/cleanup-3d.sh
rm -f content/status.en.md
