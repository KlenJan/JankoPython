'''
add_user("Dwayne", "Johnson") # None
# CSV now has two data rows:

# First Name,Last Name
# Colt,Steele
# Dwayne,Johnson
'''

from csv import writer

def add_user(first, last):
    with open('users.csv', 'a') as f:
        csv_writer = writer(f)
        csv_writer.writerow([first, last])