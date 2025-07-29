'''
Remove all keys whose value is greater than a given number. Ignore non-numeric values.
Input: d = {'a': 5, 'b': 10, 'c': 15, 'd': 'big'}, limit = 10
Expected Output: {'a': 5, 'b': 10, 'd': 'big'}
'''
d = {'a': 5, 'b': 10, 'c': 15, 'd': 'big'}
limit = 10
d = {'a': 5, 'b': 10, 'c': 15, 'd': 'big'}
limit = 10
d1 = {k: v for k, v in d.items() if not isinstance(v, (int, float)) or v <= limit}
print(d1)