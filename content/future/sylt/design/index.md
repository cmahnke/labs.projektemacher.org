---
title: 'Design'
date: 2022-11-02T18:30:07+02:00
archive: false
news: false
tags:
- Ausstellung
- Zukünftige Seite
outputs:
  - html
  - qrcode
---

# Ideen zur Gestaltung

## Plakate

Hier sind die Texte zur Präsentation in der Ausstellung gemeint, keine "Werbeplakate" um auf die Ausstellung aufmerksam zu machen.

## Webseite

Eine Webseite ist für die Präsentation von Audioinhalten und zusätzlichen Texten notwendig. Da sie in der Ausstellung genutzt werden soll, muss sie auch für mobile Endgeräte optimiert sein.

Da die Themen die Blöcke der Ausstellung bilden, sollte sich das im Design niederschlagen, ein Vorbild kann das Theme [Twenty Twenty](https://github.com/themefisher/twenty-twenty-hugo) sein. Allerdings weniger eckig. Ebenfalls können darauf aufbauend abstrakte grafische Elemente erzeugt werden, die die verschiedenen Themenbereiche (s.u. "Farben") repräsentieren.

## Schriftarten

### Analyse
Für „Wilma Bräuner, die Leica, das Meer ... und ihr Insel-Expreß“ wurde [Helvetica](https://de.wikipedia.org/wiki/Helvetica_(Schriftart)) benutzt.
Für „Leuchtendes Sylt“ kommt [Melior](https://www.typografie.info/3/Schriften/fonts.html/melior-r618/) von [Hermann Zapf](https://de.wikipedia.org/wiki/Hermann_Zapf) zum Einsatz.

Mögliche Alternativen sind:
 * Edison Book
 * Latino Regular
 * Marseille (Serial)

Eine Kombination bider Schriften bietet sich an, da die Helvetica auf der [Akzidenz-Grotesk](https://de.wikipedia.org/wiki/Akzidenz-Grotesk) basiert und diese Kombinationen nicht ungewöhnlich sind. Weitere [Kombinationen](https://fontsinuse.com/typefaces/3357/melior).

Schmuckschriften (z.B. für „Sylt“) oder die auf den Umschlägen können (noch) nicht identifiziert werden, können aber auch als Vektorgrafik eingebettet werden. So kann das Wort "Sylt" im Fließtext eingebunden werden, die stört den Lesefluss, sorgt aber für eine individuelle Note.

{{< figure src="./das-braeuner-buch-sylt-fotos-einer-malerin.png" title="Schnappschuss Online-Antiquariat" caption="Umschlag von \"Das Bräuner-Buch Sylt - Fotos einer Malerin\", 60er" link="https://www.buchfreund.de/de/d/p/103491836/das-braeuner-buch-sylt-fotos-einer-malerin" target="_blank" >}}

### Beispiel Schmuckschrift

Als Beispiel dien der Schriftzug "Sylt" in zwei Varianten, die erste Variante ist dabei weniger geeignet, da die feinen Linien in kleineren Skalierungen nicht so gut zur Geltung kommen.

{{< figure src="./Sylt2.jpg" title="Scan" caption="Titelseite von \"Leuchtendes Sylt - Das Bräuner Farbfotobuch\", 1965" >}}

{{< figure src="./Sylt2.svg" title="Vektorgrafik" caption="Die Vektorgrafik müsste noch weiter geglättet werden." >}}

{{< figure src="./Sylt.jpg" title="Scan" caption="Buchdeckel von \"Sylt: Bildbuch einer Insel\", 1950er." >}}

{{< figure src="./Sylt.svg" title="Vektorgrafik" caption="Die Vektorgrafik müsste noch weiter geglättet werden." >}}


### Freie Alternativen

 * Für Helvetica: [Roboto](https://fonts.google.com/specimen/Roboto)
 * Für Melior: (Muss noch identifiziert werden)

# Farben

Mehrere Farbschemata sind denkbar:
 * Text Schwarz und Hintergrund Weiß für Print und Web
 * Text Schwarz, Hintergrund Beige bzw. hellgelb als Verweis auf altes Papier (Postkaten, Akten, Buchumschläge)

Weitere Gestaltungselemente (wie Rahmen, Bänder etc) in Varianten von Hellgelb bis braun. Als Kontrast blau (Meer), diese können dann auch den Themenbereichen zugeordnet werden, siehe Beispiel unten.

Prinzipiell sollten die Farben so gewählt sein, dass sie auch als Themenfarben funktionieren können.

## Beispiel

{{< figure src="./Cover.jpg" title="Quelle der Farben" caption="Umschlag von \"Leuchtendes Sylt - Das Bräuner Farbfotobuch\", 1965" >}}

Es kann auch ein anderes Bild zur Extraktion eines Farbthemas herangezogen werden.

***Beispielfarben***
  * #F5E2C8 Buchdekel {{< color-sample color="#F5E2C8" text="Buchdeckel" >}}
  * #260101 (Schatten) {{< color-sample color="#260101" text="Schatten" >}}
  * #F7DBA7 (Düne) {{< color-sample color="#D9B26A" text="Düne" >}}
  * #5D8094 (Meer) {{< color-sample color="#5D8094" text="Meer" >}}
  * #BDE3F2 (Himmel) {{< color-sample color="#BDE3F2" text="Himmel" >}}
  * #7C8C3F (Gras) {{< color-sample color="#7C8C3F" text="Gras" >}}


***Themenbereiche:***
* (Einleitung): Wird umdefiniert zu "Archivarischer Kontext" {{< color-sample color="#F5E2C8" text="Buchdeckel" >}}
* Lebensstationen {{< color-sample color="#5D8094" text="Meer" >}}
* Zeichnungen und Malerei {{< color-sample color="#D9B26A" text="Düne" >}}
* Fotografie {{< color-sample color="#BDE3F2" text="Himmel" >}}
* Engagement gegen Atlantis und für den Naturschutz {{< color-sample color="#7C8C3F" text="Gras" >}}

# Kacheln für die Navigation

Kacheln dienen der einfach erkennbaren Navigation, die Farben der einfachen Wiedererkennung.

Die hier gezeigte Ansicht ist für Smartphones, dort werden die Kacheln nacheinander angezeigt. Auf dem Desktop wird ein 2x2 Raster gezeigt.

Weitere geplante Anpassungen:
* Die Kachel für den Bereich Archiv ist nicht enthalten
* Die Ränder werden noch geschärft
* Die Schriftfarbe wird je nach Hintergrund gewählt, um den Kontrast zu erhöhen.

## Meer

{{< figure src="./Wasser.svg" title="Lebensstationen" class="nav-tile" >}}

## Dünen

{{< figure src="./Dünen.svg" title="Zeichnung und Malerei" class="nav-tile" >}}

## Himmel

{{< figure src="./Himmel.svg" title="Fotographie" class="nav-tile" >}}

## Gras

{{< figure src="./Gras.svg" title="Naturschutz" class="nav-tile" >}}

# Werkzeuge
* [Schriftidenfikation](https://www.myfonts.com/pages/whatthefont)
* [Farbvarianten](http://scg.ar-ch.org/)
* [Extraktion von Farbthemen](https://color.adobe.com/de/create/image)

## Sonstiges

### Identifikation der Schiftarten
* Ein Scan in einer hohen Auflösung (600dpi)
* Ein Webdienst: https://www.myfonts.com/pages/whatthefont
* Dann Beurteilung der Ergebnisse, an Hand des zeitlichen Kontexts, da die Ergebnisse aus dem Schritt davor viele Schriften liefert, die es damals gar nicht gab, oder eher ungebräuchlich waren. Dabei helfen Schriftmusterbücher.
