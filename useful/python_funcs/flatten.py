# Flatten nested generator
def flatten(nested):
    try:
        # Don't iterate over string-like objects:
        try: nested + ''
        except TypeError: pass
        else: raise TypeError

        for sublist in nested:
            for element in flatten(sublist):
                yield element
    except TypeError:
        yield nested


if __name__ == '__main__':
    print(list(flatten([[[1], 2], 3, 4, [5, [6, 7]], 8])))
    print(list(flatten("122")))
    print(list(flatten(['foo', ['bar', ['baz']]])))
