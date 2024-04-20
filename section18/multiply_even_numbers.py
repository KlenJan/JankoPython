'''
multiply_even_numbers([2,3,4,5,6]) # 48
'''


def multiply_even_numbers(list_numbers):
    total = 1
    for number in list_numbers:
        if number % 2 == 0:
            total *= number
    return total


multiply_even_numbers([2, 3, 4, 5, 6])  # 48
