'''Story: Collect favorite colors from all your classmates—what are all the colors?
Sample Input:
friends_colors = [
  ["red", "blue"],
  ["green", "red"],
  ["yellow", "blue"]
]
Sample Output:
{'red', 'blue', 'green', 'yellow'}
Tip: What happens if someone likes the same color twice?
'''
friends_colors = [
  ["red", "blue"],
  ["green", "red"],
  ["yellow", "blue"]
]
s1 = set()
for i in friends_colors:
    s1.update(i)
print(s1)