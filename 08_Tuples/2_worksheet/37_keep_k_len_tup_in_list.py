'''
Description: Filter a list of tuples, keeping only those where the tuple length or value at a specific index meets a condition.
This task helps develop conditional filtering skills and deeper data selection logic in nested structures.
Input: lst = [(1, 2, 3), (4, 5), (6, 7, 8)], Keep tuples of length 3
Output: [(1, 2, 3), (6, 7, 8)]
'''
l1= [(1, 2, 3), (4, 5), (6, 7, 8)]
for i in l1:
    if len(i)!=3:
        l1.remove(i)
print(l1)
