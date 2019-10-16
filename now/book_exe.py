from functools import reduce

def print_one(x):
    print('#1. Print one: %s (%s)' % (x, type(x)))

def adder(*args):
    print('#2. Adder: %s (%s)' % (str(reduce(lambda x,y: x+y, args)), type(args[0])))

def copy_dict(dict):
    print('#3. Copy Dict: %s' % (str({x:dict[x] for x in dict})))


def main():
    print_one('abc'); print_one(1), print_one([1,2,3]), print_one({'a': 1, 'b': 2})
    adder(1,2); adder('a', 'b'); adder([1,2], [3,4]) #, adder({'a':1}, {'b':2})
    copy_dict({'a':1, 'b':2})


if __name__ == '__main__':
    main()
