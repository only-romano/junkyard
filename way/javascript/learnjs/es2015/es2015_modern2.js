'use strict';

let apples = 2;
let oranges = 3;
let str = `Back
  strings
    are awesome!`;

console.log(str);
console.log(`${apples} + ${oranges} = ${apples + oranges}`);

let sabStr = func`Sum of ${apples} + ${oranges} =\n ${apples + oranges}!`;

function func(string, ...values) {
  console.log(JSON.stringify(string));
  console.log(JSON.stringify(string.raw));
  console.log(JSON.stringify(values));
}

function strings(string, ...values) {
  let str = '';
  for (let i = 0; i < values.length; i++) {
    str += string[i];
    str += values[i];
  }

  str += string[string.length - 1];
  return str;
}
console.log( strings`Sum of ${apples} + ${oranges} = ${apples + oranges}!` );

let messages = { 'Hello, {0}!': 'Hello, {0}!' };

function i18n(strings, ...values) {
  let pattern = '';
    for (let i = 0; i < values.length; i++) pattern += strings[i] + '{' + i + '}';
    pattern += strings[strings.length - 1];

  let translated = messages[pattern];
  return translated.replace(/\{(\d)\}/g, (s, num) => values[num]);
}

let name = 'Vasily';
console.log( i18n`Hello, ${name}!` );

console.log( '我'.length );
console.log( '𩷶'.length );
console.log( '𝒳'.length );
console.log( '😂'.length );

console.log( '𝒳'.charCodeAt(0) + ' ' + '𝒳'.charCodeAt(1) );
console.log( '𝒳'.codePointAt(0) );

console.dir( (String.fromCodePoint(119987)) );
console.log( String.fromCharCode(119987) );

console.log("\u2033");
console.log("\u20331")
console.log("\u{20331}")

console.log("S\u0307\u0323".normalize());
console.log("\u1e68");


let strOwner = 'include js';
let strOwned = 'js';

console.log('Includes: ' + strOwner.includes(strOwned));
console.log('End with: ' + strOwner.endsWith(strOwned));
console.log('Starts with: ' + strOwner.startsWith(strOwned));
console.log('Repeat times: ' + strOwned.repeat(3));