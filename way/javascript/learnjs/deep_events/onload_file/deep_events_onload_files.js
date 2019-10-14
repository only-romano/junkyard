(function betterAlt() {
  let body = document.body;
  let images = document.getElementsByTagName('img');
  let placeholders = document.getElementsByClassName('img-replace');
    for (let i = images.length - 1; i >= 0; i--) {
      let placeholder = placeholders[i].cloneNode(true);
      let image = images[i];
        placeholder.classList.add('replacers');
      body.replaceChild(placeholder, image);
      if (image) image.onload = function() { replaceImg(placeholder, image) };
    }

  function replaceImg(placeholder, image) {
    body.replaceChild(image, placeholder);
  }
})();


(function callbackImages() {

  function preloadImages(sources, callback) {
    let counter = sources.length;
      for (let src of sources) {
        let image = new Image();
          image.src = src;
          image.onload = image.onerror = function() {
            counter--;
            if (counter === 0) callback();
          };
      }
  }

  let sources = [
    "https://js.cx/images-load/1.jpg",
    "https://js.cx/images-load/2.jpg",
    "https://js.cx/images-load/3.jpg"
  ];
    for (let source of sources) source += '?' + Math.random();

  function testLoaded() {
    let widthSum = 0;
      for (let source of sources) {
        let img = document.createElement('img');
          img.src = source;
          widthSum += img.width;
      }
      alert(widthSum);
  }

  testLoaded();
  preloadImages(sources, testLoaded);

})();

(function loadScripts() {

  function addScript(src, callback) {
    let script = document.createElement('script');
    let loaded = false;
      script.src = src;
      script.onload = script.onerror = onload;
      script.onreadystatechange = function() { if (this.readyState == 'loaded' || this.readyState == 'complete') setTimeout(onload, 0)};
    let parentScript = document.getElementsByTagName('script')[0];
    parentScript.parentNode.insertBefore(script, parentScript);

    function onload() {
      if (loaded) return;
      loaded = true;
      callback();
    }
  }

  addScript('go.js', function() { go(); });
})();


(function manyScripts() {

  function addScripts(scripts, callback) {
    let counter = scripts.length;
    let parentScript = document.getElementsByTagName('script')[0];

    function onload() {
      counter--;
      if (counter === 0) callback();
    }

      for (src of scripts) {
        let script = document.createElement('script');
          script.src = src;
          script.onload = script.onerror = onload;
          script.onreadystatechange = function() {
            if (this.readyState == 'loaded' || this.readyState == 'complete') {
              setTimeout(onload, 0);
            }
          };

        parentScript.parentNode.insertBefore(script, parentScript);
      }
  }

  addScripts(['a.js', 'b.js', 'c.js'], function() { a() });
})();