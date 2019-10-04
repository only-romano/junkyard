#! Простые задачки.

# Задача А.  Дано положительнео целое число n, выведи на экран все числа
# от 1 до n.


def a(n):
    if n == 1:
        return str(n) + ' '
    return a(n-1) + str(n) + ' '


print(a(3))
print(a(11))


# Задача B. Функция находящая факториал числа n.


def factorial(n):
    return 1 if n == 1 else n * factorial(n-1)


print(factorial(3))
print(factorial(11))


# Задача С.  Функция, принимающая n и выводящая сумму от 1 до n.


def func(n):
    return 1 if n == 1 else n + func(n-1)


print(func(3))
print(func(11))
