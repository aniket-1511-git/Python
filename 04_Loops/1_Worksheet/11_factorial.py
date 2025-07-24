'''
Take a number as input and calculate its factorial using loops (no recursion)
'''
print("Enter nu")
n=int(input())
f=1
for i in range(1,n+1):
    f*=i
    i+=1
print(f," is factorial of ",n)