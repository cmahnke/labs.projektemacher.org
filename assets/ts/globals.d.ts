/*
 * Type declarations for the global APIs the site's script entry points
 * attach to `window`. Theme globals are declared by the theme's own
 * globals.d.ts.
 */

declare global {
  interface Window {
    addFSToggle(button: HTMLElement, elem: HTMLElement): void;
    polyfill: unknown;
    Kaleidoscope: unknown;
    addFullScreen(element: HTMLElement, left: string, right: string): void;
    add3DViewer(element: HTMLElement, left: string, right: string): Promise<unknown>;
  }
}

export {};
