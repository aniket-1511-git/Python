'''
Question: Write a function power(base, exponent=2) that returns base raised to exponent (default is square).
Sample data:
print(power(3))
print(power(2, 5))
Expected output:
9
32
'''
def power(n:int, exp=2):
    m=1
    for i in range(0,exp):
       m*=n
    return m

print("Enter mrks")
n=int(input())
print(power(n))
print(power(2,5))

