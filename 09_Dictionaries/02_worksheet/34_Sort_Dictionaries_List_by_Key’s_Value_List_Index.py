'''
Given a list of dictionaries, sort them by the value at a specific index in each key’s value list.
Input: dicts = [{'a': [5,1]}, {'a': [3,4]}, {'a': [7,0]}], index = 1
Expected Output: [{'a': [7,0]}, {'a': [5,1]}, {'a': [3,4]}]
'''
dicts = [{'a': [5,1]}, {'a': [3,4]}, {'a': [7,0]}]
index = 1
result = sorted(dicts, key=lambda d: list(d.values())[0][index])
print( result)