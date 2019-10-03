#! Задача 8. Дата.

import datetime

now = datetime.datetime.date(datetime.datetime.now())

def is_date_correct2(day, month, year):
    return (year, month, day == now)


def test_is_date_correct2(arg1, arg2, arg3, value):
    print(f'Аргумент 1: {arg1}, '
          f'Аргумент 2: {arg2}, '
          f'Аргумент 2: {arg3}, '
          f'ожидание: {value} |-> '
          f'результат: {is_date_correct2(arg1, arg2, arg3)},')


# Тесты
test_is_date_correct2(0+8, 12, 2017, True)
test_is_date_correct2(33, 10, 604, False)
test_is_date_correct2(17, 12, 2016, False)
