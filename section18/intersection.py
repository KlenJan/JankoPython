# flesh out intersection pleaseeeee
def intersection(list1, list2):
    """_summary_

    Args:
        list1 (_type_): _description_
        list2 (_type_): _description_

    Returns:
        _type_: _description_
    >>> intersection([1,2,3], [3,4,5])
    [3]
    >>> intersection(1, [1,2,3])
    Traceback (most recent call last):
        ...
    TypeError: 'int' object is not iterable
    """
    return [x for x in list1 if x in list2]
