#! Занятие по книге Python Crash Course, chapter 8, "Functions".
# Занятие четвёртое.  Хранение функций в модулях, стилизация функций.

# Модуль с программой pizza.py.
import pizza as p

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# Для импорта отдельных функций для модуля:
# from module_name import function_0, function_1, function_2

from pizza import make_pizza as mp
# from pizza import * = импорт всех функций из модуля.

mp(14, 'fish', 'chicken')

# КАЖЕТСЯ, КНИГА ВПЕРВЫЕ ОПЕРЕДИТ МЕТАНИТ.  СЛЕДУЮЩАЯ ГЛАВА, ЧТО Я БУДУ
# ИЗУЧАТЬ ВО ВТОРНИК, ЗАТРАГИВАЕТ ООП, А ИМЕННО КЛАССЫ.
