

def countWays(n, jump):
    if n == 1 or n == 0:
        return 1
    return countWays(n-1, jump) * 2 - countWays(n - 1 - jump, jump)
    """
    count = [1, 1] + [0] * (1 + n)
    for i in range(2, jump + 1):
        count[i] = count[i - 1] * 2
    for i in range(jump + 1, n + 1):
        count[i] = (count[i - 1] * 2) - count[i - 1 - jump]
    return count[n]
    """

print(countWays(4, 3))