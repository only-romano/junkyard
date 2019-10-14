#! Максимкально быстро поменять переменные.

a = 1
b = 1
c = a
a, b = b, c
print(a, b)

a = 1
b = 2
a, b = b, a
print(a, b)

a = 1
b = 2


a = b + a   # - 2 - 1 = 1
b = a - b   # 2 + 1
a = a - b   # 2 + 1

print(a, b)
