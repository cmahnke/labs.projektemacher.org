/*
 * Ambient declarations for packages that don't ship TypeScript types.
 * This must stay a script file (no imports/exports on the top level) —
 * otherwise the declarations would become module augmentations, which
 * require the augmented module to be typed already.
 */

declare module 'webxr-polyfill' {
  const WebXRPolyfill: new () => void;
  export default WebXRPolyfill;
}

declare module 'ak-kaleidoscope' {
  const Kaleidoscope: unknown;
  export default Kaleidoscope;
}
