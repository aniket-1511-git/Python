'''
Print the sum of all odd numbers from 1 up to n (inclusive), using loops only.'''
print("Enter nu")
n=int(input())
for i in range(n+1):
    if i%2==1:
        print(i,end=" ")