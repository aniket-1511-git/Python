'''
Sort the keys inside each nested dictionary by their value.
Input: d = {'group1': {'b': 2, 'a': 1}, 'group2': {'c': 3, 'd': 0}}
Expected Output: {'group1': [('a', 1), ('b', 2)], 'group2': [('d', 0), ('c', 3)]}
'''
d = {'group1': {'b': 2, 'a': 1}, 'group2': {'c': 3, 'd': 0}}
result = {k: sorted(v.items(), key=lambda item: item[1]) for k, v in d.items()}
print(result)