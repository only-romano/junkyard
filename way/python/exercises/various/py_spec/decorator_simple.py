def decorate(func):
    print("decorate func outro")
    def wrapper_func(*args):
        print("decorate func intro", func.__name__)
        return func(*args)
    return wrapper_func

@decorate
def my_func(param):
    print(param)

my_func("hello")
