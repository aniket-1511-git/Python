'''
Copying dictionaries is critical when you need to manipulate data without affecting the original.
Make a shallow copy of d = {'p': 2, 'q': 3} and print the copy.
Show what happens when you do b = a with a = {'x': [1, 2]} and then modify b['x']. What happens to a?
Log Session a copy of original = {'car': 'red', 'bike': 'blue'}. Change the 'car' in the copy to 'green' and print both dictionaries.
Expected Output: Original remains unchanged.
Explain (with code) the difference between a shallow copy and a deep copy using a nested dictionary. Show the effect of changing an inner list.
'''
import copy
d = {'p': 2, 'q': 3}
shallow_d= copy.copy(d)
print("d: ",d)
print("shallow_d: ",shallow_d)
a = {'x': [1, 2]}
b = a
print("A:",a)
b['x']=[4,5]
print("B:",b)
o1 = {'car': 'red', 'bike': 'blue'}
o2 = copy.copy(o1)
o2['car']='green'
print("o1: ",o1)
print("o2: ",o2)
