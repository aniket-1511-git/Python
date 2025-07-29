'''
Sometimes, you need to clean up or adjust your dictionary as data changes.
Remove key 'math' from marks = {'math': 80, 'science': 85} using del.
Use .pop() to remove 'name' from info = {'name': 'Amit', 'city': 'Pune'} and print the value removed.
Remove all items from the dictionary: d = {'x': 1, 'y': 2}.
Write a program to remove key 'z' from d = {'x': 1, 'y': 2} only if it exists.
Expected Output: If not found, print 'Key not found'.
'''
marks = {'math': 80, 'science': 85}
del marks['math']
print(marks)
info = {'name': 'Amit', 'city': 'Pune'}
info.pop('name')
print(info)
d = {'x': 1, 'y': 2}
# d.clear()
if 'z' in d:
    d.pop('z')
else:
    print("Key not found")
print(d)

