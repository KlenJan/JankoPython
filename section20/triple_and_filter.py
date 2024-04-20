'''
triple_and_filter([1,2,3,4]) # [12]
triple_and_filter([6,8,10,12]) # [24,36]
'''


def triple_and_filter(num_list):
    return [x*3 for x in filter(lambda x: x % 4 == 0, num_list)]
