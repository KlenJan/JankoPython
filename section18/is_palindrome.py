'''
is_palindrome('testing') # False
is_palindrome('tacocat') # True
is_palindrome('hannah') # True
is_palindrome('robert') # False
is_palindrome('amanaplanacanalpanama') # True
'''


def is_palindrome(input_str):
    """_summary_

    Args:
        input_str (_type_): _description_

    Returns:
        _type_: _description_
    >>> is_palindrome('testing')
    False
    >>> is_palindrome('tacocat')
    True
    """
    mod_str = input_str.strip().lower()
    return mod_str == mod_str[::-1]
