(function textStand() {
  let kinput = document.getElementById('kinput');
  let area = document.getElementById('area');
    kinput.onkeydown = kinput.onkeyup = kinput.onkeypress = handle;

  let lastTime = Date.now();

  function handle(e) {
      if (form.elements[e.type + 'Ignore'].checked) return;

    let text = e.type + ' keyCode=' + e.keyCode + ' which=' + e.which + ' charCode=' + e.charCode +
               ' char=' + String.fromCharCode(e.keyCode || e.charCode) + (e.shiftKey ? ' +shift' : '') +
               (e.ctrlKey ? ' +ctrl' : '') + (e.metaKey ? ' +meta' : '') + (e.altKey ? ' +alt' : '') + '\n';

      if (area.value && Date.now() - lastTime > 250) area.value += new Array(81).join('-') + '\n';

    lastTime = Date.now();
      area.value += text;
      area.scrollTop = area.scrollHeight;

      if (form.elements[e.type + 'Stop'].checked) e.preventDefault();
  }
})();


function getChar(event) {
    if (event.which == null) {
      if (event.keyCode < 32) return null;
      return String.fromCharCode(event.keyCode);
    }

    if (event.which != 0 && event.charCode != 0) {
      if (event.which < 32) return null;
      return String.fromCharCode(event.which);
    }
}

(function() {
  document.getElementById('only-upper').onkeypress = function(e) {
      if (e.ctrlKey || e.altKey || e.metaKey) return;
    let char = getChar(e);
      if (!char) return;

    this.value = char.toUpperCase();

    return false;
  }
})();

console.log( navigator.connection );

(function() {
  document.getElementById('only-numbers').onkeypress = function(e) {
    let char = event.which || event.keyCode;
      if (char < 32) return;
      if ( char > 47 && char < 58) this.value += String.fromCharCode(char);
    return false;
  }
})();

(function() {

  function runOnKeys(func, ...arg) {
    let pressed = arg.slice();

    window.addEventListener('keydown', handle);
    window.addEventListener('keyup', handle2);

    function handle(e) {
      if (~arg.indexOf(e.keyCode)) {
        let index = pressed.indexOf(e.keyCode);
        ~index ? pressed.splice(index, 1) : '';
        if (pressed.length == 0) { 
          func();
          pressed = arg.slice();
        };
      };
    }

    function handle2(e) {
      let index = arg.indexOf(e.keyCode);
      if (~index) {
        !~pressed.indexOf(e.keyCode) ? pressed.push(e.keyCode) : '';
      }
      console.log(pressed);
    }
  }

  runOnKeys( function() { alert('Hello!') }, 'Q'.charCodeAt(0), 'W'.charCodeAt(0) );
})();