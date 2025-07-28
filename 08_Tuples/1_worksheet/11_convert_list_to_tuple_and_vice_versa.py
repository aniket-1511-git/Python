'''
Description: Convert a list to a tuple and a tuple to a list using built-in functions.
Mastering conversion between these types is vital for interoperability in Python programs.
Input: lst = [1, 2, 3], tup = (4, 5, 6)
Output: Tuple: (1, 2, 3)
List: [4, 5, 6]
'''
lst = [1, 2, 3]
tup = (4, 5, 6)
l=list(tup)
t=tuple(lst)
print("Tup : ",t)
print("List : ",l)
