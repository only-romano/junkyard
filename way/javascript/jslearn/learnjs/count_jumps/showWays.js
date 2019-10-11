
const showWays = function(steps, maxJump) {
    let way = newArray(steps);
    let ways = [];
    let tempWay = [];
    ways.push(way);
    for (let i = 1; i < steps; i++) {
        if (way[-i] === 1 && way[-i-1] < maxJump) {
            way.splice(-i, 2, 0, way[-1-1]+1);
            tempWay = way.slice(0, -i);
            ways.push(tempWay);
        }
        if (way[-i] === 2 && way[-i-1] < maxJump) {
            way[-i] -= 1;
            way[-i-1] += 1;
            ways.push(way.slice(0, -i+1));
            i -= 1;
        }
        if (way[-i] > 2 && way[-i-1] < maxJump) {
            let tempK = way[-i] - 2;
            way[-i] -= (tempK + 1);
            way[-i-1] += 1;
            for (let newI = 1; newI <= tempK; newI++) {
                way[-i+newI] = 1;
            }
            i -= tK;
            ways.push(way.slice(0, -i+1));
        }
    }
    return ways;
}

const newArray = function (n) {
    let mass = []
    for (i = n; i > 0; i--) {
        mass.push(1);
    }
    return mass;
}

console.log(showWays(3,3));