'''
Find all numbers less than 1000 which equal the sum of the factorials of their digits.
Valid Example: 145: 1! + 4! + 5! = 1 + 24 + 120 = 145 (valid)
Invalid Example: 123: 1! + 2! + 3! = 1 + 2 + 6 = 9 (not valid)
'''
print("Enter data")
n=int(input())
for j in range(n,0,-1):
    s=0
    t=j
    while t:
        r=t%10
        m=1
        for i in range(r,0,-1):
            m*=i
        s+=m
        t//=10
    if s==j:
        print(s,end=" ")
    
