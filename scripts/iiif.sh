#!/usr/bin/env bash

TILE_SIZE=512
IIIF_STATIC_CMD=""
OUTPUT_PREFIX=""
DEFAULT_URL_PREFIX="."
IMAGE_PREFIX=content

# This only works if there are no generated IIIF directories, otherwise these will be processed as well
#shopt -s globstar

if [ -z "$SKIP_IIIF" ] ; then

    if [[ -z "$URL_PREFIX" ]] ; then
        echo "URL_PREFIX is not set, setting it to '$DEFAULT_URL_PREFIX'"
        URL_PREFIX="$DEFAULT_URL_PREFIX"
    else
        if [ `echo "$URL_PREFIX" | rev| head -c 1` = "/" ] ; then
            URL_PREFIX=`echo $URL_PREFIX |sed 's/.$//'`
            echo "Removed tailing slash: $URL_PREFIX"
        fi
    fi

    if ! command -v vips &> /dev/null
    then
        echo "vips could not be found, using python"
        IIIF_STATIC_CMD="iiif_static.py"
    else
        VIPS_VERSION=`vips -v | cut -d '-' -f 2`
        VIPS_MAJOR=`echo $VIPS_VERSION | cut -d . -f 1`
        VIPS_MINOR=`echo $VIPS_VERSION | cut -d . -f 2`

        if [[ $VIPS_MAJOR -lt 8 && $VIPS_MINOR -lt 10 ]] ; then
            echo "vips is to old, falling back to python"
            IIIF_STATIC_CMD="iiif_static.py"
        else
            IIIF_STATIC_CMD="vips"
        fi

    fi

    echo "Processing files in '$IMAGE_PREFIX'"
    # IIFF
    for IMAGE in `ls -1 $IMAGE_PREFIX/**/**/**/front*.jpg $IMAGE_PREFIX/**/front*.jpg $IMAGE_PREFIX/**/back*.jpg $IMAGE_PREFIX/**/page*.jpg $IMAGE_PREFIX/**/front.jpg $IMAGE_PREFIX/**/end.jpg $IMAGE_PREFIX/**/title.jpg $IMAGE_PREFIX/**/back.jpg $IMAGE_PREFIX/**/*-recto.jpg $IMAGE_PREFIX/**/*-verso.jpg $IMAGE_PREFIX/**/img*.jpg $IMAGE_PREFIX/**/**/*.jpg`
    do
        OUTPUT_DIR=`dirname $IMAGE`
        IIIF_DIR=`basename $IMAGE .jpg`
        if [ $OUTPUT_PREFIX = ""] ; then
            TARGET=$OUTPUT_DIR/$IIIF_DIR
        else
            TARGET=$OUTPUT_PREFIX/$OUTPUT_DIR/$IIIF_DIR
            mkdir -p $TARGET
        fi
        echo "Processing $IMAGE..."

        if [ "$URL_PREFIX" = "." ] ; then
            IIIF_ID="$URL_PREFIX"
        else
            IIIF_ID="$URL_PREFIX/$(echo $OUTPUT_DIR |cut -d'/' -f2-)"
            echo "Setting IIIF identifier to '$IIIF_ID'"
        fi

        echo "Generating IIIF files for $IMAGE in directory $OUTPUT_DIR, IIIF directory $IIIF_DIR ($TARGET)"
        if [ $IIIF_STATIC_CMD = "vips" ] ; then
            vips dzsave $IMAGE $TARGET -t $TILE_SIZE --layout iiif --id "$IIIF_ID"
            mkdir -p  $TARGET/full/full/0/
            cp $IMAGE $TARGET/full/full/0/default.jpg
        elif [ $IIIF_STATIC_CMD = "iiif_static.py" ] ; then
            iiif_static.py -d $TARGET -i "$IIIF_ID" -t $TILE_SIZE $IMAGE
        fi
        if [[ -n "$CHOWN_UID" ]] ; then
            echo "Changing owner of $TARGET to $CHOWN_UID"
            chown -R $CHOWN_UID $TARGET
        fi

    done

fi
