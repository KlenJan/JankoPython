'''
multiple_letter_count("awesome") # {'a': 1, 'e': 2, 'm': 1, 'o': 1, 's': 1, 'w': 1}
'''

# flesh out multiple_letter count:


def multiple_letter_count(input_string):
    """_summary_

    Args:
        input_string (_type_): _description_

    Returns:
        _type_: _description_
    >>> multiple_letter_count("awesome")
    {'a': 1, 'w': 1, 'e': 2, 's': 1, 'o': 1, 'm': 1}
    """
    return {x: input_string.count(x) for x in input_string}
