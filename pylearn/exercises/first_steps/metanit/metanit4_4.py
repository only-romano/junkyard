#! Работа с материалами Metanit, глава 4, часть 4. Бинарные файлы.

# Для работы с бинарными файлами в python необходим встроенный модуль
# "pickle".  Этот модуль предоставляет два метода:
# 1. dump(obj, file): записывает объект obj в бинарный файл file.
# 2. load(file): считывает данные из бинарного файла в объект.
#
# При открытии бинарного файла следует применить в дополнение к обычным
# режимам - режим " b ".
import pickle

filename = "../d020/user.dat"

# НОРМАЛЬНАЯ ЛИ ПРАКТИКА ПРИСВАИВАТЬ НЕСКОЛЬКО ПЕРЕМЕННЫХ ?
name, age = "Tom", 19

with open(filename, "wb") as file:
    pickle.dump(name, file)
    pickle.dump(age, file)

with open(filename, "rb") as file:
    name = pickle.load(file)
    age = pickle.load(file)
    print("Имя:", name, "\tВозраст:", age)

# В примерах выше запись и чтение производятся последовательно, по
# одному объекту, соответственно.

users = [
    ["Tom", 28, True],
    ["Alice", 23, False],
    ["Bob", 34, False]
]

with open("../d020/users.dat", "wb") as file:
    pickle.dump(users, file)

with open("../d020/users.dat", "rb") as file:
    users_from_file = pickle.load(file)
    for user in users_from_file:
        print("Имя:", user[0], "\tВозраст:", user[1], "\tЖенат(замужем):",
              user[2])
