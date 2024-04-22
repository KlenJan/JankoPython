'''
evens = get_multiples(2, 3)
next(evens) # 2
next(evens) # 4
next(evens) # 6
next(evens) # StopIteration

default_multiples = get_multiples()
list(default_multiples) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
'''


def get_multiples(num=1, ct=10):
    base_num = num
    for i in range(0, ct):
        yield num
        num += base_num


default_multiples = get_multiples()
another_multiples = get_multiples(3, 5)
print(list(default_multiples))
print(list(another_multiples))
