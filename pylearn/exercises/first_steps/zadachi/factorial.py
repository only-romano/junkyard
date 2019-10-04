#! Программа по вычислению факториала.
number = int(input("Введите число: "))
i = 1
factorial = 1
while i <= number:
	factorial *= i
	i += 1
print("Факториал числа", number, "равен", factorial)

#! версия 2.
number = int(input("Введите число: "))
factorial = 1
for i in range(1, number+1):
	factorial *= i
print("Факториал числа", number, "равен", factorial)