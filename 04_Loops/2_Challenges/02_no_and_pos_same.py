'''
For n between 100 and 999, print all numbers where the sum of their digits raised to their own position is equal to the number.
Valid Example: 135: 1¹ + 3² + 5³ = 1 + 9 + 125 = 135 (valid)
Invalid Example: 123: 1¹ + 2² + 3³ = 1 + 4 + 27 = 32 (not valid)
'''
print("Enter data")
n1=int(input())
n2=int(input())
for i in range(n1,n2):
    c=0
    s=0
    t=i
    while t:
        c+=1
        t//=10
    t=i
    while t:
        r= t%10
        m=1
        for j in range(0,c):
            m*=r 
        c-=1
        s+=m
        t//=10
    if i==s:
        print(i)
        
        
    