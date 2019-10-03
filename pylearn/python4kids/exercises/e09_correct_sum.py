from random import randint

money = randint(0, 10000)

if money >= 100 and money <= 500 or money >= 1000 and money <= 5000:
	print("Correct sum")
else:
	print("Not so fast!")
