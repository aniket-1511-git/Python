'''
13. Substring Key Find
Given a search term, find out which keys in your dictionary contain it. Useful for partial name search!
Input: d = {'hello': 1, 'world': 2, 'hell': 3}, substring = 'hell'
Expected Output: Keys containing 'hell': ['hello', 'hell']
'''
d = {'hello': 1, 'world': 2, 'hell': 3}
substring = 'hell'
l1=[]
for i in d:
    if i.find(substring) !=-1:
        l1.append(i)
print(l1)
