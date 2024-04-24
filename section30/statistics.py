'''
statistics('story.txt') 
# {'lines': 172, 'words': 2145, 'characters': 11227}
'''

def statistics(filename):
    with open(filename, 'r') as f:
        flist = f.readlines()

    return {
        "lines": len(flist),
        "words": sum(len(x) for x in (x.split(" ") for x in flist)),
        "characters": sum((len(x) for x in flist))
    }

    
print(statistics('statistics.txt'))