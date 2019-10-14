def get_sum(a,b):
    return a if a == b else sum(range(min(a, b), max(a,b) + 1))

print(get_sum(1, 0))