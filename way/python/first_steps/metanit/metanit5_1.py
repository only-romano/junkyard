#! Работа с материалами Metanit, глава 5, часть 1.  Работа со строками.

string = "hello 54 wo4rld"
c0 = string[0]      # Символ по индексу.
c6 = string[6]
c1 = string[-1]
c4 = string[-4]
# c15 = string[15]  # Выйдет ошибка Index Error.

print(c0, c6, c1, c4)


# Cтрока - неизменяемый тип, поэттому при попытке изменения символа в
# строке выйдет ошибка.  Возможно только полностью переустановить
# значение строки.
# string[1] = "R"   # Ошибка.
string = "hRllo 54 wo4rld"    # Правильно


# Получение подстроки.
# string[:end]: извлекается последовательность символов начиная с 0-го
# индекса по индекс end.
# string[start:end]: извлекается последовательность символов начиная с
# индекса start по индекс end.
# string[start:end:step]: извлекается последовательность символов
# начиная с индекса start по индекс end через шаг step.

print(string[:5] + '\n' + string[6:11] + '\n' + string[0:14:2])


# Функции ord и len.

# C помощью функции ord() можно получить числовое значение для символа в
# кодировке Unicode:
for number in range(0, 10):
    print(number, ' - ', ord(str(number)))

# Для получения длины строки можно использовать функцию len():
print(len(string))


# Поиск в строке.
a = 'hello' in string
b = '54' in string
print(a, b)

string2 = string.split()
print(string2)

# Перебор строки.

chars = []
for char in string:
    chars.append(char)

print(chars)
