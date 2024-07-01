---
date: 2020-12-13T20:14:44+02:00
title: "Kartenmaterial"
type: redirect
target: https://christianmahnke.de/post/maps/
tags:
- Karten
---

# Vorbereitungen

Bevor Beiträge auf Karten angezeigt werden können, müssen folgende Schritte erlegdigt sein:
* Geokodierung von Beiträgen und / oder Tags
* Generierung einer anwendungsspezifischen Repräsentation (GeoJSON, KML)

Erst danach kann das auf einer Karte visualisiert werden.

Ein Beispiel für die [alten 3D Bilder](/future/3d/) ist [hier](/future/3d/map.geojson) zu finden.

# Anzeige im Browser

Um die generierten Daten im Browser anzuzeigen, kann das von [OpenStreetMap](https://www.openstreetmap.org/) bereitgestellte Kartenmaterial verwendet werden. Dabei übernimmt ein externer Server die Erzeugung der Bilddaten.

Hier als Beispiel die Darstellung der Orte der 3D Bilder auf einer Karte:

{{< html/iframe-consent >}}
    {{< maps/osm src="/future/3d/map.geojson" >}}
{{< /html/iframe-consent >}}

# Ausblick

Nun fehlt nur noch der letzte Schritt, eigenes Kartenmaterial erzeugen um unabhängig von externen Diensten zu sein und auch mehr Gestaltungsspielraum zu haben...
