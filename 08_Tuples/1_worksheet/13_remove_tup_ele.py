'''
Description: Remove a specific element from a tuple by converting it to a list and back.
Removing elements from tuples is a common interview question testing immutability handling.
Input: t = (1, 2, 3, 4), Remove: 2
Output: (1, 3, 4)
'''
t = (1, 2, 3, 4)
i=t.index(2)
t=t[:i]+t[i+1:]
print(t)