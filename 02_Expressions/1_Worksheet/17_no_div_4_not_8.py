'''
Check If a Number is a Multiple of 4 but Not of 8
Write an expression that is True only if a number is divisible by 4 but not by 8.
Sample Input: n = 12
'''
print("enter no")
a=int(input())
if a%4==0 and a%8!=0:
    print(a,"is Multiple of 4 but Not of 8")