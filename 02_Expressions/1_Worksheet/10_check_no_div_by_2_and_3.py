'''
Check if a Number is Divisible by Both 2 and 3
Write a single expression that evaluates to True if a number is divisible by both 2 and 3, otherwise False.
Sample Input: num = 18'''
print("enter values")
a=int(input())
if a%2==0 and a%3==0:
    print(a," is divisible by 2 and 3")
else:
    print(a," is not divisible by 2 and 3")
    
    