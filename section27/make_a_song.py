'''
kombucha_song = make_song(5, "kombucha")
next(kombucha_song) # '5 bottles of kombucha on the wall.'
next(kombucha_song) # '4 bottles of kombucha on the wall.'
next(kombucha_song) # '3 bottles of kombucha on the wall.'
next(kombucha_song) # '2 bottles of kombucha on the wall.'
next(kombucha_song) # 'Only 1 bottle of kombucha left!'
next(kombucha_song) # 'No more kombucha!'
next(kombucha_song) # StopIteration

default_song = make_song()
next(default_song) # '99 bottles of soda on the wall.'
'''


def make_song(count=99, beverage="soda"):
    for i in range(count, -1, -1):
        if i > 1:
            yield f"{i} bottles of {beverage} on the wall."
        elif i == 1:
            yield f"Only {i} bottle of {beverage} left!"
        else:
            yield f"No more {beverage}!"


default_song = make_song()
print(next(default_song))
for i in default_song:
    print(i)
print(next(default_song))
