'''
Find all keys that share the same value. Group keys by their values.
Input: d = {'m': 1, 'n': 2, 'o': 1}
Expected Output: {1: ['m', 'o'], 2: ['n']}
'''
d = {'m': 1, 'n': 2, 'o': 1}
r = {}
for k, val in d.items():
    r.setdefault(val, []).append(k)
print(r)