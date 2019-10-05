
area.onmousedown = function(e) { this.value += '\nmousedown\n'; this.scrollTop = this.scrollHeight; };
area.onmouseup = function(e) { this.value += 'mouseup\n'; this.scrollTop = this.scrollHeight; };
area.onclick = function(e) { this.value += 'click\n'; this.scrollTop = this.scrollHeight; };

elem.focus();

button.onclick = function () {
  text.value += ' ->to onclick ';
  text.focus();

  text.value += ' from onclick -> ';
}

text.onfocus = function() {
  text.value += ' !focus! ';
}

buttonTimeout.onclick = function () {
  text.value += ' ->to onclick ';

  setTimeout( function() { text.focus(); }, 0);

  text.value += ' from onclick -> ';
}