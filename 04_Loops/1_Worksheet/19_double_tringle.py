'''
For n rows, print the following double triangle pattern:
*
**
***
**
*
'''
print("Enter nu")
n=int(input())
for i in range(0,n+1):
    for j in range(0,i+1):
        print("*",end=" ")
    print("")
for i in range(0,n+1):
    
    for j in range(0,n-i):
        print("*",end=" ")
    print("")