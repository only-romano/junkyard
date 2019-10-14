const countRabbitWays = (steps, maxJump) => {
    let possibleCounts = [1,1];
    for (let i = 2; i <= maxJump; i++) {
        possibleCounts.push(possibleCounts[i-1] * 2);
    }
    for (i = maxJump + 1; i <= steps; i++) {
        possibleCounts.push(possibleCounts[i-1] * 2 - possibleCounts[i-1 - maxJump]);
    }
    return possibleCounts[steps];
}

console.log(countRabbitWays(3, 3));