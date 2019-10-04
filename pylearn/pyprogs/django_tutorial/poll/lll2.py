import time
from functools import reduce
from itertools import groupby

start_time = time.time()


def look_and_say(x):
    if x < 1:
        return "fuck you"
    value = '1'
    while x > 0:
        value = reduce((lambda z, y: z + ''.join(y)),
                       list(map(lambda y: [str(len(y)), y[0]],
                                [list(b) for a, b in groupby(value)])), '')
        x -= 1
    return value

results = look_and_say(8)
print(str(len(results)) + ' symbols\n' + results)
print("--- {} seconds ---".format(time.time() - start_time))
