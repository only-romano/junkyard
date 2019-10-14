'use strict';

console.profile();
console.time('Execution time took');
let foo = { baz: 'tubular', goo: 'rad' }, bar = 'baz';
console.log(
    "%s theory is %d %s concept. I can only describe it as %s and %s.",
    'string', 1, foo.goo, bar, foo.baz
  )
console.group('Main');
console.info("%s numbers %d, %d and %d","hello",1,2,3);
console.group('1st step')
console.warn("%s numbers %d, %d and %d","hello",1,2,3);
console.group('1.1 step')
console.error("%s numbers %d, %d and %d","hello",1,2,3);
console.groupEnd();
console.groupEnd();

let arr = [1, 2, 3];

console.groupCollapsed('2nd step: Collapsed in browser');
for (let value of arr) {
  console.log(value);
}
console.groupEnd();
console.groupEnd();
console.timeEnd('Execution time took');
console.profileEnd();

for (let char of 'Hello') console.log(char);

let range = { from: 1, to: 5 };
  range[Symbol.iterator] = function() {
    let current = this.from;
    let last = this.to;

    return {
      next() {
        if (current <= last) {
          return {
            done: false,
            value: current++
          };
        } else {
          return {
            done: true
          };
        }
      }
    }

  }

console.log();
for (let num of range) console.log(num);

range = {
  from: 1,
  to: 5,

  [Symbol.iterator]() {
    return this;
  },

  next() {
    if (this.current === undefined) this.current = this.from;
    if (this.current <= this.to) {
      return {
        done: false,
        value: this.current++
      };
    } else {
      delete this.current;
      return { done: true };
    }
  }
};

console.log();
for (let num of range) console.log( num );
console.log()
console.log( Math.max(...range) );

let string = 'Hello';

let iterator = string[Symbol.iterator]();
  while (true) {
    let result = iterator.next();
    if (result.done) break;
    console.log(result.value);
  }