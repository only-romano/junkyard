'use strict';

setInterval(() => {
    if (Math.random() > 0.75) {
        let w = document.body.offsetWidth - 200;
        let h = document.body.offsetHeight - 200;

        ghost.style.left = ~~(Math.random() * w) + 'px';
        ghost.style.top = ~~(Math.random() * h) + 'px';
        ghost.style.background = "url(src/ghost.png)";

        setTimeout(() => { ghost.style.background = ''; }, 450);
    }
}, 500)
