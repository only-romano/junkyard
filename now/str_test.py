from time import time
# if size of  less then 300 repeats - add strings, else append
reps = 10
size = 5000
str_char = 'a'
str_short = 'abc'*10
str_long = 'abc'*1000


def tester(func, *args):
    start_time = time()
    for i in range(reps):
        func(*args)
    elapsed_time = time() - start_time
    return elapsed_time

def append():
    res = []
    for x in range(size):
        res.append(cur_st)
    return ''.join(res)

def str_add():
    res = ''
    for x in range(size):
        res += cur_st
    return res

tests = (append, str_add)
strs = (str_char, str_short, str_long)

sum_of = 0
cur_st = ''
els = {}
cur = 0
for st in strs:
    cur += 1
    for test in tests:
        cur_st = st
        el = tester(test)
        sum_of = max(sum_of, el)
        els[test.__name__+str(cur)] = {'time': el}
for el in els:
    els[el]['proc'] = "%2.2f" % (els[el]['time'] / sum_of * 100)
    print("%s => %s%%" % (el, els[el]['proc']))
