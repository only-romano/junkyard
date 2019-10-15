var form = document.querySelector('form');

form.addEventListener('click', function(event) {
  event.target.style.backgroundColor = 'yellow';
  alert("target = " + event.target.tagName + ", this = " + this.tagName);
  event.target.style.backgroundColor = '';
}, false);

document.body.addEventListener('click', function() { alert('This Doesn\'t work'); });

var button = document.querySelector('button');

button.addEventListener('click', function(event) {
  alert(this.tagName + " will works");
  event.stopPropagation ? event.stopPropagation() : (event.cancelBubble=true);
});

button.addEventListener('click', function(event) {
  alert(this.tagName + " will works second time after .stopPropagation()");
});

var button2 = document.querySelectorAll('button')[1];

button2.addEventListener('click', function(event) {
  alert(this.tagName + " will works, but next does not cause of .stopImmediatePropagation()");
  event.stopImmediatePropagation();
});

button2.addEventListener('click', function(event) {
  alert(this.tagName + " will not work");
});


var elems = [document.querySelectorAll('form')[1]];
elems.push(document.querySelectorAll('div')[1]);
elems.push(document.querySelectorAll('p')[1]);

for (var i = 0; i < elems.length; i++) {
  elems[i].addEventListener('click', highlightThis, true);
  elems[i].addEventListener('click', highlightThis, false);
}

function highlightThis() {
  console.log(getComputedStyle(this).backgroundColor);
  var b = getComputedStyle(this).backgroundColor;
  this.style.backgroundColor = 'yellow';
  var a = event.currentTarget;
  alert(this.tagName + ' with capture-fased listener (from up to down)');
  if (b !== 'rgb(255, 255, 0)') {
    setTimeout( function() { innerHighlight(a, b) }, 1000 );
  }
}

function innerHighlight(elem, color) {
  console.log( elem, color );
  elem.style.backgroundColor = color;
}