#! Работа с материалами Metanit, глава 6, часть 4.  Модуль decimal.
from decimal import Decimal, ROUND_HALF_EVEN

print(0.1 + 0.1 + 0.1)
print(Decimal("0.1") + Decimal("0.1") + Decimal("0.1"))

print(Decimal("0.1") + 2)   # Можно использовать в операциях с int.
# print(Decimal("0.1") + 0.1)   # Нельзя с float.  Ошибка.

print(Decimal("0.10") * 3)  # Символы в дробной части определяют
# вывод, то есть print выдаст 0.30, а не 0.3 .  То есть, если указать
# Decimal("0.100" * 3), то вывод будет уже 0.300, а не 0.30 .

# Объекты Decimal имеют метод quantize(), который позволяет округлять
# числа.  В этот метод в качестве первого аргумента передается также
# объект Decimal, который указывает формат округления числа:

number = Decimal("0.444")
print(number.quantize(Decimal("1.00")))     # 0.44

number = Decimal("0555678")
print(number.quantize(Decimal("1.00")))     # 0.56

number = Decimal("0.999")
print(number.quantize(Decimal("1.00")))     # 1.00

# По умолчанию округление описывается константой ROUND_HALF_EVEN, при
# котором число округляется в большую сторону, если оно нечетное, а
# предыдущее перед ним больше 4.  Например:

print(Decimal("10.025").quantize(Decimal("1.00"), ROUND_HALF_EVEN))
print(Decimal("10.035").quantize(Decimal("1.00"), ROUND_HALF_EVEN))

# Строка "1.00" означает, что округление будет идти до двух чисел в
# дробной части.  Но в первом случае "10.025" - вторым знаком идет 2
# - четное число, поэтому, несмотря на то, что следующее число 5, двойка
# не округляется до тройки.  Во втором случае "10.035" - вторым знаком
# идет 3 - нечетное число, поэтому оно округляется до 4.

# - ROUND_HALF_UP: округляет число в сторону повышения, если после него
#   идет число 5 или выше.
# - ROUND_HALF_DOWN: округляет число в сторону повышения, если после
#   него идет число больше 5:
from decimal import ROUND_HALF_DOWN

print(Decimal("10.026").quantize(Decimal("1.00"), ROUND_HALF_DOWN))
print(Decimal("10.025").quantize(Decimal("1.00"), ROUND_HALF_DOWN))

# - ROUND_05UP: округляет только 0 до единицы, если после него идет 5.
from decimal import ROUND_05UP

print(Decimal("10.005").quantize(Decimal("1.00"), ROUND_05UP))
print(Decimal("10.025").quantize(Decimal("1.00"), ROUND_05UP))

# - ROUND_CEILING: округляет число в большую сторону вне зависимости
#   от того, какое число идет после него.
from decimal import ROUND_CEILING

print(Decimal("10.021").quantize(Decimal("1.00"), ROUND_CEILING))
print(Decimal("10.025").quantize(Decimal("1.00"), ROUND_CEILING))

# - ROUND_FLOOR: не округляет число вне зависимости от того, какое
#   число идет после него.
from decimal import ROUND_FLOOR

print(Decimal("10.021").quantize(Decimal("1.00"), ROUND_FLOOR))
print(Decimal("10.025").quantize(Decimal("1.00"), ROUND_FLOOR))
