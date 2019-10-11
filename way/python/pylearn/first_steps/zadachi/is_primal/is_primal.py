#!Задача.Напиши функцию is_primal, которая принимает один аргумент - целое число,
#и возвращает True если это число простое, и False если оно составное.
print("Простые и составные числа.")
number = int(input("Введите число: "))
def is_primal(number):
	y=1
	for i in range(2, number):
		if number % i == 0:
			y+=1
		if y>1:
			break
	x = y==1
	return x
print(is_primal(number))