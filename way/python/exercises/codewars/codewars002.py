
def series_sum(n):
    new_n, z = 0.00, 0.00
    while n > 0:
        z += 1 / (1 + new_n)
        n -= 1
        new_n += 3
    return format(round(z, 2), '.2f')


print(series_sum(1))
print(series_sum(2))
print(series_sum(3))
