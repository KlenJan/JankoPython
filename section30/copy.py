'''
copy('story.txt', 'story_copy.txt') # None
# expect the contents of story.txt and story_copy.txt to be the same
'''

def copy(oldfile, newfile):
    with open(oldfile, 'r') as oldf:
        with open (newfile, 'w') as newf:
            newf.write(oldf.read())

copy('oldfile.txt', 'newfile.txt')