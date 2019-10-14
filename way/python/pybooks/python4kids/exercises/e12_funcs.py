import sys

print(sys.stdin.readline())

def moon_weight():
	try:
		print("Ваш вес: ")
		weight = int(sys.stdin.readline())
	except Exception:
		weight = 70
		print("Установлено значение по умолчанию - 70")

	try:
		print("Коэффициент веса на планете: ")
		coef = float(sys.stdin.readline())
	except Exception:
		coef = 0.165
		print("Установлено значение по умолчанию - 0.165")

	try:
		print("Сколько лет считать? ")
		years = int(sys.stdin.readline())
	except Exception:
		years = 15
		print("Установлено значение по умолчанию - 15")

	for i in range(years):
		print("Ваш лунный вес в %s году - %s" % (2020 + i, weight * coef))
		weight += 1

if __name__ == "__main__":
	moon_weight()
