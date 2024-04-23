'''
frequency([1,2,3,4,4,4], 4) # 3
frequency([True, False, True, True], False) # 1
'''


def frequency(input_list, search_term):
    """_summary_

    Args:
        input_list (_type_): _description_
        search_term (_type_): _description_

    Returns:
        _type_: _description_
    >>> frequency([1,2,3,4,4,4], 4)
    3
    >>> frequency([], "something")
    0
    >>> frequency([1,2,3], "1")
    0
    """
    return input_list.count(search_term)
