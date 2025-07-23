'''
Swap two variable values in one line and print the values before and after 
swapping.
'''
print("Enter two nos")
a=int(input())
b=int(input())
print("Before")
print("A = ",a," B= ",b)
a,b=b,a # swap two
print("After")
print("A = ",a," B= ",b)