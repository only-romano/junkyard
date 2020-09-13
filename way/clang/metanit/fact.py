def fact(x):
    res = 1
    while (x):
        res *= x
        x -= 1
    return res

print(fact(int(input("Input num: "))))
