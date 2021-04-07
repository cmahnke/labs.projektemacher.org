window.$ = window.jQuery = require('jquery');
//require('iframe-consent');
import { addConsent } from './iframe-consent';

window.addConsent = addConsent;
