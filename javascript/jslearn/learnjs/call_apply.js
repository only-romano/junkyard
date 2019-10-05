/*
function showFullName() {
  console.log( this. firstName + ' ' + this.lastName);
}

var user = {
  firstName: 'Kato',
  lastName: 'Basiro'
};

showFullName.call(user);


var vasya = {
  firstName: 'Vasily',
  surname: 'Petrov',
  patronym: 'Ivanovich'
};

function showVasily(firstPart, lastPart) {
  console.log( this[firstPart] + ' ' + this[lastPart]  );
}

showVasily.call(vasya, 'firstName', 'surname');
showVasily.call(vasya, 'firstName', 'patronym');


// симмуляция методов массива для объекта
function printArgs() {
  arguments.join = [].join;
  arguments.push = [].push;

  var argStr = arguments.push(4);
  argStr = arguments.join(':');

  console.log( argStr );
}

printArgs(1, 2, 3);


function join(separator) {
  if (!this.length) return '';

  var str = this[0];

  for (var i = 1; i < this.length; i++) {
    str += separator + this[i];
  }

  return str;
}

var obj = {
  0: 'a',
  1: 'b',
  2: 'c',
  length: 3
};

obj.join = join;
console.log( obj.join('; ') );

function printArgs() {
  var join = [].join;

  var argStr = join.call(arguments, ':');  // безопасное использование метода без копирования и возможной замены родного метода

  console.log( argStr );
}

printArgs(1, 2, 3);


function forSlice() {
  var args = [].slice.call(arguments);  // создание массива из объекта arguments

  console.log( args.join(', ') );
}

forSlice('Hello', 'my', 'world!');


var pirate = {
  firstName: 'Luffy',
  surname: 'Monkey',
  patreon: 'D.'
}

function showFullName(firstName, patreon, surname) {
  console.log( this.surname, this.patreon, this.firstName );
}

showFullName.call(pirate, 'firstName', 'surname', 'patreon');  // порядок передачи аргументов не важен (кроме объекта)


var myObj = {
  0: 'one',
  1: 'two',
  2: 'three',
  some: 'no',
  3: 'four',
};

function printMyObj(obj) {

  obj.length = function() {
    var count = 0;

    for (key in obj) {
      if (isFinite(key)) count++;
    }

    return count;
  }();

  var join = []. join;
  return join.call(obj, ' : ');
}

console.log( printMyObj(myObj) );

function f() {
  console.log( this );  // выведет window
}

f.call(null);
console.log();


function g() {
  'use strict'
  console.log( this );
}

g.call(null);


console.log( Math.max(1, 5, 2) );

var arr = [1, 5, 2];
console.log( Math.max.apply(null, arr) );  // при массиве аргументов - .apply(объект, массив аргументов)


var obj = { func: function() {} };

function func() {};

// Значение this:
// - при вызове функции как метода:   this = obj
obj.func
obj['func']

// при обычном вызове:   this = window (ES3) / undefined (ES5)
func();

// в new:   this = {} (новый объект)
new func();

// явное указание:   this = указанный context
func.apply(obj, arr);  // this = obj
func.call(new func(), arr);  // this = {}, созданный new func()

function sum(arr) {
  return arr.reduce(function(a, b) {
    return a + b;
  });
}

console.log( sum([3, 4, 5]));


function mySum() {
  arguments.reduce = [].reduce;
  return arguments.reduce(function(a, b) {
    return a + b;
  });
}

console.log( mySum(12, 13, 14, 15, 16) );

*/

function sumArgs() {

  return [].reduce.call(arguments, function(a, b) {
    return a + b;
  });
}

console.log( sumArgs(4, 5, 6) );
console.log();


function applyAll(func) {
  arguments.slice = [].slice;
  return func.apply(null, arguments.slice(1));
}

console.log( applyAll(Math.max, 2, -2, 3) );
console.log( applyAll(Math.min, 2, -2, 3) );
console.log();

console.log( applyAll(sumArgs, 1, 2, 3) );


function mul() {
  return [].reduce.call(arguments, function(a, b) {
    return a * b;
  });
}


function applyAllNotMine(func) {     // из решения уже взял
  return func.apply(this, [].slice.call(arguments, 1));
}

console.log();
console.log( applyAllNotMine(mul, 2, 3, 4) );