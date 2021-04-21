---
date: 2020-12-08T12:22:44+02:00
title: "Hugo Updates"
tags:
- Hugo
---

**Update: Inzwischen wird Hugo 0.82.0 eingesetzt**

Bis zum Zeitpunk als dieser Beitrag geschrieben wurde, wurde Hugo 0.74.3 vom 23.7.20 verwendet, damals war Version 0.79 aktuell. Änderungen an der Handling von JavaScript Build-Prozessen verhindern ein Update. Erschwerend kommt hinzu, dass `homebrew` in letzter Zeit eher verschlimmbessert wurde. Downgrades sind nicht mehr einfach über die Kommandozeile möglich. Inzwischen wird Hugo aber direkt aus den Quellen gebaut, siehe unten.

<!--more-->

# Nutzung einer spezifischen Version

Am Beispiel von Version 0.80.0.

## Aktualisierung des Generators lokal

```
git clone https://github.com/gohugoio/hugo.git
cd hugo
git checkout release-0.80.0
CGO_ENABLED=1 go build --tags extended
mv hugo /usr/local/bin/hugo-0.80
```
Damit steht als `hugo-0.80` eine aktuellere Hugo Version zur Verfügung.

## Im GitHub Workflow

Zusätzlich muss `.github/workflows/gh-pages.yml` angepasst werden:

```
      - name: Setup Hugo
        uses: peaceiris/actions-hugo@v2
        with:
          hugo-version: '0.80.0'
```

# Anpassungen der Blogs 0.74.3 &rarr; 0.79.0

Die notwendigen Anpassungen liegen im Bereich des [Bauens der Javascript Abhängigkeiten](https://gohugo.io/hugo-pipes/js/), ein einheitliches Theme, das sowohl Mirador als auch Openlayers bereit stellt, sollte das Problem lösen.

# Weitere Aktualisierungen

Dieser Abschnitt wird laufend aktualisiert.

## Hugo 0.81 &rarr; 0.82

* `js.Build` funktioniert nicht mehr mit `minify` - siehe [#8370](https://github.com/gohugoio/hugo/issues/8370)

## Hugo 0.82 &rarr; 0.82.1

* GeoJSON in `[outputFormats]` sollte nun funktionieren - siehe [#8406](https://github.com/gohugoio/hugo/issues/8406)
