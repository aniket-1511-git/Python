'''
Story: Find all words that have a, e, i, o, and u!
Sample Input:
words = ["education", "python", "sequoia"]
Sample Output:
["education", "sequoia"]
Tip: Can you check if the set of vowels is inside your word's letters?
'''
words = ["education", "python", "sequoia"]
s = set("aeiou")
l1 = []
for i in words:
    w = set(i)
    if s.issubset(w):
        l1.append(i)
print(l1)