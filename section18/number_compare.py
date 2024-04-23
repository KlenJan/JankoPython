'''
number_compare(1,1) # "Numbers are equal"
number_compare(1,0) # "First is greater"
number_compare(2,4) # "Second is greater"
'''


def number_compare(first, second):
    """_summary_

    Args:
        first (_type_): _description_
        second (_type_): _description_

    Returns:
        _type_: _description_
    >>> number_compare(1,1)
    'Numbers are equal'
    >>> number_compare(1,0)
    'First is greater'
    >>> number_compare(2,4)
    'Second is greater'
    """
    if first == second:
        return "Numbers are equal"
    elif first > second:
        return "First is greater"
    return "Second is greater"
