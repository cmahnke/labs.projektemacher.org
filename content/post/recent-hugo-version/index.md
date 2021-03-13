---
date: 2020-12-08T12:22:44+02:00
title: "Hugo Updates"
tags:
- Hugo
---

# Update: Inzwischen wird Hugo 0.81.0 eingesetzt

Bisher wird Hugo 0.74.3 vom 23.7.20 verwendet, aktuell ist Version 0.79. Änderungen an der Handling von JavaScript Build-Prozessen verhindern ein Update. Erschwerend kommt hinzu, dass Homebrew in letzter Zeit eher verschlimmbessert wurde. Downgrades sind nicht mehr einfach über die Kommandozeile möglich.

<!--more-->

# Aktualisierung des Generators

```
git clone https://github.com/gohugoio/hugo.git
cd hugo
CGO_ENABLED=1 go build --tags extended
mv hugo /usr/local/bin/hugo-0.80
```

Damit steht als `hugo-0.80` eine aktuellere Hugo Version zur Verfügung.

Zusätzlich muss `.github/workflows/gh-pages.yml` angepasst werden:

```
      - name: Setup Hugo
        uses: peaceiris/actions-hugo@v2
        with:
          hugo-version: '0.81.0'
```

# Anpassungen der Blogs

Die notwendigen Anpassungen liegen im Bereich des [Bauens der Javascript Abhängigkeiten](https://gohugo.io/hugo-pipes/js/), ein einheitliches Theme, das sowohl Mirador als auch Openlayers bereit stellt, sollte das Problem lösen.
