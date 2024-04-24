'''
find_user("Colt", "Steele") # 1
find_user("Alan", "Turing") # 3
find_user("Not", "Here") # 'Not Here not found.'
'''

from csv import DictReader

def find_user(first, last):
    with open('users.csv', 'r') as f:
        dict_reader = list(DictReader(f))
        for x in dict_reader:
            if first and last in x.values():
                return dict_reader.index(x) + 1
        return f"{first} {last} not found."