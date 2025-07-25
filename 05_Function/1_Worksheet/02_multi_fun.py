'''
Question: Write a function multiply(x, y) that returns the product of its two arguments.
Sample data:
result = multiply(4, 5)
print(result)
Expected output:
20
'''
def multiply (x:int ,y:int):
    return x*y
print("Enter data")
n1=int(input())
n2=int(input())
print("Result: ",multiply(n1,n2))
