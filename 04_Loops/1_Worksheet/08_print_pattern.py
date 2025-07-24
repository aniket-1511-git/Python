'''Print a hollow square pattern of size n (n ≥ 3).
Example for n = 5:
*****
*   *
*   *
*   *
*****
'''
print("Enter nu")
n=int(input())
for i in range(0,n+1):
    for j in range(0,n+1):
        if (i==0 or j==0) or (i==n or j==n):
            print("*",end="")
        
        else:
            print(end=" ")
        j+=1
    print(" ")
    i+=1
    