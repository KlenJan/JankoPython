'''
delete_users("Grace", "Hopper") # Users deleted: 1.
delete_users("Colt", "Steele") # Users deleted: 2.
delete_users("Not", "Here") # Users deleted: 0.
'''

from csv import reader, writer
def delete_users(first, last):
    counter = 0
    with open('users.csv', 'r') as f:
        csv_reader = list(reader(f))

    with open('users.csv', 'w', newline='') as f:
        csv_writer = writer(f)
        for i in csv_reader:
            if not (i[0] == first and i[1] == last):
                csv_writer.writerow(i)
            else:
                counter +=1
    return f"Users deleted: {counter}."

delete_users("Grace", "Hopper")