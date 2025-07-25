'''
Question: Write a function factorial(n) that uses recursion to calculate the factorial of a number.
Sample data:
print(factorial(5))
Expected output:
120
'''
def facto(n:int):
    m=1
    for i in range(1,n+1):
        m*=i
        
    return m
print("enter number")
n=int(input())
print("Facto : ",facto(n))
        