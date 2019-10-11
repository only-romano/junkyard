#! Работа с материалами Metanit, глава 3, часть 1. Список.

numbers = [1, 2, 3, 4, 5]
# numbers1 = []
numbers2 = list(numbers)    # Конструктор list может принимать список.
print(numbers[0], numbers[2], numbers[-3])

numbers2[0] = 125
print(numbers2[0])

numbers1 = [5] * 6      # Новое для меня, заполнение списков.
print(numbers1)

numbers = list(range(10))
print(numbers)
numbers = list(range(2, 10))
print(numbers)
numbers = list(range(10, 2, -2))
print(numbers)

objects = [1, 2.6, "Hello", True]   # Вот это реально круто, буду знать.
print(objects)

# Перебор элементов

companies = ["Microsoft", "Google", "Oracle", "Apple"]
for item in companies:
    print(item)

i = 0
while i < len(companies):
    print(companies[i])
    i += 1

# Сравнение списков

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers2 = list(range(1, 10))
if numbers == numbers2:
    print("Both lists are equal")
else:
    print("Lists aren't equal")

# Методы и функции по работе со списками.

# .appent(item) - добавляет item в конец списка.
# .insert(index, item) - добавляет item по индексу index.
# .remove(item) - удаляет item, только первое, если нет - ValueError.
# .clear() - удаление всех элементов списка.
# .index(item) - возвращает индекс item, если нет - ValueError.
# .pop([index]) - удаляет и возвращает по индексу index, если индекс не
#      задан, то удаляет последний элемент.  P.S. - подумать с заданием.
# .count(item) - возвращает количество вхождений item в список.
# .sort([key]) - сортирует элементы по параметру key, по умолчанию идёт
#      сортировка по алфавиту.
# .reverse() - расставляет элементы списка в обратном порядке.
#
# len(list) - возаращает длину списка.
# sorted(list, [key]) - возвращает отсортированный список.
# min(list) - возвращает наименьший элемент списка.
# max(list) - возвращает наибольший элемент списка.

users = ["Tom", "Bob"]
users.append("Alice")           # ["Tom", "Bob", "Alice"]
users.insert(1, "Bill")      # ["Tom", "Bill", "Bob", "Alice"]

i = users.index("Tom")          # получение индекса
removed_item = users.pop(i)     # ["Bill", "Bob", "Alice"]

last_user = users[-1]
users.remove(last_user)         # ["Bill", "Bob"]

print(users)

users.clear()                   # удаление всех элементов


# Проверка наличия элемента.

# Если элемент не найден, то методы .remove и .index генерируют
# исключение. Для избежания этого использовать конструкцию "if . in .":

companies = ["Microsoft", "Google", "Oracle", "Apple"]
item = "Oracle"
if item in companies:   # Проверка на наличие и зависимое исполнение.
    companies.remove(item)

print(companies)


# Подсчёт вхождений.

users = ["Tom", "Bob", "Alice", "Tom", "Bill", "Tom"]

users_count = users.count("Tom")    # Присвоено колличество элементов.
print(users_count)


# Сортировка.

users = ["Tom", "Bob", "Alice", "Sam", "Bill"]

users.sort()    # Произведётся сортировка по возрастанию.
print(users)    # ["Alice", "Bill", "Bob", "Sam", "Tom"]

users.reverse()
print(users)    # ["Tom", "Sam", "Bob", "Bill", "Alice"]

users = ["Tom", "bob", "alice", "Sam", "Bill"]

users.sort()
print(users)                # ["Bill", "Sam", "Tom", "alice", "bob"]

users.sort(key=str.lower)   # Функция в качестве параметра.  Изучить.
print(users)                # ["alice", "Bill", "bob", "Sam", "Tom"]

users = ["Tom", "bob", "alice", "Sam", "Bill"]

sorted_users = sorted(users)    # Помещает в новый список результат.
print(sorted_users)         # ["Bill", "Sam", "Tom", "alice", "bob"]

sorted_users = sorted(users, key=str.lower)
print(sorted_users)         # ["alice", "Bill", "bob", "Sam", "Tom"]


# Минимальное и максимальное значения.

numbers = [9, 21, 12, 1, 3, 15, 18]
print(min(numbers))     # 1
print(max(numbers))     # 21


# Копирование списков.

# Поверхностное копирование (shallow copy):
users1 = ["Tom", "Bob", "Alice"]    # Списки представляют "mutable" -
users2 = users1         # изменяемый тип.  Если обе переменных будут
users2.append("Sam")    # указывать на один и тот же список, то при
                        # изменении одного, изменится и другая.  Оба
print(users1, users2)   # списка эквивалентны.

# Глубокое копирование (deep copy) методом deepcopy() из модуля copy:
import copy

users1 = ["Tom", "Bob", "Alice"]
users2 = copy.deepcopy(users1)
users2.append("Sam")

print(users1, users2)   # Списки имеют разный состав.


# Копирование части списка.

users = ["Tom", "Bob", "Alice", "Sam", "Tim", "Bill"]

slice_users1 = users[:3]        # С 0 по 3, не включая 3.
print(slice_users1)             # ["Tom", "Bob", "Alice"]

slice_users2 = users[1:3]       # С 1 по 3, не включая 3.
print(slice_users2)             # ["Bob", "Alice"]

slice_users3 = users[1:6:3]     # C 1 по 6 с шагом 2, не включая 6.
print(slice_users3)             # ["Bob", "Sam", "Bill"]


# Соединение списков.

users1 = ["Tom", "Bob", "Alice"]
users2 = ["Tom", "Sam", "Tim", "Bill"]
users3 = users1 + users2
print(users3)   # ["Tom", "Bob", "Alice", "Tom", "Sam", "Tim", "Bill"]


# Списки списков.

users = [               # Запись списка списков.
    ["Tom", 29],
    ["Alice", 33],
    {"Bob", 27}
]

# Вызов нужных элементов списка:
print(users[0])         # ["Tom", 29]
print(users[0][0])      # Tom
print(users[0][1])      # 29

user = list()           # Создание вложенного списка.
user.append("Bill")
user.append(41)

users.append(user)      # Добавление вложенного списка.

print(users[-1])        # ["Bill", 41]

# Добавление элемента во вложенный список:
users[-1].append("+79876543210")

print(users[-1])        # ["Bill", 41, +79876543210]

# Удаление последнего элемента из вложенного списка:
users[-1].pop()
print(users[-1])        # ["Bill", 41]

users.pop(-1)           # Удаление всего последнего вложенного списка.

# Изменение списков внутри списка:
users[0] = ["Sam", 18]
print(users)            # [["Sam", 18], ["Alice", 33], ["Bob", 27]]

# Перебор вложенных списков:

users = [
    ["Tom", 29],
    ["Alice", 33],
    {"Bob", 27}
]

for user in users:
    for item in user:
        print(item, end=" | ")
