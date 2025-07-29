'''
Story: You compared last week's and this week's homework lists. What's missing and what's new?
Sample Input:
old_hw = ["math", "science", "art"]
new_hw = ["math", "history", "science"]
Sample Output:
Missing: art
Additional: history
Tip: What set difference shows what you forgot?
'''
old_hw = ["math", "science", "art"]
new_hw = ["math", "history", "science"]
print("Missing:",end=" ")
for i in old_hw:
    if i not in new_hw:
        print(i)
print("Additional:",end=" ")
for i in new_hw:
    if i not in old_hw:
        print(i,end=" ")
