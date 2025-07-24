'''
Print all 3-digit numbers such that the sum of the cubes of their digits equals the number itself.
Example: 153 → 1³ + 5³ + 3³ = 153
'''
i=100
while i<=999:
    t=i
    c=0
    m=1
    while t>0:
        c+=1
        t//=10
    t=i
    sum=0
    while t>0:
        r=t%10
        j=0
        m=1
        while j<c:
            m*=r 
            j+=1
        sum=sum+int(m)
        t//=10
    if sum==i:
        print(sum, end=" ")
    
    i=i+1
    
