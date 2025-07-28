'''
Description: Given a list of pairs (tuples), separate each position into its own list (unzipping).
Unzipping is key for parallel data processing and converting between row-wise and column-wise formats.
Input: lst = [(1, 'a'), (2, 'b'), (3, 'c')]
Output: 
[1, 2, 3]
['a', 'b', 'c']
'''
l1 = [(1, 'a'), (2, 'b'), (3, 'c')]
int_l=[]
char_l=[]
for i in l1:
   i,c=i
   int_l.append(i)
   char_l.append(c)
print(int_l)
print(char_l)
            

