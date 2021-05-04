window.addFSToggle = function (button, elem) {
    button.addEventListener('click', function() {
        var fsStyle = "position: fixed; top: 0; left: 0; height: 100%; width: 100%; overflow: hidden;";
        if (!document.fullscreenElement) {

            elem.setAttribute('style', fsStyle);
            button.setAttribute('style', 'position: fixed;');
            document.querySelector('body').setAttribute('style', 'overflow: hidden;');
            document.documentElement.requestFullscreen();
        } else {
            if (document.exitFullscreen) {
                elem.setAttribute('style', '');
                button.setAttribute('style', '');
                document.querySelector('body').setAttribute('style', '');
                document.exitFullscreen();
            }
        }
    });
};
