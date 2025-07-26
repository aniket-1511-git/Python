'''
Task: Write a Python program to find the common elements between two lists.
Sample input: [1, 2, 3, 4], [3, 4, 5, 6]
Output: [3, 4]
'''
l1=[1, 2, 3, 4]
l2=[3, 4, 5, 6]
i= 0
while i< len(l1):
    j=0
    while j<len(l2):
        if l1[i]==l2[j]:
            print(l1[i],end=" ")
        j+=1
    i+=1
        