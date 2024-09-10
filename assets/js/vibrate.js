
var supportsVibrate = "vibrate" in navigator;
if (!supportsVibrate) {
  return
}

function addHapticFeedback (elem, jsonUrl) {
  var touchMap =fetch(jsonUrl, {
    method: 'GET',
    headers: {
        'Accept': 'application/json',
    },
  })
   .then(response => response.json())
   .then(response => console.log(JSON.stringify(response)))
  if (touchMap !== undefined) {

  }

  //TODO: Finish this
  /* See:
    https://www.chestysoft.com/imagefile/javascript/get-coordinates.asp
    https://stackoverflow.com/questions/75262324/javascript-how-to-get-the-exact-touch-position-on-an-image
  */

}
