'''
Story: You turn your collection of letters into a cool code word.
Sample Input:
letters = {"A", "B", "C"}
Sample Output:
"BAC"
Tip: Set has no order—how can you make it alphabetical?
'''
letters = {"A", "B", "C"}
s=""
for i in letters:
    s=s+i
print(s)