'''
single_letter_count("Hello World", "h") # 1
single_letter_count("Hello World", "z") # 0
single_letter_count("HelLo World", "l") # 3
'''

# define single_letter_count below:


def single_letter_count(sample_string, sample_letter):
    """_summary_

    Args:
        sample_string (_type_): _description_
        sample_letter (_type_): _description_

    Returns:
        _type_: _description_
    >>> single_letter_count("Hello World", "h")
    1
    >>> single_letter_count("Hello World", "z")
    0
    """
    return sample_string.lower().count(sample_letter.lower())
