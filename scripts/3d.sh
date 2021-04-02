#!/usr/bin/env bash

IMAGE_PREFIX=content/future/3d/

for IMAGE in `ls -1 $IMAGE_PREFIX/**/front.jpg`
do
    DIR=`dirname $IMAGE`
    python3 scripts/image-spliter.py --image $IMAGE --coords $DIR/images.json --output jps

done
