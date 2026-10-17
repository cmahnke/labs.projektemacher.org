const supportsVibrate = 'vibrate' in navigator;

// The original script aborted evaluation here (top-level `return`) when
// vibration was not supported. It had no other side effects.
export const hapticFeedbackSupported = supportsVibrate;

//TODO: Finish this
/* See:
  https://www.chestysoft.com/imagefile/javascript/get-coordinates.asp
  https://stackoverflow.com/questions/75262324/javascript-how-to-get-the-exact-touch-position-on-an-image
*/
export function addHapticFeedback(elem: HTMLElement, jsonUrl: string): void {
  const touchMap = fetch(jsonUrl, {
    method: 'GET',
    headers: {
      'Accept': 'application/json',
    },
  })
    .then(response => response.json())
    .then(response => console.log(JSON.stringify(response)));
}
