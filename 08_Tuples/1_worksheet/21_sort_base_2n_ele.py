'''
Description: Sort a list of (name, age) tuples by the second element (age) in ascending order.
Sorting tuples by a specific key is frequently used for ordering structured data.
Input: lst = [("Alice", 25), ("Bob", 20), ("Eve", 22)]
Output: [('Bob', 20), ('Eve', 22), ('Alice', 25)]
'''
lst = [("Alice", 25), ("Bob", 20), ("Eve", 22)]
lst=sorted(lst, key=lambda x: x[1])
print(lst)