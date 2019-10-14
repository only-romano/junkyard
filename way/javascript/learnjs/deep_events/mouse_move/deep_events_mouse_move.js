(function() {
  document.body.onmouseover = document.body.onmouseout = handler;

  function handler(event) {

    function str(el) {
        if (!el) return "null";
      return el.className || el.tagName;
    }

    log.value += event.type + ': ' + 'target = ' + str(event.target) +
                 ', relatedTarget = ' + str(event.relatedTarget) + ';\n';
    log.scrollTop = log.scrollHeight;

    if (event.type == 'mouseover') {
      event.target.style.background = 'pink';
    }
    if (event.type == 'mouseout') {
      event.target.style.background = '';
    }
  }
})();

(function() {
  green.onmouseover = green.onmouseout = green.onmousemove = handler;

  function handler(event) {
    var type = event.type;
      while (type < 11) type += ' ';

    log(type + ": target = " + event.target.id);
    return false;
  }

  function clearText() {
    text.value = '';
    lastMessage = '';
  }

  var lastMessageTime = 0;
  var lastMessage = '';
  var repeatCounter = 1;

  function log(message) {
      if (lastMessageTime == 0) lastMessageTime = new Date();

    var time = new Date();
      if (time - lastMessage > 500) {
        message = '------------------------------\n' + message;
      }

      if (message === lastMessage) {
        repeatCounter++;
          if (repeatCounter == 2) {
            text.value = text.value.trim() + ' x 2\n';
          } else {
            text.value = text.value.slice(0, text.value.lastIndexOf('x') + 1) + repeatCounter + '\n';
          }

      } else {
        repeatCounter = 1;
        text.value += message + '\n';
      }

    text.scrollTop = text.scrollHeight;

    lastMessageTime = time;
    lastMessage = message;
  }
})();

(function() {
  function mouselog(event) {
    text2.value += event.type + ' [target: ' + event.target.className + ']\n';
    text2.scrollTop = text.scrollHeight;
  }

   var blue = document.getElementsByClassName('blue')[0];
   blue.addEventListener('mouseover', function() { mouselog(event) });
   blue.addEventListener('mouseout', function() { mouselog(event) });
})();

(function() {
  function deepLog(event) {
    deepText.value += event.type + ' [target: ' + event.target.id + ']\n';
    deepText.scrollTop = deepText.scrollHeight;
  }

  deepBlue.addEventListener('mouseenter', function() { deepLog(event) })
  deepBlue.addEventListener('mouseleave', function() { deepLog(event) });
})();

(function() {
  var currentElem = null;

  bogua.addEventListener('mouseover', function(event) {
      if (currentElem) return;
    var target = event.target;

    while (target != this) {
      if (target.tagName == 'TD') break;
      target = target.parentNode;
    }
      if (target == this) return;

      target.style.background = 'pink';
      boguaText.value += 'mouseover ' + target.tagName + '\n';
      boguaText.scrollTop = boguaText.scrollHeight;
      currentElem = target;
  });

  bogua.addEventListener('mouseout', function(event) {
      if (!currentElem) return;
    var relatedTarget = event.relatedTarget;
      if (relatedTarget) {
        while (relatedTarget) {
          if (relatedTarget == currentElem) return;
          relatedTarget = relatedTarget.parentNode
        }
      }
      currentElem.style.background = '';
      boguaText.value += 'mouseout ' + currentElem.tagName + '\n';
      boguaText.scrollTop = boguaText.scrollHeight;
      currentElem = null;
  })
})();


(function() {
  function fixRelatedTarget(e) {
    if (e.relatedTarget === undefinded) {
      if (e.type == 'mouseover') e.relatedTarget = e.fromElement;
      if (e.type == 'mouseout') e.relatedTarget = e.toElement;
    }
  }
})();