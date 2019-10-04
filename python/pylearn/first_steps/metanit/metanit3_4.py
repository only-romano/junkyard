#! Работа с материалами Metanit, глава 3, часть 4. Множества {set}.

users = {"Tom", "Bob", "Alice", "Tom"}      # Пример множества.
print(users)    # {"Tom", "Bob", "Alice"}

# Множество содержит только УНИКАЛЬНЫЕ элементы, "Tom" не повторяется.

users3 = set(["Mike", "Bill", "Ted"])
users2 = set()
print(len(users3))                  # Длинна множества.


# Добавление элементов.

users2.add("Sam")
print(users2)


# Удаление элементов.

if "Tom" in users:       # При использовании метода .remove(), если
    users.remove("Tom")  # элемент отсутствует в множестве - ошибка.
print(users)             # {"Bob", "Alice"}

users3.discard("Ted")   # При использовании метода .discard() не будет
print(users3)       # сгенерировано исключение при отсутствии элемента.

users3.clear()          # Удаление всех элементов множества.
print(users3)


# Перебор множества.

for user in users:
    print(user)


# Операции с множествами.

users3 = users.copy()           # Копирование users в users3.
users = users3.union(users2)    # Объединение множеств в users.
print(users)        # {"Bob", "Alice", "Sam"}

users2 = users.intersection(users3)  # Пересечение двух множеств:
print(users2)   # в данном случае users & users3 в users2.
print(users & users3)   # Альтернативное пересечение.  & == and .

users2 = users.difference(users3)   # Разность множеств, два варианта.
print(users2)           # Если первое множество не содержит ни одного
print(users - users3)   # уникального элемента - выдаст пустое множ-во.


# Отношения между множествами.

# Является ли множество подмножеством, метод .issubset():
print(users.issubset(users3))   # False.
print(users3.issubset(users))   # True.

# Является ли множество надмножеством, метод .issuperset():
print(users.issuperset(users3))   # True.
print(users3.issuperset(users))   # False.


# Множества "Frozen Set".  Неизменяемые множества.

users = frozenset(users)
print(users)

# В функцию frozenset() передаётся набор элементов - список, кортеж,
# другое множестов.  В такое множество нельзя добавить новые элементы,
# кака и удалить из него уже имеющиеся.  Поддерживаемые операции:
#  len(s): возвращает длину множества;
#  x in s: возвращает True, если элемент x присутствует в множестве s;
#  x not in s: True, если элемент x отсутствует в множестве s;
#  s.issubset(t): возвращает True, если t содержит множество s;
#  s.issuperset(t): возвращает True, если t содержится в множестве s;
#  s.union(t): возвращает объединение множеств s и t;
#  s.intersection(t): возвращает пересечение множеств s и t;
#  s.difference(t): возвращает разность множеств s и t;
#  s.copy(): возвращает копию множества s.
