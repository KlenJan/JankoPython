def sum_even_values(*args):
    return sum(x for x in args if x % 2 == 0)
