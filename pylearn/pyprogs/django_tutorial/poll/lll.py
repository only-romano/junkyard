import time

start_time = time.time()


def func(x):
    if x < 1:
        return "fuck you"
    valuelist = ['1']
    while x > 0:
        valuelist = newfunc(valuelist)
        x -= 1
    return int(''.join(valuelist))


def newfunc(x):
    counter = 1
    if len(x) == 1:
        return [str(counter), x[0]]
    while counter < len(x):
        if x[counter] == x[0]:
            counter += 1
        else:
            valuelist = [str(counter), x[0]]
            extention = newfunc(x[counter:])
            valuelist.extend(extention)
            return valuelist
    return [str(counter), x[0]]


print(func(25))
print("--- %s seconds ---" % (time.time() - start_time))
