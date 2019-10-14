def countSteps(ladder, jump):
    step = [1, 1] + [None] * (ladder - 1)
    for i in range(2, jump + 1):
        step[i] = step[i-1]*2
    for i in range(jump + 1, ladder + 1):
        step[i] = step[i-1]*2 - step[i-1 -jump]
    return step[ladder]

print(countSteps(7,7))

def countSteps2(ladder, jump):
    step = (jump + 1) * [0] + (ladder-1 - (jump+1))*[0] + [1, 1]
    for i in range(0, ladder+1):
        step[i] = step[i+1]*2 - step[i+1 -jump]
    return step[i]

print(countSteps(7,2))

def count(n, k):
    seq = k*[0] + [1]
    for i in range(0, n):
        elem = sum(seq[-k:])
        seq.append(elem)
    return seq[-1]