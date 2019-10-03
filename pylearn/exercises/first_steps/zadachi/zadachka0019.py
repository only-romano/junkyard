#! Простые задачки.


# Задача 1.  Дан номер дня недели.  Выведите название дня недели.


def day_of_week(day):
    return ["Mon", "Tue", "Wed", "The", "Fri", "Sat", "Sun"][day - 1]


print(day_of_week(5))


# Задача 2.  Дан номер месяца. Выведите пору года.


def lame_period(month):
    if month in [1, 2, 12]: return "winter"
    elif month in [3, 4, 5]: return "spring"
    elif month in [6, 7, 8]: return "summer"
    else: return "autumn"


print(lame_period(6))


# Задача 3.  Даны два числа.  Если оба больше 8, то вывести их
# произведение, если хотя бы одно меньше 5, то вывести их сумму.


def lucky_numbers(num1, num2):
    if num1 > 8 and num2 > 8: return num1 * num2
    if num1 < 5 or num2 < 5: return num1 + num2


print(lucky_numbers(12, 11))
print(lucky_numbers(4, 11))
print(lucky_numbers(5, 6))


# Задача 4.  Даны три числа.  Если все числа положительны, выведите их
# сумму, если ровно два из них отрицательны, то выведите их произведение,
# если ровно два из них равны нулю, то выведите ноль.


def variable_numbers(num1, num2, num3):
    nums = sorted([num1, num2, num3])
    if nums.count(0) == 2: return 0
    elif nums[0] > 0: return sum(nums)
    elif nums[2] > 0 and nums[1] < 0: return num1 * num2 * num3


print(variable_numbers(0, 50, 0))
print(variable_numbers(10, 12, 15))
print(variable_numbers(-10, 12, -15))
print(variable_numbers(-10, 12, 15))
