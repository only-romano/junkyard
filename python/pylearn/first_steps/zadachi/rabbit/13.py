

def countWays(n, jump):
    step = [1]
    for i in range(1, jump + 1):
        step.append(2**(i-1))
    for i in range(jump + 1, n + 1):
        step.append(sum([step[x] for x in range(0, i)]) - sum([step[x] for x in range(0, i-jump)]))
    return step[n]

print(countWays(22, 11));