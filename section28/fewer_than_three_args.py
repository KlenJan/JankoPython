'''
@ensure_fewer_than_three_args
def add_all(*nums):
    return sum(nums)

add_all() # 0
add_all(1) # 1
add_all(1,2) # 3
add_all(1,2,3) # "Too many arguments!"
add_all(1,2,3,4,5,6) # "Too many arguments!"
'''

from functools import wraps


def ensure_fewer_than_three_args(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if len(args) > 2:
            return "Too many arguments!"
        else:
            return func(*args, **kwargs)
    return wrapper
