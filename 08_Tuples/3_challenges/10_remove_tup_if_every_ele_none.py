'''
Description: Remove tuples from a list where every element is None, keeping only valid data tuples.
This is a real-world data cleaning task commonly required when working with incomplete or missing data.
Input: lst = [(None, None), (1, 2), (None, 3), (4, 5), (None, None)]
Output: [(1, 2), (None, 3), (4, 5)]
'''
l1= [(None, None), (1, 2), (None, 3), (4, 5), (None, None)]
for i in l1:
    c=0
    for j in i:
        if j ==None:
            c+=1
    if c==len(i):
        l1.remove(i)
print(l1)