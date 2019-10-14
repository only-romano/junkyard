def is_primal(n):
	return False if (n % i == 0 for i in range(2, n)) else True

print(is_primal(4), is_primal(11), is_primal(121),is_primal(123))
