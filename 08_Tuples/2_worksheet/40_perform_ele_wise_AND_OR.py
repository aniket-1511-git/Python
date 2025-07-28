'''
Description: Perform elementwise AND and XOR operations between two tuples of integers of equal length.
Elementwise bitwise operations are crucial in low-level data processing and algorithm optimization.
Input: t1 = (1, 2, 3), t2 = (2, 2, 2)
Output: AND: (0, 2, 2), XOR: (3, 0, 1)
'''
t1 = (1, 2, 3)
t2 = (2, 2, 2)
t3=[]
t4=[]
i=0
while i <len(t1):
    a=t1[i]&t2[i]
    t3.append(a)
    i+=1
t3=tuple(t3)
print(t3,end=" ")

i=0
while i <len(t1):
    a=t1[i]^t2[i]
    t4.append(a)
    i+=1
t4=tuple(t4)
print(t4)