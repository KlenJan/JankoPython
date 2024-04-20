import keyword


def contains_keyword(*args):
    for x in args:
        if keyword.iskeyword(x):
            return True
    return False


print(contains_keyword("defo", "haha", "lol", "chicken", "alaska"))
