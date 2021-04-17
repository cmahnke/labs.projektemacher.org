---
date: 2021-04-17T11:22:44+02:00
title: "JPEG XL"
tags:
- Work in progress
---

# Why JPEG XL?
[JPEG XL](https://en.wikipedia.org/wiki/JPEG_XL) is a new format for raster images, in fact, is's so recent (at the time this text was written) there haven't even been an entry in the German Wikipedia.

You can read there what exactly JPEG XL does differently or better than the well-known JPEG. We limit ourselves here to the advantages for the Projektemacher blogs:
* Less storage space required
* Lossless compression available

Disadvantages are currently:
* Few programs can handle it
* The existing algorithms are not yet optimized - it is slower

The reference implementation can be found on [GitLab](https://gitlab.com/wg1/jpeg-xl).

# How?

Since the conversion to IIIF derivatives on GitHub is done by a [Docker image](https://github.com/cmahnke/iiif-action), the easiest way to integrate the use of the new format into the tool chain is to add JPEG XL support to this image. For the used [LibVIPS](https://github.com/libvips/libvips) there is a [Pull Request](https://github.com/libvips/libvips/pull/2181), which supports the JPEG XL reference implementation. This is now built into a variant of the image for conversion:

```
docker pull ghcr.io/cmahnke/iiif-action:latest-jxl
```

# Preparations

## Start an interactive container

The image can also be used to create the source files.

```
docker run -it -v ${PWD}:${PWD} 'ghcr.io/cmahnke/iiif-action:latest-jxl' /bin/bash -c "cd ${PWD}; $SHELL"
```

## File conversion

Using `vips` directly has the advantage that you can use any supported input file format.

```
vips copy front.tif front.jxl[Q=100]
```

The following issues have been discovered:

* `vips jxlsave` does not support parameters
* The parameter `effort` can lead to a crash if it is greater than `7` - might be a memory problem, not yet tested with `cjxl`

`cjxl` can also be used, but you should use a losslessly compressed (e.g. PNG) input file:

```
cjxl front.png front.jxl
```

The possible options are linked here:
* [`vips jxlsave`](https://github.com/libvips/libvips/blob/add-jxl/libvips/foreign/jxlsave.c)
* [`cjxl`](https://gitlab.com/wg1/jpeg-xl/-/blob/master/doc/man/cjxl.txt)
