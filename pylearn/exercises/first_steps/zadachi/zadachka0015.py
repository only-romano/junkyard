#! Простые задачки.


# 1.  Даны два целых  числа, отличных от нуля.  Найдите их сумму,
# произведение, разность, частное.

def test_1(a, b):
    if str(a).isdigit() and str(b).isdigit():
        return a + b, a * b, a - b, a / b
    return "Error"

print(test_1(1, 4))


# 2.  Поменяйте местами значения двух переменных.

def test_2(a, b):
    a, b = b, a
    return a, b

print(test_2(True, False))


# 3.  Дано трехзначное число.  Найдите произведение их цифр.

def test_3(a):
    b = 1
    if 99 < a < 1000:
        for num in str(a):
            b *= int(num)
        return b
    return "Error"

print(test_3(222))


# 4.  Дано пятизначное число.  Найдите разность двух чисел.  Первое
# число равно сумме цифр исходного числа, стоящих на четных местах.
# Второе число равно сумме цифр, стоящих на нечетных местах.

def test_4(a):
    if 9999 < a < 100000:
        return (int(list(str(a))[1]) + int(list(str(a))[3]) -
                int(list(str(a))[0]) - int(list(str(a))[2]) -
                int(list(str(a))[4]))
    return "Error"

print(test_4(12345))


# 5.
