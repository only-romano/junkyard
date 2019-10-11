import time
from functools import reduce
from itertools import groupby

start_time = time.time()


def look_and_say(x):
    value = '1'
    while x > 0:
        value = reduce(lambda acc, it: acc + ''.join(it), ((str(len(list(group))), key) for key, group in groupby(value)), '')
        x -= 1
    return value

results = look_and_say(46)
print(str(len(results)) + ' symbols\n' + results)
print(f"-— {time.time() - start_time} seconds —-")
