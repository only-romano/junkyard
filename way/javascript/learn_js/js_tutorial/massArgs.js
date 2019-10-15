/*

function go(a, b) {
    console.log('a='+a+", b="+b);
}

go(1); go(1,2); go(1,2,3);


function sayHi() {
    for (var i = 0; i < arguments.length; i++) {
        console.log( "Hello, " + arguments[i] );
    }
}

sayHi('Vinnie the Pooh', 'Pink Nose');


function f(x) {
    arguments[0] = 5;  // меняется переменная x
    console.log( x, arguments );  // 5

    x = 'yes';
    var args = [];
    for (var i = 0; i < arguments.length; i++) {
        args[i] = arguments[i];
    }

    console.log( arguments[0], args );
}

f(1); f('abbb');


function g(x) {
    'use strict';

    arguments[0] = 5;
    console.log( x, arguments );
}

g(1);

var vasya = {
    age: 21,
    name: 'Vasily',
    surname: 'Petrov'
};

var user = {
    isAdmin: false,
    isEmailConfirmed: true
};

var student = {
    university: 'My university'
};


function copy() {
    var dst = arguments[0];

    for (var i = 1; i < arguments.length; i++) {
        var arg = arguments[i];
        for (var key in arg) {
            dst[key] = arg[key];
        }
    }

    return dst;
}


copy(vasya, user, student);
var userClone = copy({}, user);

console.log( vasya )
console.log( userClone );


function showWarning(width, height, title, contents) {
    width = width || 200;
    height = height || 100;
    if (title === undefined) title = 'Warning';  // позволяет использовать false, 0 и тд
    console.log( width, height, title );
}

showWarning();

function f() {
    console.log( arguments.callee === f );
}

f();


var factorialNFE = function fact(n) {
    return n == 1 ? 1 : n * fact(n-1);
}

var factorialOLDIE = function factOLD(n) {
    return n == 1 ? 1 : n * arguments.callee(n-1);
};

console.log( factorialNFE(6), factorialOLDIE(6) );

var counter = 0;

function f1() {
    if (counter > 1) return arguments.callee.caller;
    console.log( arguments.callee, arguments.callee.caller );
    f2();
}

function f2() {
    console.log( arguments.callee, arguments.callee.caller );
    f3();
}

function f3() {
    console.log( arguments.callee, arguments.callee.caller );
    counter++;
    f1();
}

f1();


function showWarning(options) {
    var width = options.width || 200;
    var heigth = options.heigth || 100;
    var contents = options.contents === undefined ? 'Warning' : options.contents;
    console.log( width, heigth, contents);
}

showWarning({
    contents: 'Function is runnong'
});

var opts = { width: 400, heigth: 200, contents: 'Text' };
showWarning(opts);
opts.contents = 'Different text';
showWarning(opts);

*/

function f(x) {
    return arguments.length ? 1 : 0;
}

console.log( f(undefined), f() );


function sum() {
    var sum = 0;
    for (var i = 0; i < arguments.length; i++) {
        sum += arguments[i];
    }
    return sum;
}

console.log( sum(), sum(1), sum(1, 2), sum(1, 2, 3), sum(1, 2, 3, 4) );