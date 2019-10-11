'use strict';

let name = 'Vasily';
let isAdmin = true;

let user = {
  name,
  isAdmin
}

console.log( JSON.stringify(user) );

let propName = 'firstName';

user = {
  [propName]: 'Vasily'
};

console.log( user.firstName );


let [a, b, c] = ['My ', 'Green ', 'Crocodile!'];
user = {
  [(a + b + c).toLowerCase()]: 'Eugenius'
};

console.log( user['my green crocodile!'] );

user = {name: "Vasily"};
let visitor = { isAdmin: false, visits: true };
let admin = { isAdmin: true };

Object.assign(user, visitor, admin);
console.log( JSON.stringify(user) );

let clone = Object.assign({}, user);
console.log( JSON.stringify(clone) );

console.log( Object.is(+0, -0) );
console.log( +0 === -0);
console.log( Object.is(NaN, NaN) );
console.log( NaN === NaN );

name = 'Vasily';
let surname = 'Petrov';
let methodName = 'getFirstName';

user = {
  name,
  surname,
  sayHi() { console.log(this.name); },
  get fullName() {
    return `${name} ${surname}`;
  },
  [methodName]() {
    return name;
  }
};

user.sayHi();
console.log( user.fullName );
console.log( user.getFirstName());

let animal = {
  walk() {
    console.log( `I am walking` );
  }
};

let rabbit = {
  __proto__: animal,
  walk() {
    super.walk();
  }
};

let walk = rabbit.walk;
rabbit.walk();
walk();