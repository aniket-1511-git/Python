'''
Given a list and a dictionary, extract values for all keys that appear in both.
Input: d = {'a': 100, 'b': 200, 'c': 300}, lst = ['b', 'c', 'd']
Expected Output: {'b': 200, 'c': 300}
'''
d = {'a': 100, 'b': 200, 'c': 300}
lst = ['b', 'c', 'd']
for i in lst:
    if i in d:
        print(i," ",d[i])