'''
Scenario:
You’re making a geometry tool. Different shapes need to compute area, but each does it differently.
What you’ll learn:
Polymorphism: different classes, same interface
Practical OOP design patterns
Task:
Log Session a Shape base class with an area() method, then implement it differently in Circle and Square.
Example:
If you create a Square with side 4 and call area():
Expected Output:
16
'''
class Shape:
    def area():
        pass
class Square(Shape):
    def area(self,a):
        self.a=a*a
        print("Area of Square ",self.a)
o1= Square()
o1.area(4)
        

