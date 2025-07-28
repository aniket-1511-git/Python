'''
Description: Convert a tuple of nested tuples into a single flat tuple.
Flattening data structures is often needed for uniform data processing and analysis.
Input: t = ((1, 2), (3, 4), (5, 6))
Output: (1, 2, 3, 4, 5, 6)
'''
t = ((1, 2), (3, 4), (5, 6))
l=[]
for i in t:
    for j in i:
        l.append(j)
l=tuple(l)
print(l)
        