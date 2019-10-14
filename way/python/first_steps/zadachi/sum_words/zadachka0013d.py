
def one_word(word):
    for letter in word:
        if ord(letter) not in range(48, 58):
            return 0
    return int(word)


def sum_words(string):
    return sum(map(one_word, string.split(' ')))


def test_sum_words(arg1, value):
    print(f'Аргумент 1: {arg1}, '
          f'ожидание: {value} |-> '
          f'результат: {sum_words(arg1)},')


# Тесты
test_sum_words('tty 53 saa or exept 2 2nite', 55)
test_sum_words('12 gg 45g 27', 39)
test_sum_words('пусть ты и 21 з фу1нкц1ии1 return 3 , 4', 28)
# test_arithmetic("b", ValueError("Value Error"))
