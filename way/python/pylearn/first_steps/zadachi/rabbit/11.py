

def countWays(n, jump):
    count = [1, 1] + [0] * (1 + n)
    for i in range(2, jump + 1):
        count[i] = count[i - 1] << 1
    for i in range(jump + 1, n + 1):
        count[i] = (count[i - 1] << 1) - count[i - 1 - jump]
    return count[n]

print(countWays(7, 2))