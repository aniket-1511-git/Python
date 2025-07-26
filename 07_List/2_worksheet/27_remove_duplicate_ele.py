'''
Task: Write a Python function to remove duplicates from a list while preserving the original order of the remaining elements.
Sample input: [1, 2, 2, 3, 4, 4, 5, 6, 5]
Output: [1, 2, 3, 4, 5, 6]
'''
l1=[1, 2, 2, 3, 4, 4, 5, 6, 5]
l2=[]
for i in l1:
    if i not in l2:
        l2.append(i)
print(l2)
