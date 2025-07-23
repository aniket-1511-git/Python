'''
que: 
Describe the difference between is and == when comparing variables. Provide an example where they behave differently.
'''
'''
ans:
In Python, is and == are both comparison operators
Equality Operator ( == )
1.Compares the values of two objects.
2.Returns True if the objects have the same content or value, even if they are stored in different memory locations
'''
i=10
j=10
print(i==j)
'''
Identity Operator (is):

1. it checks if two variables refer to the exact same object in memory.
2.Returns True if both variables point to the same memory address.
'''
a=[10,20,30]
b=[10,20,30]
c=a
print(a is b)
print(a is c)