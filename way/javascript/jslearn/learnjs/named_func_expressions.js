
let g = function factorial(n) {
    return n ? n * factorial(n-1) : 1;
};

let f = g;
g = null;

console.log( f(170) );

// НАШЁЛ, НАКОНЕЦ, ЧТОБЫ ПО ДЕФОЛТУ СПЭЙСЫ ВМЕСТО ТАБОВ СТАВИЛИСЬ. АЛЛЕЛУЙЯ.

function h() { return 1.7976e+308; }
(function i() { return 1; });   // error

console.log( h(), /*i()*/ );
