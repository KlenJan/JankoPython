'''
list_manipulation([1,2,3], "remove", "end") # 3
list_manipulation([1,2,3], "remove", "beginning") #  1
list_manipulation([1,2,3], "add", "beginning", 20) #  [20,1,2,3]
list_manipulation([1,2,3], "add", "end", 30) #  [1,2,3,30]
'''


def list_manipulation(input_list, command, index_location, value=None):
    """_summary_

    Args:
        input_list (_type_): _description_
        command (_type_): _description_
        index_location (_type_): _description_
        value (_type_, optional): _description_. Defaults to None.

    Returns:
        _type_: _description_
    >>> list_manipulation([1,2,3], "remove", "end")
    3
    >>> list_manipulation([1,2,3], "remove", "beginning")
    1
    """
    if command == "remove":
        return input_list.pop(-1) if index_location == "end" else input_list.pop(0)
    if command == "add":
        input_list.insert(len(
            input_list), value) if index_location == "end" else input_list.insert(0, value)
        return input_list
