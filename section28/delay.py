'''
@delay(3)
def say_hi():
    return "hi"

say_hi()
# should print the message "Waiting 3s before running say_hi" to the console
# should then wait 3 seconds
# finally, should invoke say_hi and return "hi"
'''

from functools import wraps
from time import sleep


def delay(timesec):
    def inner(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"Waiting {timesec}s before running say_hi")
            sleep(timesec)
            return func(*args, **kwargs)
        return wrapper
    return inner
