'''
Your dictionary has mixed value types. Filter only the integer values into a new dictionary.
Input: d = {'x': 100, 'y': 'hello', 'z': 200}
Expected Output: {'x': 100, 'z': 200}
'''
d = {'x': 100, 'y': 'hello', 'z': 200}
l=[]
for i,v in d.items():
    if type(v) == int:
        l.append({i,v})
l=dict(l)
print(l)
