import sys


def count(n, k):
    seq = (k-1) * [0] + [1, 1]
    ln = k + 1
    c = 0
    for i in range(0, n-1):
        end = (seq[-1]<<1) - seq[0]
        if c == k:
            seq[c] = (seq[c-1]<<1) - seq[c]
            c = 0
        elif c == 0:
            seq[c] = (seq[-1]<<1) - seq[c]
            c += 1
        else:
            seq[c] = (seq[c-1]<<1) - seq[c]
            c += 1
    return seq[c-1 if c != 0 else -1]



print(count(123456, 789))
