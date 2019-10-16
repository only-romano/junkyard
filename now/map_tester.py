from time import time
reps = 10000
size = 10000

def tester(func, *args):
    start_time = time()
    for i in range(reps):
        func(*args)
    elapsed_time = time() - start_time
    return elapsed_time

def for_statement():
    res = []
    for x in range(size):
        res.append(abs(x))

def list_comprehension():
    res = [abs(x) for x in range(size)]

def map_func():
    res = list(map(abs, range(size)))

def gen_expression():
    res = list(abs(x) for x in range(size))

tests = (map_func, for_statement, list_comprehension, gen_expression)
sum_of = 0
els = {}
for test in tests:
    el = tester(test)
    sum_of = max(sum_of, el)
    els[test.__name__] = {'time': el}
for el in els:
    els[el]['proc'] = "%2.2f" % (els[el]['time'] / sum_of * 100)
    print("%s => %s%%" % (el, els[el]['proc']))
