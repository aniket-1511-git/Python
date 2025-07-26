'''
Task: Write a Python program to get the largest number from a list.
Sample input: [1, 2, 3, 4, 5]
Output: 5
'''
l=[1, 2, 3, 4, 5]
m=l[0]
i=0
while i<len(l):
    if l[i]>m:
        m=l[i]
    i+=1
print("max : ",m)