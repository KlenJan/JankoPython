'''
update_users("Grace", "Hopper", "Hello", "World") # Users updated: 1.
update_users("Colt", "Steele", "Boba", "Fett") # Users updated: 2.
update_users("Not", "Here", "Still not", "Here") # Users updated: 0.
'''

from csv import reader, writer
def update_users(old_first, old_last, new_first, new_last):
    counter = 0
    with open('users.csv', 'r') as f:
        csv_reader = list(reader(f))
        for i in csv_reader:
            if i[0] == old_first and i[1] == old_last:
                i[0] = new_first
                i[1] = new_last
                counter += 1
        with open('users.csv', 'w', newline='') as f2:
            csv_writer = writer(f2)
            csv_writer.writerows(csv_reader)
    return f"Users updated: {counter}."


update_users("Grace", "Hopper", "Hello", "World")