print("Простые и составные числа.")
number = int(input("Введите число: "))
y=1
for i in range(2, number):
	x = number % i
	if x == 0:
		y+=1
	y=int(y)
def is_primal(number):
	z = y==1
	return z
print(is_primal(number))