'''
copy_and_reverse('story.txt', 'story_reversed.txt') # None
# expect the contents of story_reversed.txt to be the reverse of the contents of story.txt
'''

def copy_and_reverse(oldfile, newfile):
    with open(oldfile, 'r') as oldf:
        with open (newfile, 'w') as newf:
            newf.write((oldf.read())[::-1])

copy_and_reverse('oldfile.txt', 'newfile.txt')