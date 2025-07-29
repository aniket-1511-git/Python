'''
You’re managing the stock system for a small supermarket. Each item is a key, and its count is the value. A frantic customer wants to know if “apples” are still available. How will you instantly check if “apples” are on your shelf?
Input: stock = {'apples': 14, 'bananas': 22, 'rice': 12}, query = 'apples'
Expected Output: Yes, apples are in stock!
'''
stock = {'apples': 14, 'bananas': 22, 'rice': 12}
p= stock.get('apples')
if p== None:
    print(" No ")
else:
    print(" Yes ")