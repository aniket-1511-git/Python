'''
Scenario:
Build your own pocket calculator with class-based design.

What you’ll learn:
Encapsulating operations in methods
Using OOP for real utilities

Task:
Log Session a Calculator class with methods for add, subtract, multiply, and divide.

Example:
Adding 4 and 5, then dividing 10 by 2:

Expected Output:
9
5.0
'''
class calculator:
    def __init__(self,num1,num2,sign):
        self.n1=num1
        self.n2=num2
        self.s=sign
    def operation(self):
        match self.s:
            case '+':
                print("Add: ",self.n1+self.n2)
            case '-':
                print("Diff: ",self.n1-self.n2)
            case '*':
                print("Prod: ",self.n1*self.n2)
            case '//':
                print("Quo: ",self.n1//self.n2)
            case '%':
                print("Rem: ",self.n1%self.n2)
o1= calculator(4,5,'+')
o1.operation()
o2= calculator(10,2,'//')
o2.operation()
        