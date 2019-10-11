#! Задача 9. Арифметик.

# Написать функцию arithmetic, принимающую 3 аргумента: первые 2 -
# числа, третий - операция, которая должна быть произведена над ними.
# Если третий аргумент +, сложить их; если —, то вычесть;
# * — умножить; / — разделить (первое на второе). В остальных случаях
# вернуть строку "Неизвестная операция".

def arithmetic(a, b, c):
    if (isinstance(a, int) == False or
        isinstance(b, int) == False):
        raise ValueError("Value Error")
    if c == "+":
        return a + b
    elif c == "-":
        return a - b
    elif c == "*":
        return a * b
    elif c == "/":
        return a / b
    else:
        return "Неизвестная операция"


def test_arithmetic(arg1, arg2, arg3, value):
    print(f'Аргумент 1: {arg1}, '
          f'Аргумент 2: {arg2}, '
          f'Аргумент 2: {arg3}, '
          f'ожидание: {value} |-> '
          f'результат: {arithmetic(arg1, arg2, arg3)},')


# Тесты
test_arithmetic(2, 4, "+", 6)
test_arithmetic(4, 2, "-", 2)
test_arithmetic(2, 4, "*", 8)
test_arithmetic(12, 4, "/", 3.0)
test_arithmetic(2, 4, "=", "Неизвестная операция")
# test_arithmetic("b", 4, "*", ValueError("Value Error"))
