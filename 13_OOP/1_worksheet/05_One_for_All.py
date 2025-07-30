'''The Magic of Class Attributes
Scenario:
All students in a school belong to the same institution. How can you ensure this is reflected in every student object?

What you’ll learn:
Class (static) attributes: properties shared by all instances
When and why to use them

Task:
Define a Student class where every student has the same school_name.

Example:
If you create two students and print their school_name:

Expected Output:
Central High School Central High School'''
class Student :
    def __init__(self,sName):
        self.sc_name=sName
        
    def school_name(self):
        print(self.sc_name)
s1= Student('Central High School')
s1.school_name()
s2= Student('Central High School')
s2.school_name()
        