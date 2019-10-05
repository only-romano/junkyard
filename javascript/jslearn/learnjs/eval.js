var a = 1;

(function() {
  var a = 2;

  eval('console.log(a)');
})();

console.log( eval('var b = 4 + 11; var c = 1+1; 2 + 2') );

var x = 5;
eval( "console.log(x); x = 10" );
console.log( x );


function globalEval(code) {
  window.execScript ? execScript(code) : window.eval(code);
}

var a = 1;
(function() {
  var a = 2;
  globalEval( 'alert(a)' );  // global - 1
})



var b = 2, c = 3;

var mul = new Function('b, c', 'return c * b;');
console.log( mul(b, c) );

var str = '{ \
  "name": "Vasily", \
  "age": 25 \
}';

var user = eval( '(' + str + ')' );
console.log( user.name );