import sqlite3

conn = sqlite3.connect("my_friends.db")
# create cursor object
c = conn.cursor()
# execute some sql
# c.execute("CREATE TABLE friends(first_name TEXT, last_name TEXT, closeness INTEGER);")
exe_query = '''INSERT INTO friends
VALUES ('Tomas', 'Madel', 5)
;
'''
c.execute(exe_query)
# commit changes
conn.commit()
conn.close()
