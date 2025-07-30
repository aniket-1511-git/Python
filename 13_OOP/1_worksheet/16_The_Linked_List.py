'''
Scenario:
Store and process data efficiently, like songs in a playlist.

What you’ll learn:
Building a linked list from scratch
Understanding nodes and pointers

Task:
Write a LinkedList class with insert, delete, and display.

Example:
Add 10, then 20, and display list.

Expected Output:
10 -> 20
'''
class Node:
    def __init__(self, data):
        self.d = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self):
        print("data enter")
        d=int(input())
        new_node = Node(d)
        if self.head is None: 
            self.head = new_node
        else:
            p = self.head
            while p.next: 
                p = p.next
            p.next = new_node
    def display(self):
     
        p = self.head
        while p:
            print(p.d,'->',end="")
            p = p.next
        print(" ")

ll = LinkedList()
while 1:
    print("1.insert 2.print , 3. exit")
    op=int(input())
    match op:
        case 1:
            ll.insert()
        case 2:
            ll.display()
        case 3:
            break        
