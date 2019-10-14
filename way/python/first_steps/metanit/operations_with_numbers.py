#! Metanit.com - Python: Chapter 2, lesson 3 "Operations with Numbers".

y = 0x0a    # hexadecimal system, 11
a = 0o11    # octal system, 9
x = 0b101   # binary system, 5

z = x + y

# Awesome string formatters.
print("{0} in binary {0:08b}; in hex {0:02x} in octal {0:02o}".format(z))
# {:n} - 'n' indicates how many characters are displayed, empty ones are
# replaced by zeros.

# Order of operations: degree, multiplication, addition.
number = 3 + 4 * 5 ** 2 + 7
print(number)

# Redistribution of operations order.
number = (3 + 4) * (5 ** 2 + 7)
print(number)

# Augmented assignment operators or compound assignment operators.
number = 12
number += 5
print(number)

number -= 3
print(number)

number *= 4
print(number)

number //= 9
print(number)

number **= 4
print(number)

# Bringing to the desired data type.
first_number, second_number = "2", 3
third_number = int(first_number) + second_number
print(third_number)

# Rounding.  The second parameter is the number of decimal places.
first_number = 2.00001
second_number = 5
third_number = first_number / second_number
print(round(third_number, 4))

print(round(2.0001 + 1, 4))
