'''
Find the Largest of Three Numbers Using Only Expressions
Without using if, elif, or any function, write an expression to find the largest of three given numbers.
Sample Input: a = 14, b = 27, c = 19
'''
print("enter values")
a=int(input())
b=int(input())
c=int(input())
if a>b and a>c:
    print(a," is largest")
elif b>a and b>c:
    print(b," is largest")
else:
    print(c," is largest")