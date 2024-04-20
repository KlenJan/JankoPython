'''
names = [{'first': 'Elie', 'last': 'Schoppik'},
    {'first': 'Colt', 'last': 'Steele'}]
extract_full_name(names) # ['Elie Schoppik', 'Colt Steele']
'''


def extract_full_name(dict_list):
    return [' '.join(x) for x in zip((x['first'] for x in dict_list), (x['last'] for x in dict_list))]


names = [{'first': 'Elie', 'last': 'Schoppik'},
         {'first': 'Colt', 'last': 'Steele'}]
print(extract_full_name(names))  # ['Elie Schoppik', 'Colt Steele']


def extract_full_name_different(dict_list):
    return list(map(lambda x: f"{x['first']} {x['last']}", dict_list))


print(extract_full_name_different(names))
