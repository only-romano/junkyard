#! Дан текст. Найти слова, состоящие из цифр, и сумму чисел, которые
# образуют эти слова (не используя регулярных выражений).


def find_sum(string):
    big_number1, big_number2, numbers, sum = "", "", [], 0
    for symbol in string:
        if symbol == ' ' or symbol == '.':
            big_number1 += symbol
            pass
        else:
            try:
                number = int(symbol)
                big_number1 += symbol
            except Exception:
                pass
    big_number1 += '.'
    for symbol in big_number1:
        if symbol == ' ' or symbol == '.':
            try:
                big_number3 = int(big_number2)
                numbers.append(big_number3)
                big_number2 = ""
                pass
            except:
                pass
        else:
            big_number2 += symbol
    for number in numbers:
        sum += number
    return sum

def test_find_sum(arg1, value):
    print(f'Аргумент 1: {arg1}, '
          f'ожидание: {value} |-> '
          f'результат: {find_sum(arg1)},')


# Тесты
test_find_sum('tty 53saa or exept 2nite', 55)
test_find_sum('Дан текст. Найти слова, состоящие из цифр', 0)
test_find_sum('пусть ты и21з фу1нкц1ии1 return 3, 4', 139)
# test_arithmetic("b", ValueError("Value Error"))
