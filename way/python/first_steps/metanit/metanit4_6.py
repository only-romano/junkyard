#! Работа с материалами Metanit, глава 4, часть 6.  Модуль OS и работа с
# файловой системой.

import os

# Основные функции модуля os (работа с каталогами и файлами):
# mkdir(): создает новую папку.
# rmdir(): удаляет папку.
# rename(): переименовывает файл.
# remove(): удаляет файл.
# Модуль способен работать с абсолюными и отноасительными адресами.

# Создание папок:
os.mkdir('../1. days/test')

# Удаление папок:
os.rmdir('../1. days/test')

# Переименование файла:
os.rename('../1. days/d024/target.txt', 'C://prs/me/1. days/d024/renamed.txt')

# Удаление файла:
os.remove('../1. days/d024/test2.txt')

# Проверка существования файла:

if os.path.exists('../1. days/d024/renamed.txt'):
    print('Файл существует')
else:
    print('Файл не существует')
