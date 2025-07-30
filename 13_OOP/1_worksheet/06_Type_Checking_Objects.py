'''Scenario:
You’re building a dynamic form. You need to know if a user input is a string, number, or something else.

What you’ll learn:
How to use type() and why it’s useful
Avoiding type errors in your code

Task:
Check and print the type of various objects.

Example:
You create an integer and a string and check their types.

Expected Output:
<class 'int'>
<class 'str'>
'''
class generic:
    def __init__(self,data):
        self.d=data
o1=generic(123)
print(type(o1.d))
o2=generic("123")
print(type(o2.d))
