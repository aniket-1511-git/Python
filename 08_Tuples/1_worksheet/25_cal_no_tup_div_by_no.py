'''
Description: Count the number of tuples where every element is divisible by a given integer K.
This builds filtering skills and strengthens logic construction for data validation.
Input: lst = [(3, 6), (9, 12, 15), (4, 8)], K = 3
Output: 2
'''
l1 = [(3, 6), (9, 12, 15), (4, 8)]
k = 3
c1=0
for i in l1:
    c=0
    for j in i:
        if j%k==0:
            c+=1
    if c== len(i):
        c1+=1    
print(c1)