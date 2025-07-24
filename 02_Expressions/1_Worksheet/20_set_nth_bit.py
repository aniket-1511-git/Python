'''
Set the nth Bit of a Number
Write an expression that sets the nth bit of a given integer to 1 (leave other bits unchanged).
Sample Input: n = 9, bit_position = 3
'''
print("enter no")
a=int(input())
print("enter bit")
b=int(input())
a|=1<<b
print(a)