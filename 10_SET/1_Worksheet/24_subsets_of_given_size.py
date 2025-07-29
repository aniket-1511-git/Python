'''
Story: How many different teams of 3 can you make from 5 kids?
Sample Input:
kids = {"Amy", "Bob", "Cara", "Dan", "Eva"}
size = 3
Sample Output:
("Amy", "Bob", "Cara")  # one possible team
Tip: Which Python library helps you make all teams?
'''
from itertools import combinations
kids = {"Amy", "Bob", "Cara", "Dan", "Eva"}
size = 3
l1 = set(combinations(kids, size))
l1=set(l1)
print(l1)