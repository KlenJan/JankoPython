'''
days = week()
next(days) # 'Monday'
next(days) # 'Tuesday'
next(days) # 'Wednesday'
next(days) # 'Thursday'
next(days) # 'Friday'
next(days) # 'Saturday'
next(days) # 'Sunday'
next(days) # StopIteration
'''


def week():
    weekdays = ['Monday', 'Tuesday', 'Wednesday',
                'Thursday', 'Friday', 'Saturday', 'Sunday']
    for i in weekdays:
        yield i


days = week()
print(next(days))
print(next(days))
for i in days:
    print(i)
for i in days:
    print(i)
print(next(days))
