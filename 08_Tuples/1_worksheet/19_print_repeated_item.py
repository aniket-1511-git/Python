'''
Description: Identify and print elements that occur more than once in a tuple.
Spotting duplicates in sequences is common in data cleaning and interviews.
Input: t = (2, 4, 6, 2, 8, 4, 6, 2)
Output: 2, 4, 6
'''
t1 = (2, 4, 6, 2, 8, 4, 6, 2)
t2=()
for i in t1:
    c= t1.count(i)
    if c>1 and i not in t2:
        t2=t2+(i,)
print(t2)
