#! Простые задачки.


# Задача 1.  Даны два трехзначных числа. Найдите шестизначное число,
# образованное из двух данных чисел путем дописывания второго числа к
# первому справа.


def dual_numbers(number1, number2):
    if len(str(number1)) == 3 and len(str(number2)) == 3:
        return int(str(number1) + str(number2))


print(dual_numbers(123, 456))


# Задача 2.  Даны два числа.  Выведите большее из них.


def two_numbers(number1, number2):
    if isinstance(number1, int) and isinstance(number2, int):
        numbers = [number1, number2]
        return max(numbers)


print(two_numbers(123, 456))


# Задача 3.  Даны два числа.  Если они не равны, то найти их сумму,
# иначе найти их произведение.


def sum_or_multiply(number1, number2):
    if isinstance(number1, int) and isinstance(number2, int):
        if number1 != number2:
            return number1 + number2
        else:
            return number1**2


print(sum_or_multiply(123, 456))
print(sum_or_multiply(4, 4))


# Задача 4.  Даны три числа.  Если первое число больше двух, то найти
# их сумму, иначе найти разность между вторым и третьим числами.


def three_numbers(num1, num2, num3):
    if isinstance(num1, int) and isinstance(num2, int) and\
            isinstance(num3, int):
        if num1 > (num2 + num3):
            return num1 + num2 + num3
        else:
            return num2 - num3


print(three_numbers(100, 50, 25))
print(three_numbers(100, 125, 150))
