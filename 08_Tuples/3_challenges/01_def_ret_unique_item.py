'''
Description: Write a function that accepts a tuple and returns a new tuple with only unique elements, preserving the original order.
This task is useful for removing duplicates from a tuple while ensuring the order of elements remains unchanged.
Input: t = (1, 2, 2, 3, 1, 4)
Output: (1, 2, 3, 4)
'''
def removeDup(t:tuple):
    l=[]
    for i in t:
        if i not in l:
            l.append(i)
    l=tuple(l)
    return l            
t = (1, 2, 2, 3, 1, 4)
t=removeDup(t)
print(t)