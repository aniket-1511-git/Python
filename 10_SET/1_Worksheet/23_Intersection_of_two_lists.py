'''
Story: Which stickers do you and your friend both have?
Sample Input:
mine = ["dino", "star", "moon"]
yours = ["star", "rocket", "moon"]
Sample Output:
{"star", "moon"}
Tip: How is this different if you use a list instead of a set?
'''
mine = ["dino", "star", "moon"]
yours = ["star", "rocket", "moon"]
s1=set(mine)& set(yours)
print(s1)
