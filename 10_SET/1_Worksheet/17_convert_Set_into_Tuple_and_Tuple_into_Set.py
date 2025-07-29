'''
Story: You line up your toys (tuple—order matters), then put them in a toy box (set—order doesn’t matter).
Sample Input:
toys_set = {"teddy", "robot", "ball"}
Sample Output:
("teddy", "robot", "ball")
Tip: What changes when you go from set to tuple and back?
'''
toys_set = {"teddy", "robot", "ball"}
toys_tup= tuple(toys_set)
print(toys_tup)
