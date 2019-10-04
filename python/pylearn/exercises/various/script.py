def nuc(n):
    if n > 0:
        sum = 0
        for i in range(0, n):
            sum += nuc(i)
        return 2**sum
    else:
        return 0


print(nuc(5))
