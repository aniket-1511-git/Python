'''
Task: Write a Python program to create a list of even numbers from a given list using list comprehension.
Sample input: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Output: [2, 4, 6, 8, 10]
'''
l1=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l2=[]
i=0
while i<len(l1):
    if l1[i]%2==0:
        l2.append(l1[i])
    i+=1
print(l2)