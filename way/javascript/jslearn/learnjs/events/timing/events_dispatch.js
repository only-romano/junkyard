
(function autoclick() {
  var event = new Event('click');
  elem.dispatchEvent(event);
})();


(function rabbitHide() {
  function hide() {
    var event = new Event('hide', {
      cancelable: true
    });
      if (!rabbit.dispatchEvent(event)) {
        alert( 'Event is canceled by listener' );
      } else {
        rabbit.hidden = true;
      }
  }

  rabbit.addEventListener('hide', function(event) {
    if ( confirm('Do you want to cancel hiding rabbit and run preventDefault?')) {
      event.preventDefault();
    }
  });

  setTimeout(hide, 2000);
})();

(function() {
  document.addEventListener('hello', function(event) {
    alert('Halo!');
    event.preventDefault();
  }, false);

  var event = new Event('hello', {bubbles: true, cancelable: true});
    if (hElem.dispatchEvent(event) === false) {
      alert('Event was canceled by preventDefault');
    }
})();

(function() {
  var e = new MouseEvent('click', {
    bubbles: true,
    cancelable: true,
    clientX: 100,
    clientY: 100
  })
})();

(function() {
  vasya.addEventListener('hello', function(event) {
    alert( 'Hello, ' + event.detail.name + '!') ;
  }, false);

  var event = new CustomEvent('hello', {
    detail: { name: 'Vasily' }
  });

  vasya.dispatchEvent(event);
})();

(function IE9() {
  document.addEventListener('hola', function(event) {
    alert('Crossbrowser halo!');
    event.preventDefault();
  }, false);

  var event = document.createEvent('event');
    event.initEvent('hola', true, true);

    if (elem.dispatchEvent(event) === false) {
      alert('Event was canceled by preventDefault');
    }
})();

(function IE9autoclick() {
  buttonId.onclick = function(e) {
    alert( 'Click on coordinates: ' + e.clientX + ':' + e.clientY );
  };

  var event = document.createEvent('MouseEvent');
  event.initMouseEvent('click', true, true, null, 0, 0, 0, 100, 100, true, true, true, null, 1, null);
  buttonId.dispatchEvent(event);
})();


(function customEventPolyfil() {
  try {
    new CustomEvent('IE has CustomEvent, but doesn\'t support constructor');
  } catch (e) {

    window.CustomEvent = function(event, params) {
      var evt;
      params = params || {
        bubbles: false,
        cancelable: false,
        detail: undefined
      };

      evt = document.createEvent('CustomEvent');
      evt.initCustomEvent(event, params.bubbles, params.cancelable, params.detail);
      return evt
    };

    CustomEvent.prototype = Object.create(window.Event.prototype);
  }


})();