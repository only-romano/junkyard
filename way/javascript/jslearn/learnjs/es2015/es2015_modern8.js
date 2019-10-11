'use strict';

Promise.all([
  (() => 'aa')(),
  (() => 'aaaa')()
]).then(results => {
  console.log( results );
})

const delay = (ms) => {
  return new Promise((resolve) => {
    setTimeout(() => resolve(), ms);
  })
};

delay(1000).then(() => console.log('Hello!'));


let urls = [
  'user.json',
  'guest.json'
];

let chain = Promise.resolve();
let results = [];

urls.forEach(function(url) {
  chain = chain
    .then(() => url)
    .then((result) => results.push(result));
});

chain.then( () => console.log(results) );


function* generateSequence() {
  yield 1;
  yield 2;
  return 3;
}

let generator = generateSequence();
  for(let value of generator) {
    console.log(value);
  }

let one = generator.next();
  for(let value of generator) { //  doesn't work
    console.log(value);
  }
let two = generator.next();
let three = generator.next();

console.group();
console.log(`One: ${JSON.stringify(one)},
Two: ${JSON.stringify(two)},
Three: ${JSON.stringify(three)}`);
console.groupEnd();

function* generateSequence2() {
  yield 1;
  yield 2;
  yield 3;
}

let generator2 = generateSequence2();
  for (let value of generator2) {
    console.log(value);
  }

function* generateSequence3(start, end) {
  for (let i = start; i <= end; i++) yield i;
}

let sequence = [...generateSequence3(2,5)];
console.log(sequence);

function* generateAlphaNum() {
  yield* generateSequence3(48, 57);
  yield* generateSequence3(65, 90);
  yield* generateSequence3(97,122);
}

let str = '';
  for (let code of generateAlphaNum()) str += String.fromCharCode(code);

console.log( str );

function* gen() {
  let ask1 = yield '2 + 2?';
    console.log( ask1 );
  let ask2 = yield '3 * 3?';
    console.log( ask2 );
  try {
    let result = yield 'zzzz';
  } catch(e) {
    console.log( e.message );
  }
}

let gener = gen();
console.log( gener.next().value );
console.log( gener.next(4).value );
console.log( gener.next(9).value );
console.log( gener.throw(new Error("No answer")) );



console.log('wait');
function* wait(ms) {
  yield new Promise(resolve => setTimeout(resolve, ms));
  yield console.log('ok');
}
let s = wait(3000);
s.next();
s.next();