'''
Append the keys and values of one dictionary to another, keeping the order. Build a bigger dictionary!
Input: d1 = {'one': 1, 'two': 2}, d2 = {'three': 3, 'four': 4}
Expected Output: {'one': 1, 'two': 2, 'three': 3, 'four': 4}
'''
d1 = {'one': 1, 'two': 2}
d2 = {'three': 3, 'four': 4}
d3=d1|d2
print(d3)