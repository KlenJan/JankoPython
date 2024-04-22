'''
gen = yes_or_no()
next(gen) # 'yes'
next(gen) # 'no'
next(gen) # 'yes'
next(gen) # 'no'
'''


def yes_or_no():
    answers = ('yes', 'no')
    curr = 0
    while True:
        if curr:
            yield answers[curr]
            curr = 0
        else:
            yield answers[curr]
            curr = 1


a = yes_or_no()
print(next(a))
print(next(a))
print(next(a))
print(next(a))

for i in a:
    print(i)
