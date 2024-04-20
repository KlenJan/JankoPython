def is_all_strings(some_iterable):
    return all(x is str() for x in some_iterable)
