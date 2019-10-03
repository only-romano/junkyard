#! Работа с материалами Metanit, глава 6, часть 1.  Модуль random.

# Модуль random управляет генерацией случайных чисел.  Основные функции:
# - random(): генерирует случайное число от 0.0 до 1.0.
# - randint(): возвращает случайное число из определенного диапазона.
# - randrange(): возвращает случайное число из определенного набора
#   чисел.
# - shuffle(): перемешивает список.
# - choice(): возвращает случайный элемент списка.
import random

# Функция random() возвращает случайное число с плавающей точкой в
# промежутке от 0.0 до 1.0.  Если же нам необходимо число из большего
# диапазона, скажем от 0 до 100, то мы можем соответственно умножить
# результат функции random на 100.
print(random.random())            # Случайное значение от 0.0 до 1.0.
print(random.random() * 100)      # Случайное значение от 0.0 до 100.0.

# Функция randint(min, max) возвращает случайное целое число в
# промежутке между двумя значениями min и max.
print(random.randint(20, 35))     # Случайное значение от 20 до 35.

# Функция randrange() возвращает случайное целое число из определенного
# набора чисел.  Она имеет три формы:
# - randrange(stop): в качестве набора чисел, из которых происходит
#   извлечение случайного значения, будет использоваться диапазон от 0
#   до числа stop.
# - randrange(start, stop): набор чисел представляет диапазон от числа
#   start до числа stop.
# - randrange(start, stop, stop): набор чисел представляет диапазон от
#   числа start до числа stop, при этом каждое число в диапазоне
#   отличается от предыдущего на шаг step.
print(random.randrange(10))         # Значения от 0 до 10.
print(random.randrange(2, 10))      # Значения от 2 до 10.
print(random.randrange(2, 10, 2))   # Значения: 2, 4, 6, 8, 10.

# Для работы со списками в модуле random определены две функции: функция
# shuffle() перемешивает список случайным образом, а функция choice()
# возвращает один случайный элемент из списка:

numbers = [1, 2, 3, 4, 5, 6, 7]
print(numbers)
random.shuffle(numbers)
print(numbers, "\n", random.choice(numbers))
