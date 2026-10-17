import Map from 'ol/Map';
import { Tile as TileLayer, Vector as VectorLayer } from 'ol/layer';
import View from 'ol/View';
import GeoJSON from 'ol/format/GeoJSON';
import Overlay from 'ol/Overlay';
import { OSM, XYZ, Vector as VectorSource } from 'ol/source';
import { ATTRIBUTION as OSM_ATTRIBUTION } from 'ol/source/OSM';
import type TileSource from 'ol/source/Tile';
import type SimpleGeometry from 'ol/geom/SimpleGeometry';
import { FullScreen, Zoom } from 'ol/control';

const layers: Record<string, TileLayer<TileSource>> = {};

layers['wiki'] = new TileLayer<XYZ>({
    source: new XYZ({
        attributions: [
            OSM_ATTRIBUTION, 'Map data &copy; <a href="http://openstreetmap.org/copyright">OpenStreetMap contributors</a>'],
        url: 'https://maps.wikimedia.org/osm-intl/{z}/{x}/{y}.png?lang=en'
    })
});

layers['osm'] = new TileLayer<OSM>({ source: new OSM() });

export function initMap(element: string, url: string, source?: string): Map {
    // Languages
    let lang = 'en';
    if (document.documentElement.lang !== undefined) {
        /* TODO: Check for lang locale combinations here: "de-de" instead of "de" will currently break this. */
        lang = document.documentElement.lang;
    }
    const toolTips: Record<string, Record<string, string>> = {
        'de': { 'zoomIn': 'Vergrößern', 'zoomOut': 'Verkleinern', 'fullscreen': 'Vollbildansicht', 'rotate': 'Rotation zurücksetzen', 'rotateLeft': '90° nach links drehen', 'rotateRight': '90° nach rechst drehen' },
        'en': { 'zoomIn': 'Zoom in', 'zoomOut': 'Zoom out', 'fullscreen': 'Toggle full-screen', 'rotate': 'Reset rotation', 'rotateLeft': 'Rotate 90° left', 'rotateRight': 'Rotate 90° right' }
    };

    const padding = [30, 30, 30, 30];

    // Popup elements
    const container = document.getElementById(element + '-popup')!;
    const content = document.getElementById(element + '-popup-content')!;
    const closer = document.getElementById(element + '-popup-closer')!;

    // Base layer
    let baseLayer: TileLayer<TileSource>;
    if (source !== undefined && source !== '') {
        if (source in layers) {
            baseLayer = layers[source];
        } else {
            baseLayer = new TileLayer<XYZ>({ source: new XYZ({ url: source }) });
        }
    } else {
        baseLayer = layers['osm'];
    }

    const map = new Map({
        controls: [new Zoom({ zoomInTipLabel: toolTips[lang]['zoomIn'], zoomOutTipLabel: toolTips[lang]['zoomOut'] }),
                   new FullScreen({ tipLabel: toolTips[lang]['fullscreen'] })],
        layers: [baseLayer],
        target: element,
    });
    const overlay = new Overlay({
        element: container,
        autoPan: {
            animation: {
                duration: 250
            }
        }
    });

    map.addOverlay(overlay);
    map.on('click', function (event) {
        const feature = map.forEachFeatureAtPixel(event.pixel,
            function (feature) {
                return feature;
            });

        if (feature) {
            const geometry = feature.getGeometry()! as SimpleGeometry;
            const coord = geometry.getCoordinates() as number[];
            let popup = '<h1>' + feature.get('name') + '</h1>';
            popup += feature.get('popupContent');
            content.innerHTML = popup;
            overlay.setPosition(coord);
        }

    });
    closer.onclick = function () {
        overlay.setPosition(undefined);
        closer.blur();
        return false;
    };

    fetch(url)
        .then(function (response) {
            response
                .json()
                .then(function (geojson) {
                    // See https://openlayers.org/en/latest/examples/geojson.html

                    // See https://gis.stackexchange.com/questions/373285/geojson-doesnt-render-on-map-in-openlayers-project
                    const parser = new GeoJSON({ dataProjection: 'EPSG:4326', featureProjection: 'EPSG:3857' });

                    const vectorSource = new VectorSource({
                        features: parser.readFeatures(geojson)
                    });

                    const vectorLayer = new VectorLayer({
                        source: vectorSource
                    });
                    (vectorLayer as unknown as { reportError: boolean }).reportError = true;
                    map.addLayer(vectorLayer);

                    map.setView(
                        new View({
                            center: [0, 0],
                            zoom: 2
                        })
                    );

                    const extent = vectorSource.getExtent();
                    if (extent) {
                        map.getView().fit(extent,
                            { size: map.getSize() ?? undefined, padding: padding }
                        );
                    }
                })
                .catch(function (body) {
                    console.log('Could not read GeoJSON. ' + body);
                });
        })
        .catch(function () {
            console.log('Could not read data from URL.');
        });
    return map;
}
