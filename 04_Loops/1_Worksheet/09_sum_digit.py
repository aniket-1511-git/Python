'''
Take an integer and, using only loops, sum its digits repeatedly until only a single digit remains.
Example: 9875 → 9+8+7+5=29 → 2+9=11 → 1+1=2
'''
print("Enter nu")
n=int(input())
s=0
while n>0 or s>9:
    if n==0:
        n=s
        s=0
    s+=n%10
    n//=10
print(s)