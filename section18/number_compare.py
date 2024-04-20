'''
number_compare(1,1) # "Numbers are equal"
number_compare(1,0) # "First is greater"
number_compare(2,4) # "Second is greater"
'''


def number_compare(first, second):
    if first == second:
        return "Numbers are equal"
    elif first > second:
        return "First is greater"
    return "Second is greater"
