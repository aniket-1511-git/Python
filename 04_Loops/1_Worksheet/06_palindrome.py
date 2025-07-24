'''
Check if the input number reads the same backward as forward, using only loops and arithmetic.
'''
print("Enter nu")
n=int(input())
r=0
t=n
while n>0:
    r=r*10+(n%10)
    n//=10
if t==r:
    print("Same")
else:
    print("Different")