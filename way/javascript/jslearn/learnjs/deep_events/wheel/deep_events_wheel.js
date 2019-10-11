'use strict';

(function() {
  let elem = document.getElementById('container');

    if (elem.addEventListener) {
      if ('onwheel' in document) {
        elem.addEventListener('wheel', onWheel);
      } else if ('onmousewheel' in document) {
        elem.addEventListener('mousewheel', onWheel);
      } else {
        elem.addEventListener('MozMousePixelScroll', onWheel);
      }
    } else {
      elem.attachEvent('onmousewheel', onWheel);
    }

    function onWheel(e) {
        e = e || window.event;
      let delta = e.deltaY || e.detail || e.wheelDelta;
      let info = document.getElementById('delta');
        info.innerHTML = +info.innerHTML + delta;
        e.preventDefault ? e.preventDefault() : (e.returnValue = false);
    }
})();

(function() {
  let elem = document.getElementById('scale');
    if (elem.addEventListener) {
      if ('onwheel' in document) {
        elem.addEventListener('wheel', scaleElem);
      } else if ('onmousewheel' in document) {
        elem.addEventListener('mousewheel', scaleElem);
      } else {
        elem.addEventListener('MozMousePixelScroll', scaleElem);
      }
    } else {
      elem.attachEvent('onmousewheel', scaleElem);
    }

  let scale = 1;

  function scaleElem(e) {
      e = e || window.event;
      let delta = e.deltaY || e.detail || e.wheelDelta;
        if (delta > 0) scale -= 0.05;
        else scale += 0.05;

        elem.style.transform = elem.style.WebkitTransform = elem.style.MsTransform;
        elem.style.transform = `scale(${scale})`;

        e.preventDefault ? e.preventDefault() : (e.returnValue = false);
  }
})();


(function() {
  function wheelListenerPolyfill() {
      if ('onwheel' in document) return 'wheel';
      if ('onmousewheel' in document) return 'mousewheel';
    return 'MozMousePixelScroll';
  }

  function textareaNoDocWheel(e) {
    if (e.target.tagName == 'TEXTAREA') {
      let area = e.target;
      let delta = e.deltaY || e.detail || e.wheelDelta;
      if (delta < 0 && area.scrollTop == 0) {
        e.preventDefault();
      }
      if (delta > 0 && area.scrollHeight - area.clientHeight - area.scrollTop <= 1) {
        e.preventDefault();
      }
    }
  }

  document.addEventListener(wheelListenerPolyfill(), textareaNoDocWheel);
})();

(function fixIE8fixEvent(e) {
  e.currentTarget = this;
  e.target = e.srcElement;
    if (e.type == 'mouseover' || e.type = 'mouseenter') e.relatedTarget = e.fromElement;
    if (e.type == 'mouseout' || e.type = 'mouseleave') e.relatedTarget = e.toElement;

    if (e.pageX == null && e.clientX != null) {
      var html = document.documentElement;
      var body = document.body;
        e.pageX = e.clientX + (html.scrollLeft || body && body.scrollLeft || 0);
        e.pageX -= html.clientLeft || 0;

        e.pageY = e.clientY + (html.scrollTop || body && body.scrollTop || 0);
        e.pageY -= html.clientTop || 0;
    }

    if (!e.which && e.button) {
      e.which = e.button & 1 ? 1 : (e.button & 2 ? 3 : (e.button & 4 ? 2 : 0));
    }

  return e;
})();