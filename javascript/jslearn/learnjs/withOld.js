/*
var a = 'no';
var b = 'yes';

var obj = {
  a: 10
};

with(obj) {
  console.log( a );
  console.log( b );
}


var width = 'no';
var height = 'no';
var weight = 'no';

var obj = {
  width: 'no',
  height: 'no',
  weight: 10,
  size: {
    width: 5,
    height: 7,
    weight: 'no'
  }
};

with(obj) {
  var cool;
  with(size) {
    cool = width * height;
    console.log( cool, weight )
    weight = 3;
    sex = 'cool'
  }
  console.log( cool / weight );
}

console.log( obj.size.weight );
console.log( sex );  // создана глобальная переменная в констркуции with


var i = 0;

function fast() {
  i++;
}

function slow() {
  with(i) {}
  i++;
}

var time = performance.now();
while (i < 1000000) fast();
alert( "Without with-expression: " +  (performance.now() - time) );

var time = performance.now();
i = 0;
while (i < 1000000) slow();
alert( "With with-expression: " + (performance.now() - time) );

*/

var elem = {
  style: {
    top: 0,
    left: '5px'
  }
}

console.log( elem.style );

with(elem.style) {
  top = '10px';
  left = '20px';
}

console.log( elem.style );


var s = elem.style;

s.top = 0;
s.left = '5px';

console.log( elem.style );


function f() {
  console.log( 'no' );
}

var obj = {
  f: function() {
    console.log( 'yes' );
  }
};

with(obj) {
  f();
}


var a = 1;

obj = {
  b: 2
};

with(obj) {
  var b;
  console.log( a + b );
}