(function() {
  let placeholder = document.getElementById('placeholder');
  placeholder.onclick = function() { input.focus() };
  input.onfocus = function() {
    placeholder.parentNode && placeholder.parentNode.removeChild(placeholder);
  };
})();



  let capsLockEnabled = null;
  document.documentElement.addEventListener('keypress', function(e) {
    let chr = getChar(e);
      if (!chr) return;
      if (chr.toLowerCase() == chr.toUpperCase()) return;
    capsLockEnabled = (chr.toLowerCase() == chr && e.shiftKey) ||
                      (chr.toUpperCase() == chr && !e.shiftKey);
  })

  if (navigator.platform.substr(0, 3) != 'Mac') {
    document.onkeydown = function(e) {
      if (e.keyCode == 20 && capsLockEnabled !== null) {
        capsLockEnabled = !capsLockEnabled;
      }
    };
  }

  function getChar(event) {
      if (event.which == null) {
        if (event.keyCode < 32) return null;
        return String.fromCharCode(event.keyCode) // IE
      }

      if (event.which != 0 && event.charCode != 0) {
        if (event.which < 32) return null;
        return String.fromCharCode(event.which) // остальные
      }

      return null; // специальная клавиша
    }

function checkCapsWarning() {
  document.getElementById('capsIndicator').style.display = capsLockEnabled ? 'block' : 'none';
}

function removeCapsWarning() {
  document.getElementById('capsIndicator').style.display = 'none';
}