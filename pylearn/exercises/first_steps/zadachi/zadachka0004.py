#! Задание о проверке импорта.
#
# При первом импорте модуля, вызывается весь скрипт.  Именно при первом!
# А остальные импорты скрипт уже не вызывают.  Вот задание тебе :)
# Проверь это при первом и не важно каком.  Проверь отличия просто
# import от from тоже.

print("Начало первого импорта - фулл модуль\n")

import metanit2_9

# w1 = say_goodbye()
# w2 = metanit2_9.say_goodbye()

print("\n Конец первого импорта - фулл модуль\n\n" +
      "Начало второго импорта - одна команда\n")

from metanit2_9 import *
say_goodbye()

print("\n Конец второго импорта - одна команда\n\n" +
      "Начало третьего импорта - одна команда\n")

import metanit2_9 as cs
cs.say_poop()

print("\n Конец третьего импорта - одна команда\n\n")

# Различие import от from в том, что имена из импортируемого модуля при
# import не перейдут в глобальное пространство имён, то есть формула w1
# не будет исполнена, а w2 будет (обе закомментены).  При from же идёт
# импорт имён функций из модуля в глобальное пространство имён и функция
# say_goodbye() будет исполнена.  Третий вариант ислоьзован с заменой
# имён на более удобное.  From использовать если функция из модуля будет
# часто использована и нет совпадений имён функций, либо если нужно
# импортировать конкретную функцию, а не все.