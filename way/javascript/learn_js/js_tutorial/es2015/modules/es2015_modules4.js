'use strict';

export let one = 1;

let two = 2;
let three = 3;
export {two, three as tripple};

export class User {
  constructor(name) {
    this.name = name;
  }
};

export function sayHi() {
  alert(`Hello, ${this.name || 'anonymous'}!`);
}