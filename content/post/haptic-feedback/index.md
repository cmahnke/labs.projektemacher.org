---
date: 2020-12-04T18:22:44+02:00
title: "Haptisches Feedback"
tags:
- IIIF
iiifManifest: ./index.json
iiifContext: http://iiif.io/api/presentation/2/context.json
resources:
- src: "page031.jpg"
  params:
    iiif: page031/info.json
    hint: non-paged
    label: Tafel 31
---

<!--more-->

# Vorbereitung der Bilddaten

{{< figure src="./page031-0-cut.png" caption="Ausschnitt zur Analyse" >}}

{{< figure src="./page031-0-filter_0_FIND_EDGES.png" caption="Kantenerkennung" >}}

{{< figure src="./page031-0-filter_1_EDGE_ENHANCE.png" caption="Kantenverbesserung" >}}

{{< figure src="./page031-0-filter_2_SMOOTH_MORE.png" caption="Weichzeichnen 1" >}}

{{< figure src="./page031-0-filter_3_SMOOTH_MORE.png" caption="Weichzeichnen 2" >}}

{{< figure src="./page031-0-filter_4_GRAYSCALE.png" caption="Graustufen" >}}

{{< figure src="./page031-0-filter_5_EQUALIZE.png" caption="Mittelwert" >}}

{{< figure src="./page031-0-filter_6_BINARIZE.png" caption="Binarisieren" >}}

{{< figure src="./page031-0.png" caption="Reduktion auf eine Pixelkantenlänge von 1mm" >}}

{{< mirador manifestUrl="index.json" >}}
