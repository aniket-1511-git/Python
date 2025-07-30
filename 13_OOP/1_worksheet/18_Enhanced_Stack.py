'''
Scenario:
See the current state of the stack—great for debugging.
What you’ll learn:
Extending existing classes
Useful methods for state visibility
Task:
Add a display method to your Stack class to show its elements.
Example:
Push 1, then 2; display stack.
Expected Output:
[1, 2]
'''
class stack:
    l=[]
    def __init__(self):
        pass
    def push(self):
        print("enter data")
        num=int(input())
        self.l.append(num)
    def printStack(self):
        print(self.l)
        
s1=stack()
while 1:
    print("1.push 2.print ")
    op=int(input())
    match op:
        case 1:
            s1.push()
        case 2:
            s1.printStack()