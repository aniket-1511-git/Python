'''
For a given number of rows, print the following number pyramid pattern
1
1 2
1 2 3
...
1 2 ... n
'''
print("Enter nu")
n=int(input())
for i in range(1,n+1):
    
    for j in range(1,i+1):
        print(j,end=" ")
    print("")