def count(n, k):
    seq = k*[0] + [1]
    for i in range(0, n):
        elem = sum(seq[-k:])
        seq.append(elem)
    return seq[-1]


print(count(7, 5))
