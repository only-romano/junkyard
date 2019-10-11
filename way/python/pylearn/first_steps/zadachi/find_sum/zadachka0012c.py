#! Дан текст. Найти слова, состоящие из цифр, и сумму чисел, которые
# образуют эти слова (не используя регулярных выражений).


def find_sum(string):
    string = string + ' '
    new_string, words, word_library, numbers_lib, sum_words = '', [], {}, {}, 0
    for symbol in string:      # Разделяем текст на слова.
        if symbol == ' ' and new_string != '':
            words.append(new_string)
            new_string = ''
        else:
            new_string += symbol
    for word in words:        # Найдём слова с числами.
        word_number = ''
        for symbol in word:
            try:
                number = int(symbol)
                word_number += symbol
            except Exception:
                if word_number != '':
                    key = word + ' ' + symbol
                    word_library[key] = int(word_number)
                    word_number = ''
                else:
                    pass
        for key in word_library:
            if word_library[key] != '':
                numbers_lib[key] = int(word_library[key])
    for word in numbers_lib:    # Найдём сумму чисел.
        sum_words += int(numbers_lib[word])
    return word_library, numbers_lib, sum_words

def test_find_sum(arg1, value):
    print(f'Аргумент 1: {arg1}, '
          f'ожидание: {value} |-> '
          f'результат: {find_sum(arg1)},')


# Тесты
test_find_sum('tty 53saa or exept 2nite', ({'53saa': 53, '2nite': 2}, 55))
test_find_sum('Дан текст. Найти слова, состоящие из цифр', ({}, 0))
test_find_sum('пусть ты и21з фу1нкц1ии1 return 3, 4', ({'и21з': 21, 'фу1нкц1ии1': 111, '3,': 3, '4': 4}, 139))
# test_arithmetic("b", ValueError("Value Error"))
