'''
You know a value, but not which key owns it. Trace back and report the key for a given value!
Input: d = {'x': 100, 'y': 200}, value = 200
Expected Output: Key for value 200: 'y'
'''
d = {'x': 100, 'y': 200}
value = 200
for k,i in d.items():
    if i == value:
        print(k)
        

