/*
const CountJumps = function (steps, maxJump) {
    let finalCounts = [];
    /*for (let jumps = 0; jumps < maxJump; jumps--) {
        finalCounts += sexyCount(steps, maxJump, steps-maxJump+jumps)
    }
    if (maxJump === 1 || maxJump === 0) {return 1};
    for (let jumps = 0; jumps < maxJump; jumps++) {
        for (let countSteps = 1; countSteps < 
        finalCounts.push()
    }
    for (let countSteps = 1; countSteps < steps; countSteps++) {
        for (let jumps = 1; jumps <= maxJump; jumps++) {
            finalCounts += CountJumps(countSteps, jumps);
        }
    }
    for (let nachiStuff = maxJump; nachiStuff > 0; nachiStuff--) {
        finalCounts += CountJumps(steps, nachiStuff-1)
    }
    return finalCounts;
}

const fibHelp = function (count, number) {
    let counts = [1,1] + [0] * (count-1);
    for (let i = 2; i <= number; i++) {
    }
    return b;
}

console.log(CountJumps(4,2));

/*
k / n   2   3   4   5   6   7
1       1   1   1   1   1   1
2       2   3   5   8   13  21
3       =   4   7   13  24  44
4       =   =   8   15  29  56
5       =   =   =   16  31
6       =   =   =   =   32

(3,3) = (2,3) + (1,3) + (0,3)
(7,3) = (6,3) + (5,3) + (4,3)



*/


const countRabbitWays = (steps, maxJump) => {
    let massSteps = new Array(maxJump);
    massSteps.push(1);
    massSteps.push(1);
    let tempSlice = [];
    while (massSteps.length < maxJump + 1 + steps) {
        tempSlice = massSteps.slice(-maxJump);
        let a = tempSlice.reduce(function(a, b) {return a + b;});
        massSteps.push(a);
    }
    let b = massSteps.pop()
    return b;
};

console.log(countRabbitWays(123, 45));