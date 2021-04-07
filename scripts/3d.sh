#!/usr/bin/env bash

IMAGE_PREFIX=content/future/3d/
SCRIPT=`dirname $0`/./image-splitter.py

for META in `ls -1 $IMAGE_PREFIX/**/3d-images.json`
do
    DIR=`dirname $META`
    python3 $SCRIPT --image $DIR/front.jpg --coords $DIR/3d-images.json --output jps images gif

done
