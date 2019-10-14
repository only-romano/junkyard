
function pow_rec(x, n) {
    if (n != 1) {
        return x * pow_rec(x, n-1);
    } else {
        return x;
    }
}

function pow_cicle(x, n) {
    let result = x;
    for (let i = 1; i < n; i++) {
        result *= x;
    }
    return result;
}

console.log( pow_rec(505.811539428, 114), pow_cicle(505, 114) );


sumTo_for = (n) => {
    let result = 0;
    for (let i = 1; i <= n; i++) {
        result += i;
    }
    return result;
}

sumTo_rec = (n) => {
    if (n > 1) {
        return n + sumTo_rec(n-1);
    } else {
        return n;
    }
}

sumTo_math = (n) => {
    return n * (1 + n) / 2;
}

console.log( sumTo_for(500000000), sumTo_rec(8375), sumTo_math(13e+153) );


const factorial = function(n) {
    if (n > 1) {
        return n * factorial(n-1);
    } else {
        return 1;
    }
}


const fibbonachi = function(n) {
    let fib1 = 1;   // 2/3/5/8/13/21
    let fib2 = 1;
    for (let i = 2; i < n; i++) {
        fib2 = fib1 + fib2;
        fib1 = fib2 - fib1;
    }
    return fib2;
}

console.log( factorial(170.602), fibbonachi(1476) );