'''
Scenario:
Designing a map app? You’ll want to know the area covered by a circular pond!
What you’ll learn:
Implementing methods with calculations
Understanding encapsulation
Task:
Build a Circle class with area() and perimeter() methods.
Example:
For a circle of radius 3:
Expected Output:
28.27
18.85
'''
class Circle:
    def __init__(self,r):
        self.r=r
    def circleArea(self):
        print("Area of Circle : ",f"{3.14*self.r*self.r:0.2f}")
    def circleperimeter(self):
        print("Perimeter of Circle : ",2*3.14*self.r)
o1=Circle(3)
o1.circleArea()
o1.circleperimeter()
    