# name = input("Input your name: ")
# print("Hello Python from " + name + " again :)")
print("Hello Python again :)")

if 1 < 2:
    print("2 > 1 of course!")

x = 3.9e3
y = 3.9e-3
print(x, y, type(x), x // y, x ** y)

first_num = "2"
second_num = 3
print(int(first_num) + second_num)
print(round(2.0001 + 0.1, 4))

a = 0b101
b = 0o11
c = 0x0a
print("{0} in binary {0:08b} in hex {0:02x} in octal {0:02o}".format(a+b+c))

age = 22
weight = 58
isMarried = False
result = age > 21 and weight == 58 or isMarried
print(result)
