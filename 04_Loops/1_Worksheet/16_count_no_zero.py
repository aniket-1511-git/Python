'''
Input an integer and count how many times 0 appears in it (no strings or lists).'''
print("Enter nu")
n=int(input())
r=0
while n>0:
    if (n%10)==0:
        r+=1
    n//=10
print("no of zero:",r)