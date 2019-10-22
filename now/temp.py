
def equantion(x_coef, y_coef, num_coef):
    return {(x, y) for x in range(-100, 100) for y in range(-100, 100) if \
        (x_coef * x**2 + y_coef * y**2 + num_coef == 0)}

if __name__ == '__main__':
    print(equantion(5, 2, -32))
