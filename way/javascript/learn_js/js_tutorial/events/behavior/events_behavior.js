
document.onclick = function(event) {
    if (!event.target.hasAttribute('data-counter')) return;
  event.target.innerHTML++;
};

document.addEventListener('click', function(event) {
  var id = event.target.getAttribute('data-toggle-id');
    if (id) {
      document.getElementById(id).hidden = !document.getElementById(id).hidden;
    }
});


document.addEventListener('mouseover', function(event) {
  var target = event.target;
  var tip = target.getAttribute('data-tooltip');
    if (tip) {
      var elemRect = target.getBoundingClientRect();
      var spanTip = document.createElement('span');
        spanTip.classList.add('span-tip');
        spanTip.innerHTML = tip;
      document.body.appendChild(spanTip);
      var spanSize = spanTip.getBoundingClientRect();
        if ( elemRect.top > spanSize.height + 7 ) {
          spanTip.style.top = (window.pageYOffset + elemRect.top - (spanSize.height + 5)) + 'px';
        } else {
          spanTip.style.top = (window.pageYOffset + elemRect.bottom + 5) + 'px';
        }

        if ( (elemRect.left + (elemRect.width + spanSize.width) / 2) > document.clientWidth ) {
          spanTip.style.left = (document.clientWidth - spansize.width) + 'px';
        } else if ((elemRect.left + (elemRect.width - spanSize.width) / 2) < 0) {
          spanTip.style.left = '0px';
        } else {
          spanTip.style.left = (elemRect.left + (elemRect.width - spanSize.width) / 2) + 'px';
        }
    }
});


document.addEventListener('mouseout', function(event) {
  var tip = document.getElementsByClassName('span-tip')[0];
    if (tip) {
      tip.parentNode.removeChild(tip);
    }
});