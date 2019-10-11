#! Короч вот такие правила: поп 35 олп4л 5ол 098 === 35.  Бери только
# валидные целые положительные числа.  Используй split.  Не гнушайся
# писать вспомогательные функции.  Старайся не использовать Exceptions,
# это довольно затратная операция.  Обойдись только арифметикой и
# логикой.  Pазделяй логически обособленные куски кода по функциям.

# '12 gg 45g'.split(' ') »> ['12', 'gg', '45g']

def word(b):
    for letter in b:
        if ord(letter) not in range(48, 58):
            return 0
        else:
            pass
    return int(b)

def words(a):
    sum = 0
    while a:
        word = a.pop()
        sum += int(word(word))
    return sum

def sum_words(string):
    string = string.split(' ')
    summa = words(string)
    return summa

def test_sum_words(arg1, value):
    print(f'Аргумент 1: {arg1}, '
          f'ожидание: {value} |-> '
          f'результат: {sum_words(arg1)},')

# Тесты
test_sum_words('tty 53 saa or exept 2nite', 53)
test_sum_words('Дан текст. Найти слова, состоящие из цифр', 0)
test_sum_words('пусть ты и 21 з фу1нкц1ии1 return 3 , 4', 28)
# test_arithmetic("b", ValueError("Value Error"))
