#! Простые задачки.


# Задачи 1-2.  1) Вывести на экран числа 10, 20, 30, ..., 150.
# 2) Вывести на экран текст "Silence is golden".


def z21_1_2():
    return ' '.join(str(i) for i in range(10, 151, 10))

print(z21_1_2())


# Задача 2.  Вывести на экран n строк, каждая из которых состоит из m
# нулей.


def z21_3(m, n):
    return n * ("0" * m + '\n')


print(z21_3(4, 6))


# Задача 3.  Найдите сумму 1+3+5+7+...+37.


def z21_4(n):
    return sum(list(range(1, n+1, 2)))


print(z21_4(37))


# Задача 4.  Найдите произведение 1⋅2⋅3⋅…⋅n.


def z21_5(n):
    for m in range(n-1, 1, -1):
        n *= m
    return n


print(z21_5(123))
print(z21_5(5))


# Задача 5.  Найдите сумму 1:2+2:3+3:4+…+100:101.


def z21_6(n):
    for m in range(1, n+1):
        n += m / (m+1) - 1
    return round(n, 2)


print(z21_6(5))
print(z21_6(100))


# Задача 6.  Выведите на экран n строк, каждая из которых состоит из
# такого количества нулей, каков номер строки.


def z21_7(n):
    k = ''
    for m in range(1, n+1):
        k += '0' * m + '\n'
    return k


print(z21_7(5))



# Задача 4.  Вывести на экран текущее название дня недели, название
# месяца и свое имя.  Каждое слово должно быть в отдельной строке.

import datetime
name = 'Kato'


def z21_8():
    today = str(datetime.datetime.today()).replace('-', ' ').split()
    month = ['Jan','Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul',
             'Aug', "Sep", "Oct", 'Nov', 'Dec'][int(today[1])-1]
    today2 = datetime.date(int(today[0]), int(today[1]),
                           int(today[2])).weekday()
    weekday = ['Mon','Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'][today2]
    return weekday + '\n' + month + '\n' + name


print(z21_8())
