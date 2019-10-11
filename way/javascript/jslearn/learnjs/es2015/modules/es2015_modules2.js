'use strict';

let a = require('./es2015_modules').mass;
console.log( a );

let user = new (require('./es2015_modules').User)('Vasily');
user.sayHi = require('./es2015_modules').sayHi;
user.sayHi();