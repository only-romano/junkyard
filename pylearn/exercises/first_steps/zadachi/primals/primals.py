'''
Такой способ разработки, когда сперва пишут тесты, а потом реализацию,
называют TDD (Test Driven Development). Очень распространенная практика.
'''


def get_primals(x):
    pass


def test_equals(arg, value):
    print(f'Аргумент: {arg}, '
          f'результат: {get_primals(arg)}, '
          f'ожидание: {value}')


# Тесты
test_equals(0, [])
test_equals(1, [])
test_equals(2, [1])
test_equals(3, [1, 2])
test_equals(9, [1, 2, 3, 5, 7])
test_equals(13, [1, 2, 3, 5, 7, 11])


print('_'*64 + '\n')


# Тесты на отрицательные
#test_equals(-1, [])
#test_equals(-2, [-1])
#test_equals(-3, [-1, -2])
#test_equals(-9, [-1, -2, -3, -5, -7])
#test_equals(-13, [-1, -2, -3, -5, -7, -11])
