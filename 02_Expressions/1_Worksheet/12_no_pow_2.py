'''
Check if a Number is a Power of Two
Write a single Boolean expression to check if a number is a power of two.
Sample Input: n = 32
'''
print("enter values")
a=int(input())
if a&(a-1)==0:
    print(a," is Power of Two ")
else:
    print(a," is not Power of Two ")
