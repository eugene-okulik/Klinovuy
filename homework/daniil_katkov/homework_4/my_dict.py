my_dict = {
    'tuple': (1, 3, 1, 'name', True),
    'list': [False, 'Daniil', 8, 'Python'],
    'dict': {'my_name': 'Daniil', 'username': 'Klinovuy', 'age': 32, 'city': 'Kharkiv', 'male': True},
    'set': {8, 12, True, 'life', 3.26}
}

print(my_dict['tuple'][-1])
my_dict['list'].append(40)
my_dict['list'].pop(1)
my_dict['dict']['i am a tuple'] = True
my_dict['dict'].pop('my_name')
my_dict['set'].add('Daniil')
my_dict['set'].remove(True)

print(my_dict)
