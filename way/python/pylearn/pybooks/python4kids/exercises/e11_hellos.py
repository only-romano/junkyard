for x in range(0, 20):
	print('hello %s' % x)
	if x < 9:
		break

age = 28

for x in range(age):
	if x % 2 == 0:
		print(x)

ingredients = ["колбаса", "сыр", "помидорки", "огурцы", "перчик"]

for x in range(len(ingredients)):
	print("%s. %s" % (x+1, ingredients[x]))


weight = 180

for i in range(15):
	weight *= .95
	print("Земной вес - %s ; Лунный вес - %s" % (weight, weight * 0.165))
