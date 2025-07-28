'''
Description: Check whether all elements in a tuple are unique using set comparison.
Ensures data integrity in scenarios where duplicate values are not allowed.
Input: t = (1, 2, 3, 4, 5)
Output: True
'''
t1 = (1, 2, 2, 4, 5)
f=0
for i in t1:
   c=t1.count(i)
   if c>1:
       f=1
       break
if f:
    print("False")
else :
    print("True")
    

