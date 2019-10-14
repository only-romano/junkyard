#! Задача 9. Арифметик.

def arithmetic(a, b, c):
    if c in ["+", "-", "*","/"]:
        return eval("a + c + b")
    else:
        return "Неизвестная операция"


def test_arithmetic(arg1, arg2, arg3, value):
    print(f'Аргумент 1: {arg1}, '
          f'Аргумент 2: {arg2}, '
          f'Аргумент 2: {arg3}, '
          f'ожидание: {value} |-> '
          f'результат: {arithmetic(arg1, arg2, arg3)},')


# Тесты
test_arithmetic('2', '4', '+', 6)
test_arithmetic('4', '2', '-', 2)
test_arithmetic('2', '4', '*', 8)
test_arithmetic('12', '4', '/', 3.0)
test_arithmetic('2', '4', '=', "Неизвестная операция")
# test_arithmetic("b", 4, "*", ValueError("Value Error"))