'''
Description: Find all possible pair combinations from two tuples, combining each element from the first tuple with each from the second.
This problem introduces the concept of Cartesian product and is useful for combinatorial tasks.
Input: t1 = (1, 2), t2 = (3, 4)
Output: [(1, 3), (1, 4), (2, 3), (2, 4)]
'''
t1 = (1, 2)
t2 = (3, 4)
l1=[]
for i in t1:
    for j in t2:
        l1.append((i,j))
l1=tuple(l1)
print(l1)
