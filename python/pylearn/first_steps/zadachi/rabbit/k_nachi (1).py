import sys


def count(n, k):
    seq = (k-1) * [0] + [1, 1]
    ln = k + 1
    for i in range(0, n-1):
        end = (seq[-1]<<1) - seq[0]
        for j in range(0, ln - 1):
            seq[j] = seq[j + 1]
        seq[-1] = end
    return seq[-1]

print(count(123456,789))