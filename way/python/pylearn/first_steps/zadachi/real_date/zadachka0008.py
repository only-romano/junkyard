#! Задача 8. Дата.

# Написать функцию date, принимающую 3 аргумента — день, месяц
# и год. Вернуть True, если такая дата есть в нашем календаре, и False
# иначе. Одной строчкой напиши:
# is_date_correct(date):
#    return ТУТТЫПИШИ

def date(day, month, year):
    if (isinstance(year, int) == False or
        month not in range(1, 13)):
        return False
    elif (month in [1, 3, 5, 7, 8, 10, 12] and
        day not in range(1, 32)):
        return False
    elif (month in [4, 6, 9, 11] and
        day not in range(1, 31)):
        return False
    elif (month == 2 and year % 4 == 0 and
        day not in range(1, 30)):
        return False
    elif (month == 2 and year % 4 != 0 and
        day not in range(1, 29)):
        return False
    return True


def test_date(arg1, arg2, arg3, value):
    print(f'Аргумент 1: {arg1}, '
          f'Аргумент 2: {arg2}, '
          f'Аргумент 2: {arg3}, '
          f'ожидание: {value} |-> '
          f'результат: {date(arg1, arg2, arg3)},')


# Тесты
test_date(8, 12, 2017, True)
test_date(33, 10, 604, False)
test_date(2, 103, 36683, False)
test_date(17, 12, 538921, True)
test_date(29, 2, 2017, False)
# test_date(22, "Июнь", "vfvf", "Введено неверное значение")
