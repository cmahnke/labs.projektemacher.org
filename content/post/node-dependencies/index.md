---
date: 2021-03-13T12:22:44+02:00
title: "Node Abhängigkeiten aus Themes"
tags:
- Hugo
- Themes
- Node
---
Mit dem [Upgrade auf eine Hugo version auf über 0.75.0](/post/recent-hugo-version/) besteht die Möglichkeit das Kommando [`hugo mod npm pack`](https://gohugo.io/commands/hugo_mod_npm_pack/) zu verwenden um die Node Abhängigkeiten eines Themes mit denen eines Projektes zusammenzuführen.

Dafür müssen die Abhängigkeiten eines Themes in einer Datei `package.hugo.json` statt `package.json` gesichert sein, es reicht einfach die von `npm` oder `yarn` angelegte Datei umzubenennen. Ein Symlink alleine funktioniert nicht, da Hugo's virtuelles Dateisystem Symlinks nicht mag.

<!--more-->

Wenn es nur darum geht die Abschnitte `dependencies` und `devDependencies` zusammenzuführen klappt das auch sehr gut. Wenn man allerdings noch spezielle Scripte (Abschnitt `scripts` in `package.json`) definiert hat, z.B. um bestehende Node Bibliotheken anzupassen, hilft das ganze nicht wirklich weiter, da diese Abschnitte (und alle anderen, die nicht explizit Abhängigkeiten definieren) bei der Zusammenführung ignoriert.

Dazu gibt es auch ein [Hugo Feature Request](https://github.com/gohugoio/hugo/issues/8319), allerdings ist noch nicht ganz klar ob und wenn ja, wann dieser umgesetzt wird.

Bis dahin muss man sich selber Scripte basteln, die das mit Hilfe von [`jq`](https://stedolan.github.io/jq/) erledigen.


Ein Beispiel für zwei Dateien:
```
jq -s '.[0] * .[1]'  package.hugo.json themes/some-hugo-theme-with-npm-dependencies/package.hugo.json
```

Ein Beispiel für mehrere Themes:
```
find . -name "package.hugo.json" -o -name "package.json" -depth 0 | xargs jq -s add > package.json
```
