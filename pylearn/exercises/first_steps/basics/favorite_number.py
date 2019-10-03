#! Favorite number program


def favorite_number(num=17):
    """Returns your favorite number"""
    return 'Your favorite number is {} and it\'s awesome!'.format(str(num))


if __name__ == '__main__':
    print(favorite_number())
