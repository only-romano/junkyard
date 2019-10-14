function checkMobilesWidth() {
    // fix for mobile width
  if (/Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i
    .test(navigator.userAgent))
      document.body.style.width = '100vw'; // actions
}

(function() {
    // optimized images loader
    window.addEventListener('scroll', loadMainImages);
    loadMainImages();

    let loadMainImages = (optimized) => {
        let counter = 0;
        while (counter < optimized.length) {
            let img = optimized[counter];
            if (img.getBoundingClientRect().top < document.documentElement.clientHeight * 1.5) {
                img.setAttribute('src', img.getAttribute('realsrc'));
                img.classList.remove('optimized-black');
                // optimized.pop(counter)
                counter++;
            }
        }
    }
})();
