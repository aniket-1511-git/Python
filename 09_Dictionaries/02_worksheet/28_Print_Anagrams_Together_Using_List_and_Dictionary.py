'''Group words that are anagrams together from a list (all the jumbled twins in one basket).
Input: words = ['listen', 'silent', 'enlist', 'hello', 'ohlle']
Expected Output: [['listen', 'silent', 'enlist'], ['hello', 'ohlle']]'''
from collections import defaultdict
words = ['listen', 'silent', 'enlist', 'hello', 'ohlle']
l = defaultdict(list)
for i in words:
    key = ''.join(sorted(i))
    l[key].append(i)
    
