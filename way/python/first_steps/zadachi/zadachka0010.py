#! Задача 10. Арифметик.

# Написать функцию square, принимающую 1 аргумент — сторону квадрата,
# и возвращающую 3 значения (с помощью кортежа): периметр квадрата,
# площадь квадрата и диагональ квадрата.

def square(a):
    if isinstance(a, int) == False:
        raise ValueError("Value Error")
    return (4 * a, a * a, round((2 * a * a) ** 0.5, 2))


def test_square(arg1, value):
    print(f'Аргумент 1: {arg1}, '
          f'ожидание: {value} |-> '
          f'результат: {square(arg1)},')


# Тесты
test_square(2, (8, 4, 2.83))
test_square(3, (12, 9, 4.24))
# test_arithmetic("b", ValueError("Value Error"))