'''
Scenario:
Imagine you’re building a drawing tool. You have a general Shape, but want to specialize it into Circle and Square.

What you’ll learn:
The basics of inheritance
How subclasses can extend or override parent class functionality

Task:
Log Session a Shape class with a method called draw(). Inherit and customize in Circle and Square.

Example:
If you create a Circle and ask it to draw():

Expected Output:

Drawing a circle
'''
class Shape:
    def draw():
        pass
        
class circle(Shape):
    def draw():
        print("Drawing a circle")
c1=circle
c1.draw()