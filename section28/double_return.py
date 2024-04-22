'''
@double_return 
def add(x, y):
    return x + y
    
add(1, 2) # [3, 3]

@double_return
def greet(name):
    return "Hi, I'm " + name

greet("Colt") # ["Hi, I'm Colt", "Hi, I'm Colt"]
'''


def double_return(func):
    def wrapper(*args, **kwargs):
        return [func(*args, **kwargs), func(*args, **kwargs)]
    return wrapper
