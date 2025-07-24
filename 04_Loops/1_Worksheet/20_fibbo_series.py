'''
input n and print the nth Fibonacci number using only variable updates and a loop (no lists, no recursion).
'''
print("Enter nu")
n=int(input())
s=0
t1=0
t2=1
for i in range(0,n+1):
    print(t1,end=" ")
    s=t1+t2
    t1=t2
    t2=s