'''
find_and_replace('story.txt', 'Alice', 'Colt') 
# story.txt now contains the first chapter of my new book,
# Colt's Adventures in Wonderland
'''

def find_and_replace(file, search_str, replacement_str):
    with open(file, 'r+') as nuke_codes:
        read_codes = nuke_codes.readlines()
        nuke_codes.seek(0)
        for i in read_codes:
            nuke_codes.write(i.replace(search_str, replacement_str))

find_and_replace('nukes.txt', 'Jan', 'XXX')