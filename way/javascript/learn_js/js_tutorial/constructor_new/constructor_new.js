/*
function Animal(name) {  // использование функции как конструктора объектов:
  // this = {};

  // заполнение this:
  this.name = name;
  this.canWalk = true;

  // return this;
}

var animal = new Animal('hedgehog');
console.log( animal );


var kittie = new function() {
  this.name = 'Vasily';
  this.canWalk = true;
};


function BigAnimal() {

  this.name = 'mouse';

  return { name: 'godzilla' };
}

console.log( new BigAnimal );


function LittleAnimal() {

  this.name = 'mouse';

  return 'Godzilla';
}

console.log( new LittleAnimal );


function User(name) {
  this.name = name;

  this.sayHi = function() {
    console.log( 'Hi, my name is... my name is... ma name is... Slim Shady... oops, no.. My name is ' + this.name );
  };
}

var ivan = new User('Ivan');
ivan.sayHi();

function User(firstName, lastName) {

  var phrase = 'Wazzzuuuup';

  function getFullName() {
    return firstName + ' ' + lastName;
  }

  this.sayHi = function() {
    console.log( phrase + ', ' + getFullName() + '!' );
  };
}

var vasya = new User('Vasily', 'Petrov');
vasya.sayHi();


function A() { return vasya };
function B() { return vasya };

var a = new A;
var b = new B;

console.log( a == b );


function Calculator() {

  var num1;
  var num2;

  this.read = function() {
    num1 = +prompt('input first value');
    num2 = +prompt('input second value');
  };

  this.sum = function() {
    return num1 + num2;
  };

  this.mul = function() {
    return num1 * num2;
  };
}

var calculator = new Calculator();
calculator.read();

console.log( 'Summ is ' + calculator.sum() );
console.log( 'Multiply is ' + calculator.mul() );

*/

function Accumulator(startingValue) {

  this.value = startingValue;

  this.read = function() {
    this.value += +prompt('input add value');
  }
}

var accumulator = new Accumulator(1);
accumulator.read();
accumulator.read();
console.log( accumulator.value );


function Calculator() {

  this['+'] = function(a, b) {
    return a + b;
  }

  this['-'] = function(a, b) {
    return a - b;
  }

  this.calculate = function(str) {
    var arr = str.split(' ');
    if (!this[arr[1]]) {
      return 'Method doesn\'t exist';
    } else if (arr.length !== 3) {
      return 'Unexpected numbers of token';
    };
    return this[arr[1]](+arr[0], +arr[2]);
  };

  this.addMethod = function(str, func) {
    this[str] = func;
  };

}

var calc = new Calculator;

console.log( calc.calculate('3 + 7') );


var powerCalc = new Calculator;

powerCalc.addMethod('*', function(a,  b) {
  return a * b;
});

powerCalc.addMethod('/', function(a, b) {
  return a / b;
});

powerCalc.addMethod('**', function(a, b) {
  return Math.pow(a, b);
});

console.log( powerCalc.calculate('2 ** 3') );
console.log( powerCalc.calculate('2 * 3') );
console.log( powerCalc.calculate('2 / 3') );
console.log( powerCalc.calculate('2 z 3') );
console.log( powerCalc.calculate('2 / 3 s') );