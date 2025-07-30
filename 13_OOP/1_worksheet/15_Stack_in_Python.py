'''
Scenario:
Log Session a feature like "undo" in a drawing app.

What you’ll learn:
How to build a stack (LIFO) using classes
Using lists for stack operations

Task:
Implement a Stack class with push and pop methods.

Example:
Push 10, then 20; pop an element.

Expected Output:
20
'''
class stack:
    l=[]
    def __init__(self):
        pass
    def push(self):
        print("enter data")
        num=int(input())
        self.l.append(num)
    def pop(self):
        self.l.pop(0)
    def printStack(self):
        print(self.l,end=" ")
s1=stack()
while 1:
    print("1.insert 2.Pop 3.print ")
    op=int(input())
    match op:
        case 1:
            s1.push()
        case 2:
            s1.pop()
        case 3:
            s1.printStack()
            



    
        
