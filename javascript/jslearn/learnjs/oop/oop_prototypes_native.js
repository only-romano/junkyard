var obj = {};

console.log( obj.toString == Object.prototype.toString );
console.log( obj.__proto__ == Object.prototype );
console.log( obj.__proto__.__proto__ );

function showList() {
  console.log( [].join.call(arguments, ' - ') );
  console.log( Array.prototype.join.call(arguments, ' : ') );
}

showList('Vasily', 'Pavel', 'Maria');

var user = 'Vasily';
user.age = 30;

console.log( user.age );

var number = new Number(22);
var number2 = 22;
console.log( typeof number, typeof number2 );

var zero = new Number(0);
var zero2 = 0;

if (zero) console.log('buuuug');
if (zero2) console.log('never');

String.prototype.repeat = function(times) {
  return new Array(times + 1).join(this);
};

console.log( 'la'.repeat(3) );

Object.prototype.each = function(f) {
  for (var property in this) {
      // if (!this.hasOwnProperty(property)) continue;
    var value = this[property];
    f.call(value, property, value);
  }
}

Object.defineProperty(Object.prototype, 'each', { enumerable: false });

var user = {
  name: 'Vasily',
  age: 25
};

user.each(function(prop, val) { console.log(prop); });

if (!Object.create) {
  Object.create = function(proto) {
    function F() {}
    F.prototype = proto;
    return new F;
  }
}


Function.prototype.defer = function(ms) {
  let self = this;
  return function (...args) {
            function onComplete() {
              self.apply(self, args);
            }
            setTimeout( onComplete, ms);
        }
}

function f() {
  console.log( 'hello' );
}

function func(a, b) {
  console.log( a + b );
}

f.defer(1000)();
func.defer(1000)(1, 2);