#!/usr/bin/env bash

IMAGE_PREFIX=content/future/3d/
IMG_NAME_PREFIX=front
SCRIPT=`dirname $0`/./image-splitter.py

for META in `ls -1 $IMAGE_PREFIX/**/3d-images.json`
do
    DIR=`dirname $META`
    if [ -r "$DIR/$IMG_NAME_PREFIX.jpg" ] ; then
      IMG_FILE="$DIR/$IMG_NAME_PREFIX.jpg"
    elif [ -r "$DIR/$IMG_NAME_PREFIX.jxl" ] ; then
      IMG_FILE="$DIR/$IMG_NAME_PREFIX.jxl"
    fi
    python3 $SCRIPT -s --image $IMG_FILE --coords $DIR/3d-images.json --output jps images gif jpg

done
