---
date: 2020-12-16T20:14:44+02:00
title: "Video"
tags:
- Medientypen
---

Mit dem [`hugo-video`](https://github.com/martignoni/hugo-video) Theme können einfach lokale Videos eingebunden werden:

{{< video src="marburg" >}}

<!--more-->

YouTube wird von Hugo mit dem entsprechendem [Shortcode](https://gohugo.io/content-management/shortcodes/#youtube) unterstützt.

Eine DVD Video Datei in MP4 fürs Web konvertieren. Mit deiniterlacing (`-vf yadif`) und Zuschnitt auf einen speziellen Ausschnitt (`-ss 00:00:05 -to 00:05:39`).

```
ffmpeg -i VTS_01_1.VOB -vf yadif -ss 00:00:05 -to 00:05:39 -an output.mp4
```
