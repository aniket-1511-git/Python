'''
Task: Write a Python function to reverse a list at a specific location.
Sample input: [1, 2, 3, 4, 5, 6], position: 3
Output: [1, 2, 3, 6, 5, 4]
'''
l1=[1, 2, 3, 4, 5, 6]
i=0
p=3
l=len(l1)
l2=[]
while i<p:
    l2.append(l1[i])
    i+=1
l-=1
while l>=p:
    l2.append(l1[l])
    l-=1
l1=l2
print(l1)