'''
Story: What games do you want to play this week that you didn't play last week?
Sample Input:
last_week = ["hide", "seek", "tag"]
this_week = ["hide", "seek", "jump", "run"]
Sample Output:
["jump", "run"]
Tip: Use set subtraction: A - B!
'''
last_week = ["hide", "seek", "tag"]
this_week = ["hide", "seek", "jump", "run"]
l1=list(set(this_week)-set(last_week))
print(l1)