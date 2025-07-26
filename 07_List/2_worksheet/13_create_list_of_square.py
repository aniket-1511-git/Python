''''
Task: Write a Python program to create a list of squares from 1 to 10 using list comprehension.
Sample input: Range: 1 to 10
Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
'''
j=0
l=[]
for i in range(1,11):
    l.append(i*i)
    i+=1
print(l)