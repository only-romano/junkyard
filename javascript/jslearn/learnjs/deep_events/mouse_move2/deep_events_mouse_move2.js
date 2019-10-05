(function() {

  // LISTENERS

  document.addEventListener('mouseover', function(event) {
    listener(event);
  });

  house.addEventListener('mouseout', deleteTip);


  // FUNCTIONS

  function createTip(tip) {
    var spanTip = document.createElement('span');
      spanTip.classList.add('span-tip');
      spanTip.innerHTML = tip;
    document.body.appendChild(spanTip);
    return spanTip;
  }

  function listener(event) {
    var target = event.target;
      while (target != document.documentElement) {
        var tip = target.getAttribute('data-tooltip');
          if (tip) {
            setTipSize( createTip(tip), target );
            break;
          }
        target = target.parentNode;
      }
  }

  function deleteTip() {
    var tip = document.getElementsByClassName('span-tip')[0];
      if (tip) tip.parentNode.removeChild(tip);
  }

  function setTipSize(spanTip, target) {
    var elemRect = target.getBoundingClientRect();
    var spanSize = spanTip.getBoundingClientRect();

    var spanRoof = document.createElement('div');
    var wideSpan = spanSize.width;
    var heightSpan = spanSize.height;
      spanRoof.className = 'span-roof';
      spanRoof.style.borderLeft = wideSpan/14 + 'px solid transparent';
      spanRoof.style.borderRight = wideSpan/14 + 'px solid transparent';
      spanRoof.style.left = wideSpan/7*3 + 'px';

      if ( elemRect.top > spanSize.height + 7 ) {
        spanRoof.style.borderTop = heightSpan/5 + 'px solid rgba(0, 0, 0, 0.7)';
        spanRoof.style.top = heightSpan + 'px';
        spanTip.style.top = (window.pageYOffset + elemRect.top - (spanSize.height + 5)) + 'px';
      } else {
        spanRoof.style.borderBottom = heightSpan/5 + 'px solid rgba(0, 0, 0, 0.7)';
        spanRoof.style.top = -heightSpan/5 + 'px';
        spanTip.style.top = (window.pageYOffset + elemRect.bottom + 5) + 'px';
      }

      if ( (elemRect.left + (elemRect.width + spanSize.width) / 2) > document.clientWidth ) {
        spanTip.style.left = (document.clientWidth - spansize.width) + 'px';
      } else if ((elemRect.left + (elemRect.width - spanSize.width) / 2) < 0) {
        spanTip.style.left = '0px';
      } else {
        spanTip.style.left = (elemRect.left + (elemRect.width - spanSize.width) / 2) + 'px';
      }
    spanTip.appendChild(spanRoof);
  }


  function HoverIntent(options) {
    var timer = null;
    var on = false;

    options.elem.addEventListener('mouseover', function() {
      if (on === false) {
        timer = setTimeout(function() {
          on = true;
          options.over();
        }, 500);
      }
    });
    options.elem.addEventListener('mouseout', function(event) {
      clearTimeout(timer);
      if (on === true) {
        var target = event.relatedTarget;
          while (target != document.documentElement) {
            if (target == elem) return;
            target = target.parentNode;
          }
          on = false;
          options.out();
      }
    })
  }

  new HoverIntent( {
    elem: elem,
    over: function() {setTipSize( createTip('Help for the clocks'), this.elem )},
    out: deleteTip
  })
})();

(function() {
})();