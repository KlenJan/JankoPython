def my_for(my_iterable, func):
    my_iterator = iter(my_iterable)
    while True:
        try:
            item = next(my_iterator)
        except StopIteration:
            break
        else:
            func(item)


def square(x):
    print(x*x)


my_for("hello", print)
my_for([1, 2, 3], square)
