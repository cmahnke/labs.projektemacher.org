---
date: 2020-12-13T20:14:44+02:00
title: "Kartenmaterial"
type: redirect
target: https://christianmahnke.de/post/maps/
tags:
- Karten
---

# Preparations

Before posts can be displayed on maps, the following steps must be taken:
* Geocoding of posts and / or tags
* Generation of an application-specific representations (GeoJSON, KML)

After this has been done, the next step can be approached.

An example of the [old 3D images](/future/3d/) can be found [here](/future/3d/map.geojson).

# Plotting data on a map in a browser

The map material provided by [OpenStreetMap](https://www.openstreetmap.org/) can be used to display the generated data in the browser. An external server generates the images needed to display a map.

This example shows the locations of the 3D images on a map:

{{< html/iframe-consent >}}
    {{< maps/osm src="./map.geojson" >}}
{{< /html/iframe-consent >}}

# Next steps

Now only the last step is missing, generating your own map material in order to be independent of external services and also to have the possibility to change the appearance...
