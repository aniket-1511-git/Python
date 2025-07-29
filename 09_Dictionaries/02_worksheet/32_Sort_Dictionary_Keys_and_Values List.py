'''
Sort a dictionary by keys, and also sort the values list of each key.
Input: d = {'c': [3,1], 'a': [2,4], 'b': [5,1]}
Expected Output: [('a', [2,4]), ('b', [1,5]), ('c', [1,3])]
'''
d = {'c': [3,1], 'a': [2,4], 'b': [5,1]}
result = sorted((k, sorted(v)) for k, v in d.items())
print( result)