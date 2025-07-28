# Description: Flatten a tuple that contains lists as elements into a single tuple containing all the items.
# This helps in unifying data structures for easier processing and analysis.
# Input: t = ([1, 2], [3, 4], [5, 6])
# Output: (1, 2, 3, 4, 5, 6)
t = ([1, 2], [3, 4], [5, 6])
l=[]
for i in t:
    for j in i:
        l.append(j)
t=tuple(l)
print(t)