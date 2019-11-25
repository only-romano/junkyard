default_names = ['orange', 'tomato', 'pie']

class Limiter:
    __slots__ = default_names


if __name__ == '__main__':
    x = Limiter()
    x.orange = 11
    print(x.orange)
    # x['gold'] = 2
