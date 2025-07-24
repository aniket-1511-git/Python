'''
Toggle a Specific Bit in an Integer
Given a number and a bit position, write an expression to toggle (flip) that bit.
Sample Input: n = 12, bit_position = 2
'''
print("enter no")
a=int(input())
print("enter bit")
b=int(input())
a^=1<<b
print(a)