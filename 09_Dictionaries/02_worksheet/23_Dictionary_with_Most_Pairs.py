'''Given multiple dictionaries, find the one with the most key-value pairs (the biggest dictionary wins).
Input: dicts = [{'a': 1, 'b': 2}, {'x': 1, 'y': 2, 'z': 3}, {'k': 9}]
Expected Output: {'x': 1, 'y': 2, 'z': 3}'''
dicts = [{'a': 1, 'b': 2}, {'x': 1, 'y': 2, 'z': 3}, {'k': 9}]
max_d=max(dicts,key=len)
print(max_d)