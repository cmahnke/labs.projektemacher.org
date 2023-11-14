window.$ = window.jQuery = require('jquery');
import { addConsent } from './iframe-consent';
import { initMap } from './maps/osm-map.js';
import { fullscreen } from './fullscreen.js';

window.addConsent = addConsent;
window.initMap = initMap;
