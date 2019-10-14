/*
var user = {
  name: "Vasily"
};
console.log( user );
user = null;
console.log( user );


var vasya = {};
var petya = {};
vasya.friend = petya;
petya.friend = vasya;
console.log( vasya, petya );

vasya = petya = null;
console.log( vasya, petya );


function marry(man, woman) {
  woman.husband = man;
  man.wife = woman;

  return {
    father: man,
    mother: woman
  }
}

var family = marry({
  name: "Vasily"
}, {
  name: "Maria"
});
console.log( family );

delete family.father;
console.log();
console.log( family );

delete family.mother.husband;
console.log( family );

// window.family = null; удалит весь объект в  целом, так как ссылки в корне на него нет.


function showTime() {
  console.log( new Date() );  // объект будет создан и сразу умрёт
}

showTime();

function f() {
  var value = 123;

  function g() {}
}

f();
// во время выполнения функции f() её объект переменных { value: 123, g: function } находится в текущем
// стеке выполнения, поэтому жив.  По окончанию, объект станет недостижим и будет убран из памяти вместе
// с остальными локальными переменными.


function h() {
  var value = 123;

  function g() {}

  return g;
}

var g = h();
// В скрытом свойстве g.[[Scope]] находится ссылка на объект переменных, в котором была создана g.
// Поэтому этот объект переменных останется в памяти, а в нём – и value.


function j() {
  var value = Math.random();

  return function() { return value };
}

var arr = [j(), j(), j()];
// Если f() будет вызываться много раз, а полученные функции будут сохраняться, например, складываться
// в массив, то будут сохраняться и объекты LexicalEnvironment с соответствующими значениями value.


function k() {
  var value = 123;

  function g() {}

  return g;
}

var g = f();  // функция g жива, а значит и объект переменных f.
g = null  // теперь память будет очищена

var value = 'Surprise motherfucker!'

function f() {
  var value = Math.random();

  function g() {
    debugger;
  }

  return g;
}

var g = f()
g();

*/

function sumTo(n) {
  var result = 0;
  for (var i = 1; i <= n; i++) {
    result += i;
  }
  return result;
}

function sumToRec(n) {
  return n == 1 ? 1 : n + sumToRec(n-1);
}

var timeLoop = performance.now();
for (var i = 1; i < 1000; i++) sumTo(1000);
timeLoop = performance.now() - timeLoop;

var timeRecursion = performance.now();
for (var i = 1; i < 1000; i++) sumToRec(1000);
timeRecursion = performance.now() - timeRecursion;

alert ( "Difference is in " + (timeRecursion / timeLoop) + " times" );