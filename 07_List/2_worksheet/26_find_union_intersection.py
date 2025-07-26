'''
Task: Write a Python function to find the union and intersection of two lists.
Sample input: [1, 2, 3, 4], [3, 4, 5, 6]
Output: Union: [1, 2, 3, 4, 5, 6]
Intersection: [3, 4]
'''
l1=[1, 2, 3, 4]
l2=[3, 4, 5, 6]
l3=[]
print("union: ",end=" ")
for i in l1:
    if i not in l3:
        l3.append(i)
for i in l2:
    if i not in l3:
        l3.append(i)
print(l3)  
print("Intersection: ",end=" ")
i=0
while i<len(l1):
    j=0
    while j < len(l2):
        if l1[i]==l2[j]:
            print(l1[i],end=" ")
        j+=1
    i+=1
    
