'''
Question: Write a recursive function fibonacci(n) that returns the nth Fibonacci number.
Sample data:
print(fibonacci(6))
Expected output:
8
'''
def fibbo(n:int):
    s=0
    t1=0
    t2=1
    for i in range(n):
        s=t1+t2
        t1=t2
        t2=s
    return t1
print("enter num")
n=int(input())
print(fibbo(n))