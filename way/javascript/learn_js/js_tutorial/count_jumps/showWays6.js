
let steps = 1;
let maxJump = 1;
let ways = [];


const startCount = function (n, k) {
    steps = n;
    maxJump = k;
    runWays(0);
    return ways;
}

const runWays_new = function (sumOfJumps, way=[]) {
    let params = new Array(sumOfJumps, way);
    let stack = [params];

    for (let jump = 1; jump <= maxJump; jump++) {


    }
}

const runWays = function (sumOfJumps, way=[]) {
    let params = new Array(sumOfJumps, way);
    let stack = [params];

    while (stack.length > 0) {

        let elem = stack.pop();

        if ( elem[0] === steps ) {
            let c = elem[1].slice()
            ways.push(c);

        }
        if (elem[0] < steps) {
            for (let jump = 1; jump <= maxJump; jump++) {
                let b = elem[0] + jump;
                if (b <= steps) {
                    let d = elem[1].slice()
                    d.push(jump);
                    let soul = new Array(b, d);
                    stack.push(soul);
                }
                if (b === steps) {
                    break;
                }
            }
        }
    };
    return ways;
}
/*
const runWays = function (sumOfJumps, way=[]) {

    if (sumOfJumps < steps) 
        for (let jump = 1; jump <= maxJump; jump++) {
            way.push(jump);
            runWays(sumOfJumps + jump, way);
        } 
    if (sumOfJumps === steps) { ways.push(way) }; 
} */


console.log(startCount(123456,123));