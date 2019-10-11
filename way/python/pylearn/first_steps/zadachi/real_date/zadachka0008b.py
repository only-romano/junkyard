#! Задача 8. Дата.

# Написать функцию date, принимающую 3 аргумента — день, месяц
# и год. Вернуть True, если такая дата есть в нашем календаре, и False
# иначе. Одной строчкой напиши:
# is_date_correct(date):
#    return ТУТТЫПИШИ

def is_date_correct(day, month, year):
    return (isinstance(year, int) and
        ((month in [1, 3, 5, 7, 8, 10, 12] and
        day in range(1, 32)) or
         (month in [4, 6, 9, 11] and
        day in range(1, 31)) or
         (month == 2 and year % 4 == 0 and
        day in range(1, 30)) or
         (month == 2 and year % 4 != 0 and
        day in range(1, 29))))


def test_is_date_correct(arg1, arg2, arg3, value):
    print(f'Аргумент 1: {arg1}, '
          f'Аргумент 2: {arg2}, '
          f'Аргумент 2: {arg3}, '
          f'ожидание: {value} |-> '
          f'результат: {is_date_correct(arg1, arg2, arg3)},')


# Тесты
test_is_date_correct(8, 12, 2017, True)
test_is_date_correct(33, 10, 604, False)
test_is_date_correct(2, 103, 36683, False)
test_is_date_correct(17, 12, 538921, True)
test_is_date_correct(29, 2, 2017, False)
# test_date(22, "Июнь", "vfvf", "Введено неверное значение")