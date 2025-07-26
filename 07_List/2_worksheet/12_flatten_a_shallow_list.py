'''
Task: Write a Python program to flatten a shallow list.
Sample input: [[1, 2], [3, 4], [5, 6]]
Output: [1, 2, 3, 4, 5, 6]
'''
l=[[1, 2], [3, 4], [5, 6]]
i=0
while i<len(l):
    print(l[i],end=" ")
    i+=1