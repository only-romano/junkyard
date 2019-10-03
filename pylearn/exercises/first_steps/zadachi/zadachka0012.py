#! Дан текст. Найти слова, состоящие из цифр, и сумму чисел, которые
# образуют эти слова (не используя регулярных выражений).

def find_numbers(string):
    sum = 0
    for symbol in string:
        try:
            number = int(symbol)
            sum += number
        except Exception:
            pass
    return sum

def test_find_numbers(arg1, value):
    print(f'Аргумент 1: {arg1}, '
          f'ожидание: {value} |-> '
          f'результат: {find_numbers(arg1)},')


# Тесты
test_find_numbers('tty 53saa or exept 2nite', 10)
test_find_numbers('Дан текст. Найти слова, состоящие из цифр', 0)
test_find_numbers('пусть ты из функции return 3, 4', 7)
# test_arithmetic("b", ValueError("Value Error"))
