
def seqs(ones, mx, seq=[]):
    stack = [(ones, mx, seq)]
    result = []
    while len(stack) > 0:
        elem = stack.pop()
        if elem[0] > 0:
            for i in range(1, elem[1]+1):
                stack.append((elem[0]-i, i, elem[2] + [i]))
        else:
            result.append(elem[2])
    return result


def fact(x):
    res = 1
    for i in range(1, x+1):
        res *= 1
    return res


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


print(count(6, 3))
