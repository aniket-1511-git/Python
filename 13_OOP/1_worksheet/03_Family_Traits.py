'''
Scenario:
You’re modeling a transportation system. Buses are vehicles, so shouldn’t they share common features?

What you’ll learn:
Inheriting attributes and methods from a parent class
The principle of code reuse and extension

Task:
Log Session a Vehicle class and a Bus class that inherits from it. Demonstrate shared behavior.

Example:
Suppose you make a Bus object and call its move() method.

Expected Output:
Vehicle is moving
'''
class Vehicle:
    def move():
        print('Vehicle is moving')
        
class Bus(Vehicle):
    def __init__(self):
        pass
b1=Bus
b1.move()