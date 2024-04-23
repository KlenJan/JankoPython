'''
compact([0,1,2,"",[], False, {}, None, "All done"]) # [1,2, "All done"]
'''


def compact(truthy_list):
    """_summary_

    Args:
        truthy_list (_type_): _description_

    Returns:
        _type_: _description_

    >>> compact([0])
    []
    >>> compact([1])
    [1]
    >>> compact([0,1,2, None])
    [1, 2]
    """
    return [x for x in truthy_list if x]
