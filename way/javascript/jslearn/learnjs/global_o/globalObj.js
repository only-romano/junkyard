'use strict';
/*
В JavaScript все глобальные переменные и функции являются свойствами специального объекта,
который называется "глобальный объект" ( global object );
*/
alert( 'c' in window);
alert(a);
alert(f);
alert(g);
// alert(z); - ошибка, т.к. переменная 'z' даже в старом стандарте была бы создана только в момент присваивания.
// window = { f: function, a: undefined, b: undefined, c: undefined, g: undefined }
var a = 5;
// window = { f: function, a: 5, b: undefined, c: undefined, g: undefined }
alert( window.a );
window.b = 17;
// window = { f: function, a: 5, b: 17, c: undefined, g: undefined }
alert( b );

/*
Порядок инициализации скрипта:
1) объявленные функции (создаются сразу работающими);
2) объявление переменных, на момент инициализации они равны undefined;
3) присваивание значений (=) переменных построчно;
*/

var c = 5;
// window = { f: function, a: 5, b: 17, c: 5, g: undefined }

function f(arg) { /*...*/ };
// без изменений

var g = function(arg) { /* ... */ };
// window = { f: function, a: 5, b: 17, c: 5, g: function }

//z = 66;

var i = 10;

// for, while, if не влияют на видимость переменных
for (var i = 0; i < 20; i++){
    c++;
}

alert(i, c);
var i = 5;

if ('dum' in window) {
    var dum = 1;
}
alert( dum )  // 1

if('damn' in window) {
    damn = 1
}
// alert( damn )  error

if('badums' in window) {
    badums = 1;
}
var badums;
alert(badums);