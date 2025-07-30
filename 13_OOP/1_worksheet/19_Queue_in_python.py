'''
Scenario:
Manage waiting lines—like people in a ticket queue.

What you’ll learn:
Implementing a queue (FIFO) in Python
Real-world queue management

Task:
Build a Queue class with enqueue and dequeue methods.

Example:
Enqueue 10, then 20; dequeue once.

Expected Output:

10
'''
class queue:
    l=[]
    def __init__(self):
        pass
    def enqueue(self):
        print("enter data")
        num=int(input())
        self.l.insert(0,num)
    def dequeue(self):
        self.l.pop()
    def printQue(self):
        print(self.l)
s1=queue()
while 1:
    print("1.enqueue 2.dequeue 3.print ")
    op=int(input())
    match op:
        case 1:
            s1.enqueue()
        case 2:
            s1.dequeue()
        case 3:
            s1.printQue()