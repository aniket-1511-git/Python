'''
Check if a given number is a perfect number (sum of divisors excluding itself), using only loops.
'''
print("Enter nu")
n=int(input())
s=0
for i in range(1,n):
    if n%i==0:
        s+=i
if s==n:
    print("Perfect no ")
else:
    print("not Perfect no ")
    
