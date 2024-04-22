'''
@ensure_authorized
def show_secrets(*args, **kwargs):
    return "Shh! Don't tell anybody!"

show_secrets(role="admin") # "Shh! Don't tell anybody!"
show_secrets(role="nobody") # "Unauthorized"
show_secrets(a="b") # "Unauthorized"
'''

from functools import wraps


def ensure_authorized(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if any(x for x in kwargs.keys() if x == "role") and any(x for x in kwargs.values() if x == "admin"):
            return func(*args, **kwargs)
        return "Unauthorized"
    return wrapper


@ensure_authorized
def show_secrets(*args, **kwargs):
    return "Shh! Don't tell anybody!"


print(show_secrets(role="admin"))
