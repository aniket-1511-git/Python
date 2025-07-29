'''
Remove all keys from the dictionary that contain a certain substring (like a keyword filter).
Input: d = {'sun': 1, 'sunny': 2, 'rain': 3}, substring = 'sun'
Expected Output: {'rain': 3}
'''
d = {'sun': 1, 'sunny': 2, 'rain': 3}
substring = 'sun'
d1 = {k: v for k, v in d.items() if substring not in k}
print(d1)