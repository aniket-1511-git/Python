'''
Description: From a list of tuples, keep only those where all numbers are positive.
Filtering based on condition is commonly used for cleaning or selecting data.
Input: lst = [(1, 2), (-3, 4), (5, 6)]
Output: [(1, 2), (5, 6)]
'''
l1 = [(1, 2), (-3, 4), (5, 6)]
c1=0
for i in l1:
    c=0
    for j in i:
        if j>0:
            c+=1
    if c== len(i):
        print(i,end=" ")           