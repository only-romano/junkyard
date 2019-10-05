
    const newArray = function (n) {
        let mass = []
        for (i = n; i > 0; i--) {
            mass.push(1);
        }
        return mass;
    }

const stepyWays = function (steps, maxJump, ways=[], sumOfJumps=0, tempWay=[]) {
    for (let jump = maxJump; jump > 0; jump--) {
        sumOfJumps += jump;
        if (sumOfJumps === steps) {
            tempWay.push(jump);
            ways.push(tempWay.slice());
            tempWay = [];
            sumOfJumps = 0;
        } else if (sumOfJumps < steps) {
            tempWay.push(jump);
            params = stepyWays(steps, maxJump, ways, sumOfJumps, tempWay);
            ways = params[0]; sumOfJumps = params[1]; tempWay = params[2];
        } else {
            sumOfJumps -= jump;
            jump = steps - sumOfJumps + 1;
        }
    }
    return [ways, sumOfJumps, tempWay];
}

console.log(stepyWays(3, 3));

//      2       s=2     temp=[2]