#! Replace With Alphabet Position


def square_of_squares(x):
    return True if x**0.5 - round(x**0.5, 0) == 0 else False


print(square_of_squares(4))
print(square_of_squares(400))
print(square_of_squares(2669375556))
print(square_of_squares(266937555))
print(square_of_squares(14))
print(square_of_squares(169))
