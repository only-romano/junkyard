/*

console.log( 0xFF, 1e-5, 1.8e308, Infinity-Infinity  );
console.log( isNaN( s = function() {let tu = 1; return tu} ), isNaN( s() ))

let p = parseInt('s123');
if (p !== p) console.log( isNaN(p), "parseInt('s123') = " + p );

let inf = Infinity;
let num = 123456;
console.log( isFinite(p), isFinite(num), isFinite(inf) );

console.log( +"   -12", +"12test", +" \n 34  \n", +"", +" 1 2" );

let pInt = parseInt('aff12', 16);
let pFlo = parseFloat('127.1.1.1');
console.log(pInt, pFlo);

if (isNaN( isNaN(false) ? undefined : isNaN(null) ? '' : isNaN( parseInt('s15', 28) ) ? 'duH' : true )) {
    console.log( 'Not a Number, cococo' );
} else {
    console.log( 'Num is num, life is life' );
}

function isNumeric(n) {
    return !isNum(parseFloat(n)) && isFinite(n);
}

var num = 9876543210;   // приведение к другим системам счисления с помощью toСтрока
console.log( num.toString(16), num.toString(2), num.toString(36) );

num = [1.5, 2.1, 3.9];  // округление с помощью Math пол-потолок-вокруг
num.forEach( function(n) {
    console.log( Math.floor(n), Math.ceil(n), Math.round(n) );
});

num = 12,3;  // побитовые операции для округления
console.log( ~~num, num ^ 0, (num + num) / num ^ 0 );

var nunum = 3.456789;  // округление до заданной точности
console.log( Math.round(nunum * 100) / 100 );  // 3.456789 -> 345.6789 -> 346 -> 3.46

var n = 12.34567;  // округление до фиксированной точности, результат в виде строки
console.log( n.toFixed(1), n.toFixed(2), +n.toFixed(6) );

var price = 6.35;  // неточности при вычислениях
console.log( price.toFixed(1), Math.round(price * 10) / 10 );
console.log( 0.1.toFixed(20), 0.2.toFixed(20) );
console.log( 9999999999999999 );

console.log( ((0.1 * 10) + (0.2 * 10)) / 10 );  // как драться с неточностями, часть 1
console.log( +(0.1 + 0.2).toFixed(10) );  // КДсН, часть 2

var degree = 1;  // a little bit of trigonometrics
var y = 0.5;
console.log( Math.acos(degree), Math.asin(degree), Math.atan(degree), Math.atan2(degree, y) );
console.log( Math.sin(y), Math.cos(y), Math.tan(y) )

var x = 1 / 3;
console.log( Math.sqrt(x), Math.log(x), Math.pow(x, -3/5), Math.abs(-x), Math.exp(x) )

var y = 1 / 2;
var z = 1;  // random возвращает псевдослучайное число между 0 и 1
console.log( Math.max(x, y, z), Math.min(x, y, z), Math.random() )

var number = 123456789;
console.log( number.toLocaleString() );

console.log( 6.35.toFixed(1), 6.35.toFixed(20) ); // funny numbers

var price1 = '0.10$';
var price2 = '0.20$';
console.log( parseFloat(price1) + parseFloat(price2) + ' $' );
console.log( +(parseFloat(price1) + parseFloat(price2)).toFixed(10) + ' $'); // who's da man?

var i = 0;
while (+i.toFixed(3) != 10) {  // альтернатива  (i != 10.0)
    i += 0.2;  // ошибка из-за того что float 0.2 содержит в себе погрешность с 10
};
console.log( i.toFixed(20) );

function getDecimal(num) {
    var dec = num.toString();
    var dot = dec.indexOf('.');
    return dot === -1 ? 0 : +dec.slice(dot);
}

console.log( getDecimal(12.345), getDecimal(1.2), getDecimal(-1.25) );

function fibBinet(n) {
    return Math.round(((1 + Math.sqrt(5)) / 2) ** n / Math.sqrt(5));
}

console.log(fibBinet(77));

*/

function randomToMax(max) {
    var random = Math.random() * max;
    return random === max ? max - 1e-15 : random ;
}

function randomFromMinToMax(min, max) {
    var random = min + Math.random() * (max - min);
    return random === max ? max - 1e-15 : random;
}

function randomInteger(min, max) {
    return Math.round(min + Math.random() * (max - min))
}

for (var i = 0; i < 15; i++) {
    console.log(randomToMax(5), randomFromMinToMax(5, 10), randomInteger(1, 10), randomIntegerRight(1, 10));
}


function randomIntegerRight(min, max) {
    return Math.floor(min + Math.random() * (max + 1 - min))
}