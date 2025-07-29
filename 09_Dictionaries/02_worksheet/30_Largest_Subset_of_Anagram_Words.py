'''
Given a list of words, find the size of the largest subset where all are anagrams of each other.
Input: words = ['bat', 'tab', 'eat', 'tea', 'tan', 'nat']
Expected Output: 3
'''
words = ['bat', 'tab', 'eat', 'tea', 'tan', 'nat']
d1 = {}
for word in words:
    key = ''.join(sorted(word))
    d1.get(key, 0) + 1
c=max(d1.values())
print(c)