#!Задача.Напиши функцию is_primal, которая принимает один аргумент - целое число,
#и возвращает True если это число простое, и False если оно составное.
print("Простые и составные числа.")
number = int(input("Введите число: "))
def is_primal(number):
	y=1
	for i in range(2, number):
		x = number % i
		if x == 0:
			y+=1
	y=int(y)
	z = y==1
	return z
print(is_primal(number))