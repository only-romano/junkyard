'use strict'

let apples = 5;

if (true) {
  let apples = 10;
  console.log(apples);
}
console.log(apples);

const apple = 5;
// apple = 10; - Error

let [firstName, lastName] = ['Sexy', 'Day'];
console.log( firstName, lastName);

let [, , title] = 'Julius Cesar Imperor of Rome'.split(' ');
console.log( title );

let [name, surame, ...rest] = 'Julius Cesar The Emperor of Rome'.split(' ');
console.log( name, surame, rest);

[name, surame=defaultLastName()] = []
console.log(name, surame);

function defaultLastName() {
  return Date.now() + '-visitor';
}

let options = {
  title: 'Menu',
  width: 100,
  height: 200
};

let {title: tit, width, height, macaron:pool='sex'} = options;
console.log(tit, width, height, pool);

let a, b;
({a,b} = {a:5, b:6});
console.log(a,b);

let newOptions = {
  size: {
    width: 100,
    height: 200
  },
  items: ['Donut', 'Picake']
}

let { newTitle="Menu", size: {width: newWidth, height: newHeight},
    items:[item1, item2] } = newOptions;
console.log(newTitle, newWidth, newHeight, item1, item2);

let numbers = [2, 3, 15];
let max = Math.max(...numbers);
console.log(max);

function showMenu({title="Menu", width:w=100, height:h=200} = {}) {
  console.log( title + ' ' + w + ' ' + h);
}

showMenu();

function f() {}
let g = function g() {};
console.log(f.name, g.name);

let user = {
  sayHi: function() {}
};
console.log(user.sayHi.name);

if (true) {
  sayHi();
  function sayHi() {
    console.log('Hi')
  }
}

try {
  sayHi();
} catch (e) {
  console.log(e.message);
}

let inc = x => x+1;
console.log( inc(21) );
let sum = (a, b) => a + b;
console.log( sum(5,6) );
let getTime = () => new Date().getHours() + ':' + new Date().getMinutes();
console.log( getTime() );

let arr = [5,8,3];
let sorted = arr.sort( (a,b) => a - b );
console.log( sorted );

let group = {
  title: 'Owr course',
  students: ['Vasily', 'Petro', 'Daria'],
  showList: function() {
    this.students.forEach( student => console.log (this.title + ': ' + student) )
  }
}

group.showList();

function f() {
  let showArg = () => console.log(arguments[0]);
  showArg();
}

f(1);

function defer(f, ms) {
  return function() {
    setTimeout( () => f.apply(this, arguments), ms );
  }
}

function sayHi(who) {
  console.log( 'Hello, ' + who );
}

let sayHiDeferred = defer(sayHi, 2000);
sayHiDeferred('Vasily');