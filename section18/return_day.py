'''
return_day(1) # "Sunday"
return_day(2) # "Monday"
return_day(3) # "Tuesday"
return_day(4) # "Wednesday"
return_day(5) # "Thursday"
return_day(6) # "Friday"
return_day(7) # "Saturday"
return_day(41) # None
'''

weekdays = {
    1: "Sunday",
    2: "Monday",
    3: "Tuesday",
    4: "Wednesday",
    5: "Thursday",
    6: "Friday",
    7: "Saturday"
}


def return_day(number: int):
    """_summary_

    Args:
        number (int): _description_

    Returns:
        _type_: _description_
    >>> return_day(1)
    'Sunday'
    >>> return_day(45564)

    """
    if number in weekdays:
        return weekdays[number]
    return None
