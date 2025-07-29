'''
Add Dictionary Items
Dynamic addition of new items allows for scalable and flexible data storage.
Add 'Bangalore': 12000000 to cities = {'Delhi': 18000000, 'Mumbai': 20000000}.
Add a key 'status' with value 'active' to user = {'name': 'Riya'} only if it doesn’t exist.
Given a list ['dog', 'cat', 'rabbit'], create a dictionary with words as keys and their lengths as values.
Expected Output: {'dog': 3, 'cat': 3, 'rabbit': 6}
Merge two dictionaries: d1 = {'x': 1} and d2 = {'y': 2}.
Expected Output: {'x': 1, 'y': 2}
'''
cities = {'Delhi': 18000000, 'Mumbai': 20000000}
print(cities)
cities.update({'Bangalore': 12000000})
print(cities)
usr = {'name': 'Riya'}
print(usr)
usr.update({'status': 'active'})
print(usr)
animal=['dog', 'cat', 'rabbit']
l=[3,3,6]
aml=dict(zip(animal,l))
print(aml)
d1 = {'x': 1} 
d2 = {'y': 2}
d1.update(d2)
print(d1)
