---
date: 2020-12-08T12:22:44+02:00
title: "Hugo Updates"
tags:
- Hugo
---

**Update: Hugo 0.82.0 is now being used**

Up to the time this article was written, Hugo 0.74.3 from July 23, 2020 was used, at that time the current version was 0.79. Changes to the handling of JavaScript build processes prevent an update. To make matters worse, `homebrew` has been getting worse lately. Downgrades are no longer possible simply from the command line. In the meantime, Hugo is being built directly from the sources, see below.

<!--more-->

# Use of a specific Hugo version

Shown with version 0.80.0.

## Local update

```
git clone https://github.com/gohugoio/hugo.git
cd hugo
git checkout release-0.80.0
CGO_ENABLED=1 go build --tags extended
mv hugo /usr/local/bin/hugo-0.80
```
This will result in an executable `hugo-0.80` on `$PATH`.

## for the GitHub workflow

`.github/workflows/gh-pages.yml` has to be changed:

```
      - name: Setup Hugo
        uses: peaceiris/actions-hugo@v2
        with:
          hugo-version: '0.80.0'
```

# Required changes 0.74.3 &rarr; 0.79.0

The required changes are in the area of ​​[building the Javascript dependencies](https://gohugo.io/hugo-pipes/js/), a uniform theme that provides Mirador and OpenLayers should solve the problem.

# More updates

This section is continuously updated.

## Hugo 0.81 &rarr; 0.82

* `js.Build` no longer works with `minify` - see [#8370](https://github.com/gohugoio/hugo/issues/8370)

## Hugo 0.82 &rarr; 0.82.1

* GeoJSON in `[outputFormats]` should work now - see [#8406](https://github.com/gohugoio/hugo/issues/8406)
