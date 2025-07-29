'''
Given a list, build a nested dictionary where each item is a deeper level (like a Russian doll).
Input: lst = ['a', 'b', 'c', 'd']
Expected Output: {'a': {'b': {'c': {'d': {}}}}}
'''
lst = ['a', 'b', 'c', 'd']
nest_dict={}
for item in reversed(lst):
    nest_dict = {item: nest_dict}
print(nest_dict)
