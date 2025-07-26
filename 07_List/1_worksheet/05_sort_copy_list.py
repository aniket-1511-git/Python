'''
5. Sorting and Copying Lists
Log Session a list of numbers: [3, 1, 4, 2, 5].
Sort the list in ascending order.
Sort the list in descending order.
Copy the sorted list to a new list.
Print both lists to verify they are separate copies.
'''
l1=[3, 1, 4, 2, 5]
print(l1)
l1.sort()
print(l1)
l1.reverse()
print("L1=:",l1)
l2=l1
print("L2=:",l2)