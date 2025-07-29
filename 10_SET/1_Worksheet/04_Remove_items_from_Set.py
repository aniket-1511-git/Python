'''
Story: You want to take out an old toy from your toy box.
Sample Input:
toys = {"robot", "car", "doll"}
# remove "doll"
Sample Output:
{"robot", "car"}
Tip: What’s the difference between remove and discard if the item isn't there?
'''
toys = {"robot", "car", "doll"}
print(toys)
toys.remove("doll")
print(toys)
