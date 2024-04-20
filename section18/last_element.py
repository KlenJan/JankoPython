'''
last_element([1,2,3]) # 3
last_element([]) # None
'''


def last_element(zoznam: list):
    return zoznam[-1] if zoznam else None
