
let steps = 1;
let maxJump = 1;
let ways = [];


const startCount = function (n, k) {
    steps = n;
    maxJump = k;
    runWays(0);
    return ways;
}


const runWays = function (sumOfJumps, way=[]) {

    if (sumOfJumps < steps) 
        for (let jump = 1; jump <= maxJump; jump++) {
            way.push(jump);
            runWays(sumOfJumps + jump, way);
        } 
    if (sumOfJumps === steps) { ways.push(way) }; 
}


console.log(startCount(22,11));