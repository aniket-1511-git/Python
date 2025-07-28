''''
Description: Convert a tuple of positive integers into a single integer by concatenating their values.
This is a common data transformation task, often seen in problems that require generating a unique number from a sequence.
Input: t = (1, 2, 3)
Output: 123
'''
t = (1, 2, 3)
n=0
m=1
for i in t:
    n=n*10+i
print(n)