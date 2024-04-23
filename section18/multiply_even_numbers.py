'''
multiply_even_numbers([2,3,4,5,6]) # 48
'''


def multiply_even_numbers(list_numbers):
    """_summary_

    Args:
        list_numbers (_type_): _description_

    Returns:
        _type_: _description_
    >>> multiply_even_numbers([2,2,2,2,2])
    32
    >>> multiply_even_numbers([3,3,3,3,3])
    0
    >>> multiply_even_numbers([1,2,3])
    2
    """
    total = 1
    for number in list_numbers:
        if number % 2 == 0:
            total *= number
    return total if total != 1 else 0


multiply_even_numbers([2, 3, 4, 5, 6])  # 48
