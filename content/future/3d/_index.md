---
title: Vintage Reality
displayinlist: false
metaPage: true
description: "3D Bilder sind keine neue Erfindung - bereits Ende des 19. Jahrhunderts gab es 3D Betrachter..."
outputs:
- html
- geojson
type: redirect
target: https://vintagereality.projektemacher.org/
cascade:
  - target:
      kind: "{page}"
      lang: de
      path: '**'
    params:
      draft: true
---

Ein Experiment zu Medientypen und Dateiformaten.

# Update Frühjahr 2024

Diese Sektion ist nun ein eigenes [Blog](https://vintagereality.projektemacher.org/), dort werden auch vorher nicht gezeigte Bilder bereitgestellt. Zusätzlich sind weitere Funktionalitäten, wie eine Darstellung für Rot-Grün-Brillen und generierte Tiefenkarten hinzugekommen.

# Update Weihnachten 2022

* Die Qualität der generierten Wackelbilder wurde massiv durch die Nutzung von [StereoscoPy](https://github.com/2sh/StereoscoPy), verbessert. Es nutzt OpenCV um die Bildanordnung zu verbessern. Zusätzlich können jetzt Anaglyphen erzeugt werden.
* Die verbesserte Anordnung funktioniert nicht sehr gut bei wenig strukturierten Inhalten, wie Innenräumen oder vielen Pflanzen, ohne Horizont oder ohne Kontrast.
* Es sind nun mehr Bilder online
* Es werden nun auch [MPO](https://de.wikipedia.org/wiki/Multi_Picture_Object) Dateien erzeugt.


## Weitere Informationen zur Ansicht im Browser bieten verschiedene Blogs:
* [Learning to Free-View: See Stereoscopic Images with the Naked Eye](https://stereoscopy.blog/2022/03/11/learning-to-free-view-see-stereoscopic-images-with-the-naked-eye/)

# Bildlizenzen
Die folgenden Dateien von Wikimedia Commons kommen zum Einsatz, die jeweiligen Lizenzbedingungen finden sich hinter dem jeweiligen Link.
* {{< figure src="/images/3d/3d_glasses_red_blue.svg" class="glasses-icon" link="https://commons.wikimedia.org/wiki/File:3d_glasses_red_blue.svg" >}}
* {{< figure src="/images/3d/3d_glasses_red_cyan.svg" class="glasses-icon" link="https://de.wikipedia.org/wiki/Datei:3d_glasses_red_cyan.svg" >}}


# Weitere Links

* [The Stereoscopic Society: Early 3D](https://www.stereoscopicsociety.org.uk/WordPress/early-3d/)
* [History of Stereoscopy](https://jules-richard-museum.com/history-stereoscopy-engl/)
* [3D in the 19th century](https://blog.nationalmuseum.ch/en/2021/07/tourism-stereoscopic-images/)
* [Stereo 3D Cameras](https://www.studio3d.com/pages/stereophoto.html)
* [Stereoscopy: the birth of 3D technology](https://artsandculture.google.com/story/stereoscopy-the-birth-of-3d-technology-the-royal-society/pwWRTNS-hqDN5g?hl=en)
