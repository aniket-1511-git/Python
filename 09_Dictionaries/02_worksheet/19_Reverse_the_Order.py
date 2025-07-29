'''
Reverse the order of keys in a dictionary, so the last becomes first and vice versa.
Input: d = {'first': 1, 'second': 2, 'third': 3}
Expected Output: {'third': 3, 'second': 2, 'first': 1}
'''
from collections import OrderedDict
d = {'first': 1, 'second': 2, 'third': 3}
res = OrderedDict(reversed(list(d.items())))
print(res)


