'''
Rotate Bits Left by k Positions
Given a number (assume 8 bits) and a value k, write an expression to rotate its bits to the left by k positions.
Sample Input: n = 150, k = 2
'''
print("enter no")
a=int(input())
print("enter bit")
b=int(input())
i=0
j=7
print("a = ",bin(a))
for i in range(b):
    m=a>>i&1
    n=a>>j&1
    if n!=m:
        a^=1<<i
        a^=1<<j
    j=j-1
    i=i+1
print("a = ",bin(a))
    
    
        
