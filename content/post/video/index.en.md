---
date: 2020-12-16T20:14:44+02:00
title: "Video"
tags:
- Medientypen
---

Using the [`hugo-video`](https://github.com/martignoni/hugo-video) theme local videos can be included via shortcode:

{{< video src="marburg" >}}

<!--more-->

YouTube is supported by a buildin [shortcode](https://gohugo.io/content-management/shortcodes/#youtube).

Converting a DVD video file into MP4 for the web. With deiniterlacing (`-vf yadif`) and cutting to timestamps (`-ss 00:00:05 -to 00:05:39`).

```
ffmpeg -i VTS_01_1.VOB -vf yadif -ss 00:00:05 -to 00:05:39 -an output.mp4
```
