'''
Using only loops and arithmetic, compute the sum of all numbers below 1000 that are multiples of 3 or 5.
'''
print("Enter nu")
n=int(input())
s=0
for i in range(1,n+1):
    if i%3==0 or i%5==0:
        s+=i
print("sum = ",s)