'''
Description: Find all unique elements present in a tuple of tuples using set logic.
This teaches set operations and how to process nested iterable structures.
Input: t = ((1, 2), (2, 3), (4, 5))
Output: {1, 2, 3, 4, 5}
'''
t = ((1, 2), (2, 3), (4, 5))
l=[]
for i in t:
    for j in i:
        if j not in l:
            l.append(j)
l=set(l)
print(l)