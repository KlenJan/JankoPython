'''
print_users() # None
# prints to the console:
# Colt Steele
'''

from csv import reader
def print_users():
    with open('users.csv', 'r') as f:
        csv_reader = reader(f)
        next(csv_reader)
        for i in csv_reader:
            print(f"{i[0]} {i[1]}")


# OR

from csv import DictReader
def print_users_dict():
    with open('users.csv', 'r') as f:
        csv_reader = DictReader(f)
        for i in csv_reader:
            print(f"{i['Name']} {i['Last Name']}")