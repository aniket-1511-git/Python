'''
Description: Check if a specified value is present in any of the inner tuples in a tuple of tuples.
This teaches how to search through nested tuples, which is useful in multi-dimensional data handling.
Input: t = (('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime')), Check: 'White'
Output: True
'''
t = (('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime'))
f=0
for i in t:
    for j in i:
        if j=="White":
            f=1
if f==1:
    print("True")
else:
    print("False")