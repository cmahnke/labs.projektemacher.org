---
date: 2020-12-16T20:14:44+02:00
title: "Video"
tags:
- Medientypen
---

Converting a DVD video file into MP4 for the web. With deiniterlacing (`-vf yadif`) and cutting to timestamps (`-ss 00:00:05 -to 00:05:39`).

```
ffmpeg -i VTS_01_1.VOB -vf yadif -ss 00:00:05 -to 00:05:39 -an output.mp4
```
