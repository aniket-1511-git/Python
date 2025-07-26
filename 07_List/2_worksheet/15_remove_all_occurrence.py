'''
Task: Write a Python program to remove all occurrences of a specific element from a list.
Sample input: [1, 2, 3, 2, 4, 2, 5], element to remove: 2
Output: [1, 3, 4, 5]

'''
l=[1, 2, 3, 2, 4, 2, 5]
print(l)
for i in l:
    if i == 2:
        l.remove(i)
print(l)