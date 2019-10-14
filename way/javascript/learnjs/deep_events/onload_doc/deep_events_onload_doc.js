(function() {
  document.addEventListener('DOMContentLoaded', ready)

  function ready() {
    alert('DOM is ready');
    alert('Image size: ' + img.offsetWidth + 'x' + img.offsetHeight);
  }

  window.addEventListener('load', function() {alert('Document and resurses are loaded')})

  window.onbeforeunload = function() {
  return "Данные не сохранены. Точно перейти?";
};
});

(function() {
  let script = document.createElement('script');
    script.src = 'https://cdnjs.cloudflare.com/ajax/libs/lodash.js/4.3.0/lodash.js';
  document.body.appendChild(script);

  script.onload = function() {
    console.log( _ );
    script = document.createElement('script');
      script.src = 'https://example.com/404.js';
    document.body.appendChild(script);
      script.onerror = function() {
        console.log( "Error: " + this.src );
      }
  }

});

(function() {
  let script = document.createElement('script');
    script.src = 'https://code.jquery.com/jquery.js';
  document.documentElement.appendChild(script);

  function afterLoad() {
    console.log( 'Loading is succesfull: ' + typeof(jQuery) );
  }

  script.onload = script.onerror = function() {
    if (!this.exeecuted) {
      this.executed = true;
      afterLoad();
    }
  };

  script.onreadystatechange = function() {
    let self = this;
      if (this.readyState == 'complete' || this.readyState == 'loaded') {
        setTimeout(function() {
          self.onload()
        }, 0);
      }
  };
})();