'''
def isEven(num):
    return num % 2 == 0

partition([1,2,3,4], isEven) # [[2,4],[1,3]]
'''


def partition(input_list, callback):
    """_summary_

    Args:
        input_list (_type_): _description_
        callback (function): _description_

    Returns:
        _type_: _description_
    >>> partition([1,2,3,4], isEven)
    [[2, 4], [1, 3]]
    """
    return [[x for x in input_list if callback(x)], [x for x in input_list if not callback(x)]]


def isEven(input_num):
    if input_num % 2 == 0:
        return True
    return False
