'''
Sort a dictionary by the sum of its list values, from smallest to largest.
Input: d = {'x': [5,5], 'y': [1,2,3], 'z': [10]}
Expected Output: [('y', [1,2,3]), ('x', [5,5]), ('z', [10])]
'''
d = {'x': [5,5], 'y': [1,2,3], 'z': [10]}
result = sorted(d.items(), key=lambda x: sum(x[1]))
print( result)