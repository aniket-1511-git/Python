'''
Story: You and your friend want to see if you both like any of the same cartoons.
Sample Input:
my_favs = ["Tom", "Jerry", "Ben 10"]
friend_favs = ["Powerpuff", "Jerry", "Scooby"]
Sample Output:
Yes! "Jerry" is common.
Tip: Which set operation shows what you both like?
'''
my_favs = ["Tom", "Jerry", "Ben 10"]
friend_favs = ["Powerpuff", "Jerry", "Scooby"]
for i in my_favs:
    if i in friend_favs:
        print(i,end=" ")
