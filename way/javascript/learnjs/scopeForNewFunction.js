'use strict';

/*
// при создании функции с использованием new Function, ее свойство [[Scope]] ссылается не на текущий LexicalEnvironment, а на window

var a = 1;

function getFunc() {
    var a = 2;

    var func = new Function('', 'alert(a)');  // global a, 1

    return func;
}

getFunc()();


var b = 1;

function innerScope() {
    var b = 3;

    var func = function() { alert(b) };  // Lexical Environment b, 3

    return func;
}

innerScope()();


var sum = new Function('c, d', 'alert(c+d)');

var c = 10;
var d = 7;
alert( sum(c, d) );
*/

for (var i = 1; i <= 5; i++) {
    setTimeout( function timer() {
        console.log( i );
    }, 1000);
}

for (let j = 1; j <= 5; j++) {
    setTimeout( function timer() {
        console.log( j );
    }, 1000);
}


let arr = [];
for (let k = 0; k <= 5; k++) {
    function myFunc() {
        return function retFunc() {
            console.log("k = ", k);
            return k;
        }
    }
    arr[k] = myFunc()();
}

console.log( arr );