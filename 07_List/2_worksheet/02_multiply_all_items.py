'''
Task: Write a Python program to multiply all the items in a list.
Sample input: [1, 2, 3, 4]
Output: 24
'''
l=[1, 2, 3, 4]
i =0
s=1
while i<len(l):
    s*=l[i]
    i+=1   
print("Output : ",s)