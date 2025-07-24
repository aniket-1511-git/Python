'''
Evaluate a Quadratic Expression
Given values for x, a, b, and c, write an expression to compute ax² + bx + c.
Sample Input: a = 2, b = 3, c = 4, x = 5'''
print("enter values")
a=int(input())
b=int(input())
c=int(input())
x=int(input())
d=(a*(x*x))+(b*x)+c
print("d = ",d)