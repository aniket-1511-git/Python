'''
Scenario:
Simulate a graphics editor: various shapes with their own formulas.

What you’ll learn:
Creating class hierarchies
Overriding methods for specialized behavior

Task:
Write a Shape base class, then subclasses for Circle, Triangle, and Square, each with its own area/perimeter.

Example:
If you create a Triangle with base 6 and height 4 and call area():

Expected Output:
12.0
'''
class shape:
    def __init__(self):
        pass
    def area():
        pass
    def perimeter():
        pass
class triangle(shape):
    def __init__(self,b,h):
        self.b=b
        self.h=h
    def area(self):
        print("area of Trinagle",(1/2)*self.b*self.h)
    def perimeter(self):
        print("perimeter of Trinagle")
t1=triangle(6,4)    
t1.area()