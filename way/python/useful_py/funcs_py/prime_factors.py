# Prime factors function
import math

def prime_factors(num):
    # returns a list of prime factors of number
    factors = []
    for i in range(2, math.ceil(num**0.5)):
        if num < i and num > 1:
            factors.append(int(num))
            num /= num
            break
        if is_primal(i):
            while num % i == 0:
                factors.append(i)
                num = num / i
    if num > 1:
        factors.append(int(num))
    return factors


def is_primal(num):
    # checks if a number is primal
    for i in range(2, math.ceil(num**0.5)):
        if num % i == 0:
            return False
    return True
