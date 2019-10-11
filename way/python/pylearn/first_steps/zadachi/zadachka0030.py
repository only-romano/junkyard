#! Простые задачки.

# Задачи 40.  Из 16-тиричной в двоичную.


def z40(a):
    return bin(int(a, 16))[2:].replace('b', '')


print(z40('-abc'))

# Задача 41. Из 16-тиричной в десятеричную.


def z41(a):
    return int(a, 16)


print(z41('AB'))
print(z41('-BC'))
