'''
Every order is tracked in a list. Can you build a menu board that shows how many times each item was ordered today?
Input: orders = ['latte', 'espresso', 'latte', 'tea', 'espresso', 'latte']
Expected Output: {'latte': 3, 'espresso': 2, 'tea': 1}
'''
orders = ['latte', 'espresso', 'latte', 'tea', 'espresso', 'latte']
l1=[]
l2=[]
for i in orders:
    c=orders.count(i)
    if i not in l1:
      l1.append(i)  
      l2.append(c)  
d = dict(zip(l1,l2))
print(d)

      
