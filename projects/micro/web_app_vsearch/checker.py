from functools import wraps

def check_log_in(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if True:
            return func(*args, **kwargs)
        return "<h4>Permission Denied</h4>"
    return wrapper
