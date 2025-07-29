'''
Story: Give each pet a number for your pet show.
Sample Input:
pets = {"dog", "cat", "fish"}
Sample Output:
{'dog': 0, 'cat': 1, 'fish': 2}
Tip: Try using enumerate() to give each item a number.
'''
pets = {"dog", "cat", "fish"}
d1 = {pet: i for i, pet in enumerate(pets)}
print(d1)