'''
Description: Compute the element-wise sum of multiple tuples of equal length.
This exercise teaches how to combine tuples by adding corresponding elements, often used in mathematical and data processing tasks.
Input: t1 = (1, 2, 3, 4), t2 = (3, 5, 2, 1), t3 = (2, 2, 3, 1)
Output: (6, 9, 8, 6)
'''
t1 = (1, 2, 3, 4)
t2 = (3, 5, 2, 1)
t3 = (2, 2, 3, 1)
t4=[]
i=0
while i <len(t1):
    a=t1[i]+t2[i]+t3[i]
    t4.append(a)
    i+=1
t4=tuple(t4)
print(t4)