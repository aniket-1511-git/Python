'''
Extract all unique values from the dictionary. How many distinct items are there?
Input: d = {'a': 1, 'b': 2, 'c': 2, 'd': 3}
Expected Output: [1, 2, 3]
'''
d = {'a': 1, 'b': 2, 'c': 2, 'd': 3}
l=[]
for k,val in d.items():
    if val not in l:
        l.append(val)
print(l)