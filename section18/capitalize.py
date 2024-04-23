'''
capitalize("tim") # "Tim"
capitalize("matt") # "Matt"
'''


def capitalize(input_str):
    """_summary_

    Args:
        input_str (_type_): _description_

    Returns:
        _type_: _description_

    >>> capitalize("ahoj")
    'Ahoj'

    >>> capitalize("AHOJ")
    'AHOJ'

    >>> capitalize(123)
    Traceback (most recent call last):
        ...
    TypeError: 'int' object is not subscriptable
    """
    return input_str[0].upper() + input_str[1:]
