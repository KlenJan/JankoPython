'''
@only_ints
def add(x, y):
    return x + y

add(1, 2) # 3
add("1", "2") # "Please only invoke with integers."
'''

from functools import wraps


def only_ints(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if all(isinstance(x, int) for x in args) and all(isinstance(x, int) for x in kwargs):
            return func(*args, **kwargs)
        return "Please only invoke with integers."
    return wrapper


@ only_ints
def add(x, y):
    return x + y


print(add(1, 2))
print(add("1", "2"))
