
const showWays = function(steps, maxJump) {
    let way = newArray(steps);
    let ways = [way.slice()];
    for (let i = steps-1; i > 0; i--) {
        if (way[i-1] < maxJump) {
            let tempWayK = way[i];
            way.splice(i-1, 2, way[i-1] + 1, (tempWayK === 1) ? 0 : 1)
            if (tempWayK > 2) {
                let tempK = tempWayK - 2;
                for (let newI = 1; newI <= tempK; newI++) {
                    way.splice(i+newI, 1, 1);
                }
                i += tempK;
            }
            ways.push(way.slice(0, (tempWayK === 1) ? i : i+1));
            if (tempWayK !== 1) { i += 1 };
        }
        if (way[i-1] === maxJump) {
            let key = i-1;
            while (way[key] === maxJump) {
                key--;
                if (key < 0) { return ways };
            }
            way.splice(key, 1, way[key] + 1)
            let tempK = (maxJump - 1) * ((i-1) - key) - 1 + (way[i] - 1);
            for (let newI = key+1; newI <= i+tempK; newI++) {
                way.splice(newI, 1, 1);
            }
            i += tempK;
            ways.push(way.slice(0, i+1));
            i += 1;
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

let b = showWays(23,23);
console.log(b.length);
