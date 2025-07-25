'''
Question: Write a function calculate(a, b) that returns both the sum and difference of a and b.
Sample data:
s, d = calculate(10, 3)
print("Sum:", s)
print("Difference:", d)
Expected output:
Sum: 13
Difference: 7
'''
def calculate(a:int, b:int):
    sum = a+b
    diff= a-b
    return sum, abs(diff)
print("enter num1")
a=int(input())
print("enter num2")
b=int(input())
s , d = calculate(a,b)
print("Sum = ",s)
print("Difference = ",d)