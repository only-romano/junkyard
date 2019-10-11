/*[[1, 1, 1, 1, 1], [2, 1, 1, 1], [2, 2, 1], ...]
5,4

1-1-1-1-1, 1-1-1-2,  1-1-2-1, 1-2-1-1, 1-2-2, 2-1-1-1, 2-1-2, 2-2-1, 1-1-3, 1-3-1, 3-1



start = Array(k,[1])

k / n   2   3   4   5   6   7
1       1   1   1   1   1   1
2       2   3   5   8   13  21
3       =   4   7   13  24  44
4       =   =   8   15  29  56
5       =   =   =   16  31
6       =   =   =   =   32


2,2

1,1
+  2

3,3

1,1,1
+  1,2  ;  2,1
+  3

4,4

1,1,1,1
+  1,1,2  ;  1,2,1  ;  2,1,1  /  +  /  2,2  /
+  1,3  ;  3,1
+  4

steps =                                         now     3
currentMass = [1,1,1]                           now     [1,1,1]
currentJump = (let i = 2; i <= maxJump; i--);    now     2
nextStep = steps - currentJump                  now     3-2 = 1
    if (nextStep === 0) {resultMass.push(currentmass)}
(3,3) 
currentMass = [1,1,1], currentJump = 2; nextStep = 3-2 = 1;
tempMass[currentJump, nextStep/]
resultMass = [[1,1,1]; []]



1,1,1 -> 1,2 -> 2,1 -> 3
1,1,1,1 -> 1,1,2 -> 1,2,1 -> 1,3 -> 2-1-1 -> 2,2 -> 3,1 -> 4
1,1,1,1,1 -> 1,1,1,2, ->1,1,2,1 -> 1,1,3 -> 1,2,1,1 -> 1,2,2 -> 1,3,1 -> 1,4 -> 2,1,1,1 -> 2,1,2 -> 2,2,1 -> 2,3 ->
    3,1,1 -> 3,2 -> 4,1 -> 5

1,1,1,1,1
1,1,1,2
1,1,2,1
1,1,3
1,2,1,1
1,2,2
1,3,1
1,4
2,1,1,1
2,1,2
2,2,1
2,3
3,1,1
3.2
4,1
5


for (let i = 1; i <= maxJump; i++) {
    mass.join(i);
    sumOfJumps += i;
    if (steps === sumOfJumps) {
        variants.join(mass);
        return variants
    }
}
if (steps == sumOfSteps + currentjump) {
    +
}


let mass = new Array(n)
let sumOfArray = 0
let vars = []
for (let i = n-1; i >= 0; i--) {
    for (let j = 1; j <= maxJump; j++) {
        mass[i] = j;
        sumOfArray += j;
        if (sumOfArray)
    };

}

tempMass = [1] * n
sumOfMass = steps


const newArray = function (n) {
    let mass = []
    for (i = n; i > 0; i--) {
        mass.push(1);
    }
}

for (let index = n-1; index >= 0; index--) {
    if (steps)
    for (let jump = 2; jump <= maxJump; jump++) {
        
    }
}


1,1,1 - 1,1,2 - 1,1,3 - 1,2,1

let steps = 7;
let currentSteps = steps;  // (default)
let maxJump = 3;
let currentJump = 1;  // (default)
params = [steps, maxJump, currentSteps, currentJump]

const showWays = function (params) {
    let newVariant = [];
    for (let counter = 0; counter < params[2]; counter++) {
        newVariant.push(1);
    }
    for (let jumpIndex = params[2] - 1; jumpIndex >= 0; jumpIndex)
    return params.slice(4)
}

params = [steps, maxJump, tempVarm, sumOfJumps]
[4, 3, [], 0]

3
params[2] = 
params[3] = 3

for (let jump = params[1]; jump > 0; jump--) {
    params[3] += jump;
    if (params[3] === params[0]) {
        params[2].push(jump);
        params.push(params[2]);
        params[2] = [];
        params[3] = 0;
        continue;
    } else if (params[3] > steps) {
        params[3] -= jump;
        continue;
    } else {
        params[2].push(jump);
        CountWays(params);
    }
}








for (let jumpIndex = steps-1; jumpIndex >= 0; jumpIndex--) {
    let tempWay = new Array(steps);
    for (let jump = 1; jump <= maxJump; jump++) {
        tempWay[jumpIndex] = jump;
        let sumWay = tempWay.reduce(function(a,b) {return a+b;});
        if (sumWay === variants[0] && !(variants.includes(tempWay)) {
            variants.push(tempWay)
        }
    }

}


    for jumpIndex in range(0, steps):
        tempVariant = [1]*steps
        for jump in range(2, maxJump+1):
            tempVariant[jumpIndex] = jump
            if sum(tempVariant) == variants[0] and tempVariant not in variants:
                variants.append(tempVariant)
    return variants


5,5

1,1,1,1,1
+  1,1,1,2  ;  1,1,2,1  ;  1,2,1,1  ;  2,1,1,1  /  +  /  1,2,2  ;  2,1,2  ;  2,2,1  /
+  1,1,3  ;  1,3,1  ;  3,1,1  /  +  /  2,3  ;  3,2  /
+  1,4  /  4,1
+  5

if (currentMass[-i] < currentK && currentMass.length > currentK) {

}
