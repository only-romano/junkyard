#! File writing 'x' power 'y' program


def power(x, y):
    """Exponentiation 'x' power 'y'"""
    return x ** y


# Creation and writing to the file
file = open('exponentiation.txt', 'w')
file.write(str(power(3, 7)))
file.close()
