def show(num=10, exp=10):
	message = "Number\t\t"
	if exp > 0:
		for i in range(2, exp+1):
			message += "n**" + str(i) + "\t\t"
	else:
		for i in range(0, exp-1, -1):
			message += "n**(" + str(i) + ")\t\t"
	print(message)

	if num > 0:
		for i in range(1, num+1):
			message = ""
			if exp > 0:
				for j in range(1, exp+1):
					message += str(i**j) + "\t\t"
			else:
				for j in range(0, exp-1, -1):
					message += str(i**j) + "\t\t"
			print(message)
	else:
		for i in range(0, num-1, -1):
			message = ""
			if exp > 0:
				for j in range(1, exp+1):
					message += str(i**j) + "\t\t"
			else:
				for j in range(0, exp-1, -1):
					message += str(i**j) + "\t\t"
			print(message)
