#! Static greet program


def name(user='Kato'):
    """Return name or default name"""
    return user


def greet(user=name()):
    """Greet default person"""
    return "Hello, {}!".format(user)


print(greet())
