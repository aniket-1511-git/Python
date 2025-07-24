'''
Using only loops, print all prime numbers between 2 and n (n is user input).
'''
print("Enter nu")
n=int(input())
i=j=0
for i in range(2,n):
    for j in range(2,i):
        if i%j==0:
            break
        j+=1
    if i==j:
        print(i, end=" ")
    i+=1
        