'''
Description: Given a list of tuples, count and print the number of elements before encountering a tuple in the list.
This teaches control flow and type checking within mixed-type data collections.
Input: lst = [1, 2, 3, (4, 5), 6]
Output: 3
'''
l1= [1, 2, 3, (4, 5), 6]
c=0
for i in l1:
    if type(i)!= tuple:
        c+=1
    else:
        break
print(c)
