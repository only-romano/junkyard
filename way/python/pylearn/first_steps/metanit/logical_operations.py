#! Metanit.com - Python: Chapter 2, lesson 4 "Logical operations".

# Boolean variables.
a, b = 5, 6
result = a == b
print(result)

print(a != b, a > b, a < b)

bool1, bool2 = True, False
print(bool1 == bool2)

age, weight, isMarried = 27, 133, False

# 'And' operation returns 'True' if all expressions are 'True'.
print(age > 21 and weight == 133)

# 'Or' operation returns 'True' if any of expressions is 'True' or both.
print(age > 21 or isMarried)

# 'Not' operation return 'True' if expression is 'False'.
print(not age > 21, not isMarried)

# Priorities of operations: not ->  and -> or.
print(weight == 133 or isMarried and not age >= 21)

# Redistribution of logic operations order.
print((weight == 70 or isMarried) and not age < 21)
