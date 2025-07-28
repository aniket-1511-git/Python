'''
Description: Remove all empty tuples from a list of tuples and print the cleaned list.
This is useful for sanitizing input data before processing.
Input: lst = [(), (), ('a', 'b'), ('c',)]
Output: [('a', 'b'), ('c',)]
'''
l1= [(), (), ('a', 'b'), ('c',)]
l2=[]
for i in l1:
    if len(i)!=0:
        l2.append(i)
        
print(l2)
