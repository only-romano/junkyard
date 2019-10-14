#! Работа с материалами Metanit, глава 4, часть 5.  Модуль shelve.

# shelve - модуль для работы с бинарными файлами.  Он сохраняет объекты
# в файл с определённым ключом, затем по этому ключу можно извлечь ранее
# сохнанённый объект из файла.  Процесс работы с данными через модуль
# shelve напоминает работу со словарями, которые используют ключи для
# сохранения и извлечения объектов.

import shelve

# Открытие и закрнытие файлов:
filename = "../1. days/d023/shelve.txt"
d = shelve.open(filename, flag="n")
d["London"] = "Great Britain"
d2 = d.get("London")
d.close()

# Флаги.
# c: файл открывается для чтения и записи (значение по умолчанию).  Если
# файл не существует, то он создается.
# r: файл открывается только для чтения.
# w: файл открывается для записи.
# n: файл открывается для записи.  Если файл не существует, то он
# создается.  Если он существует, то он перезаписывается.

print(d2)


# Запись в файл и чтение из файла (также работает конструкция with):

# Запись предполагает установку значения для определённого ключа.
with shelve.open(filename) as states:
    states["Paris"] = "France"
    states["Berlin"] = "Germany"
    states["Madrid"] = "Spain"

# Чтение эквивалентно получению значения по ключу.  В качестве ключей
# используются строковые значения.  При чтении, если запрашиваемый
# ключ отсутствует, то генерируется исключение.
with shelve.open(filename) as states:
    for state in states:
        print(states[state], "-", state)
    if "London" in states:      # Избегаем исключения.
        print(states["London"])
    state = states.get("Madrid")
    print(state)

# Методы.
with shelve.open(filename) as states:
    for city in states.keys():
        print(city, end=" ")
    print()     # ДЛЯ ЧЕГО МОЖЕТ СТАВИТЬСЯ ПУСТОЙ ПРИНТ ?
    for country in states.values():
        print(country, end=" ")
    for state in states.items():
        print(state)

# Для изменения данных достаточно присвоить по ключу новое значение, а
# для добавления данных - определить новый ключ.
with shelve.open(filename) as states:
    states["Brussels"] = "Belgium"
    states["London"] = "United Kingdom"
    for key in states:
        print(key, " - ", states[key])

# Удаление данных.
with shelve.open(filename) as states:
    state = states.pop("London", "NotFound")    # 2 значение страхует.
    print(state, "\n")
    for key in states:
        print(key, " - ", states[key])

with shelve.open(filename) as states:
    del states["Madrid"]
    for key in states:
        print(key, " - ", states[key])

with shelve.open(filename) as states:
    states.clear()
    for key in states:
        print(key, " - ", states[key])
