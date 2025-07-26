'''
Task: Write a Python program to sum all the items in a list.
Sample input: [1, 2, 3, 4, 5]
Output: 15
'''
l=[1, 2, 3, 4, 5]
i = s=0
while i<len(l):
    s+=l[i]
    i+=1   
print("Output : ",s)