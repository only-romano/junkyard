'use strict';

let one = 1;

let two = 2;
let three = 3;
exports.mass = [one, two, three];;

exports.User = class User {
  constructor(name) {
    this.name = name;
  }
};

exports.sayHi = function sayHi() {
  console.log(`Hello, ${this.name}!`);
}