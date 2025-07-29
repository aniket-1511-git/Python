'''
You intercepted a list of coded messages (keys), but your team uses new code names (a mapping). How will you quickly rename every code to its new secret label?
Input: codes = {'alpha': 'ok', 'beta': 'wait'}, new_labels = {'alpha': 'red', 'beta': 'blue'}
Expected Output: {'red': 'ok', 'blue': 'wait'}
'''
codes = {'alpha': 'ok', 'beta': 'wait'}
new_labels = {'alpha': 'red', 'beta': 'blue'}
l1=[]
l2=[]
for i in codes:
    l1.append(codes[i])
for i in new_labels:
    l2.append(new_labels[i])
final_dict=dict(zip(l1,l2))
print(final_dict)


