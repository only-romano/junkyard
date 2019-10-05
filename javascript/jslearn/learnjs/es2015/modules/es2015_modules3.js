'use strict';

import {one as item1, two, tripple, User, sayHi} from './es2015_modules4';
import * as things from './es2015_modules4';

let user = new User('Vasily');
user.sayHi = sayHi;
user.sayHi();

console.log( things );