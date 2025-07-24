'''
Print all 4-digit numbers where the product of the first two digits equals the product of the last two digits.
Valid Example: 1441 → (1 × 4) == (4 × 1) → 4 == 4 (valid)
Invalid Example: 2356 → (2 × 3) == (5 × 6) → 6 == 30 (not valid)
'''
print("Enter data")
n=int(input())
p1=1
p2=1
r=0
for i in range(0,2):
    p1*=n%10
    n//=10
while n:
   r=r*10+n%10
   n//=10
for i in range(0,2):
    p2=p2*r%10
    r//=10
if p1==p2:
    print(p1,"Valid")