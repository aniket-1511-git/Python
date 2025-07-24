'''
Swap Two Numbers Without Using a Third Variable
Swap two variables’ values using a single line of code.
Sample Input: a = 15, b = 8
'''
print("enter values")
a=int(input())
b=int(input())
print("Before\n","A= ",a," B= ",b)
a,b=b,a
print("After\n","A= ",a," B= ",b)