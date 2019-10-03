from random import randint

twinkles = randint(1, 600)

if twinkles < 100:
	print("Слишком мало бисквитов...")
elif twinkles > 500:
	print("Слишком много бисквитов!")
else:
	print("Нормально всё с бисквитами.")
