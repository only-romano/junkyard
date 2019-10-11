(function() {
  document.getElementsByTagName('button')[1].onclick = function(e) {

      if (e.ctrlKey || e.metaKey) {
        alert('Mac is happy!');
        return;
      }
      if (!e.altKey || !e.shiftKey) return;

    alert( "Hurray!" );
  }
})();

function fixWhich(e) {
  if (!e.which && e.button) {
    if (e.button & 1) e.which = 1;
    else if (e.button & 4) e.which = 2;
    else if (e.button & 2) e.which = 3;
  }
};


function fixPageXY(e) {
  if (e.pageX == null && e.clientX != null) {
    var html = document.documentElement;
    var body = document.body;

    e.pageX = e.clientX + (html.scrollLeft || body && body.scrollLeft || 0) - (html.clientLeft || 0);
    e.pageY = e.clientY + (html.scrollTop || body && body.scrollTop || 0) - (html.clientTop || 0);

  }
};


(function() {
  var ul = document.getElementsByTagName('ul')[0];
  var lastChoosen;

  ul.addEventListener('click', function(event) {
    if (event.target.nodeName === 'LI') {
      var target = event.target;
      var selected = document.getElementsByClassName('selected');
      var isSeveral = selected.length > 1;
        if (event.ctrlKey || event.metaKey) {
          target.classList.toggle('selected');
          setLastChoosen();
          return;
        }
        if (event.shiftKey && lastChoosen) {
          if (lastChoosen.compareDocumentPosition(target) === 4) {
            while (true) {
              lastChoosen.nextElementSibling.classList.add('selected')
              lastChoosen = lastChoosen.nextElementSibling;
              if (lastChoosen === target) break;
            }
          } else if (lastChoosen.compareDocumentPosition(target) === 2) {
            while (true) {
              lastChoosen.previousElementSibling.classList.add('selected')
              lastChoosen = lastChoosen.previousElementSibling;
              if (lastChoosen === target) break;
            }
          }
          return;
        }

        for (var i = selected.length - 1; i >= 0; i--) {
          if (selected[i] === target && !isSeveral) continue;
          selected[i].classList.toggle('selected');
        }
      target.classList.toggle('selected');
      setLastChoosen();

      function setLastChoosen() {
        for (var i = 0; i < selected.length; i++) {
          if (selected[i] === target) lastChoosen = target;
        }
      }

    }

  });

})();


(function() {
  tree.onclick = function(evt) {
    var evt = evt || event;
    var target = evt.target || evt.srcElement;

    if ( !isOverTitle(evt, target) ) return;

    var node = target.getElementsByTagName('ul')[0];
    if (!node) return;

    node.style.display = node.style.display ? '' : 'none';
    };

  function isOverTitle(evt, li) {
    var titleWrapper = document.createElement('span');
    var titleTextNode = li.firstChild;
    li.insertBefore(titleWrapper, titleTextNode);
    titleWrapper.appendChild(titleTextNode);

    var isClickOnTitle = (document.elementFromPoint(evt.clientX, evt.clientY) == titleWrapper);

    titleWrapper.removeChild(titleWrapper.firstChild);
    li.replaceChild(titleTextNode, titleWrapper);

    return isClickOnTitle;
  }
})();