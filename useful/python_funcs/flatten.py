# Flatten nested recursive
def flatten(nested):
    try:
        for sublist in nested:
            for element in flatten(sublist):
                yield element
    except TypeError:
        yield nested


if __name__ == '__main__':
    print(list(flatten([[[1], 2], 3, 4, [5, [6, 7]], 8])))
