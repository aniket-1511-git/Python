'''
You have a dictionary of spells, but some spells are now forbidden. Given a list of banned spell names, wipe them from your magic book!
Input: spells = {'fireball': 5, 'healing': 10, 'curse': 2}, banned = ['curse', 'fireball']
Expected Output: {'healing': 10}
'''
spells = {'fireball': 5, 'healing': 10, 'curse': 2}
banned = ['curse', 'fireball']
for i in banned:
    if i in spells:
        del spells[i]
print(spells)
