def sum_floats(*args):
    return sum(x for x in args if type(x) == float)
