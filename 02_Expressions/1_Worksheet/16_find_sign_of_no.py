'''
Find the Sign of a Number as -1, 0, or 1 (Using Only Expressions)
Write a single expression that gives -1 for negative numbers, 0 for zero, and 1 for positive numbers.
Sample Input: n = -56
'''
print("enter no")
a=int(input())
d=-1 if a<0 else 0 if a==0 else 1
print(d)