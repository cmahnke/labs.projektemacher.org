---
date: 2021-02-26T18:22:44+02:00
title: "Fold-outs"
iiifContext: http://iiif.io/api/presentation/2/context.json
tags:
- IIIF
- Work in progress
outputs:
- html
- iiif-manifest
resources:
- src: "front01.jpg"
  params:
    iiif: front01/info.json
    hint: continuous
- src: "front02.jpg"
  params:
    iiif: front02/info.json
    hint: continuous
- src: "front03.jpg"
  params:
    iiif: front03/info.json
    hint: continuous
- src: "front04.jpg"
  params:
    iiif: front04/info.json
    hint: continuous
- src: "front05.jpg"
  params:
    iiif: front05/info.json
    hint: continuous
- src: "front06.jpg"
  params:
    iiif: front06/info.json
    hint: continuous
- src: "front07.jpg"
  params:
    iiif: front07/info.json
    hint: continuous
- src: "front08.jpg"
  params:
    iiif: front08/info.json
    hint: continuous
- src: "front09.jpg"
  params:
    iiif: front09/info.json
    hint: continuous
- src: "front10.jpg"
  params:
    iiif: front10/info.json
- src: "back01.jpg"
  params:
    iiif: back01/info.json
    hint: continuous
- src: "back02.jpg"
  params:
    iiif: back02/info.json
    hint: continuous
- src: "back03.jpg"
  params:
    iiif: back03/info.json
    hint: continuous
- src: "back04.jpg"
  params:
    iiif: back04/info.json
    hint: continuous
- src: "back05.jpg"
  params:
    iiif: back05/info.json
    hint: continuous
- src: "back06.jpg"
  params:
    iiif: back06/info.json
    hint: continuous
- src: "back07.jpg"
  params:
    iiif: back07/info.json
    hint: continuous
- src: "back08.jpg"
  params:
    iiif: back08/info.json
    hint: continuous
- src: "back09.jpg"
  params:
    iiif: back09/info.json
    hint: continuous
- src: "back10.jpg"
  params:
    iiif: back10/info.json
---

Demonstrator for displaying fold-outs (Orihon, Accordion Book) using [Mirador](https://github.com/ProjectMirador/mirador). Hints on encoding the fold-out can be found [here](https://groups.google.com/g/iiif-discuss/c/tG1O3y3ecWw). the following pages are relevant:
* [IIIF cookbook](https://preview.iiif.io/cookbook/3333-choice/recipe/0035-foldouts/)
* [Example Mahābhārata scroll](https://librarylabs.ed.ac.uk/iiif/uv/?manifest=https://librarylabs.ed.ac.uk/iiif/manifest/mahabharataFinal.json#?c=0&m=0&s=0&cv=0&xywh=-25583%2C0%2C54981%2C49069)

<!--more-->

Example for currently supported viewing hints:
```
- src: "front01.jpg"
  params:
    iiif: front01/info.json
    hint: non-paged
```

Example for the necessary change:
```
- src: "front01.jpg"
  params:
    iiif: front01/info.json
    hint: continuous
```

{{< iiif/presentation manifestUrl="manifest.json" >}}
