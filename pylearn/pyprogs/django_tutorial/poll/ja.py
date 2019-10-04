
def p(n, k):
    return sum(map(x, range(n-k, n)))


def x(n):
    if n == 1:
        return 1
    return sum(map(x, range(1, n+1)))

print(p(4, 1))