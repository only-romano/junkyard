import time

duration = input("How many seconds until start?\n")

try:
	duration = int(duration)
except Exception:
	duration = 5

for i in range(duration, 0, -1):
	star = ' *' * i
	print(str(i) + star)
	time.sleep(1)

print("\nHurray!")
