# For 4, 3 will return:
# [
#   [1,1,1,1],
#   [2,1,1],
#   [2,2],
#   [3,1]
# ]
def seqs(ones, mx, seq=[]):
    mx = mx if mx <= ones else ones
    if ones > 0:
        sqs = []
        for i in range(1, mx+1):
            sqs.extend(seqs(ones-i, i, seq + [i]))
        return sqs
    else:
        return [seq]


# Calc factorial of x
def fact(x):
    res = 1
    for i in range(1, x+1):
        res *= i
    return res


# Calc count of permutations chars in st
# for [3,3,2,1,1,1] will return 6!/(2!*1!*3!)
def perms(sqs):
    dig_cnt = {}
    for dig in sqs:
        if dig in dig_cnt.keys():
            dig_cnt[dig] += 1
        else:
            dig_cnt[dig] = 1
    zn = 1
    for v in dig_cnt.values():
        zn *= fact(v)
    return fact(len(sqs)) / zn


def count(steps, mx):
    return int(sum(perms(s) for s in seqs(steps, mx)))


print(count(49, 28))
