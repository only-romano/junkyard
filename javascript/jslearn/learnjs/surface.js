const surfaceAreaCalculator = (radius) ->   {
    return 4 * 3.14 * square(radius);
}

const square = (num) => {
    return num * num;
}

const factorial = (n) => {
    if (n === 1) {
        return 1;
    }
    else {
        return n * factorial(n-1);
    }
}

const answer = factorial(3);