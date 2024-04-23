'''
last_element([1,2,3]) # 3
last_element([]) # None
'''


def last_element(zoznam: list):
    """_summary_

    Args:
        zoznam (list): _description_

    Returns:
        _type_: _description_
    >>> last_element([1,2,3])
    3
    >>> last_element(["abc","efg"])
    'efg'
    >>> last_element([])

    """
    return zoznam[-1] if zoznam else None
