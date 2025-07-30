'''
Scenario:
Log Session a birthday tracker! Determine someone’s age from their date of birth.

What you’ll learn:
Handling dates and calculating with them
Real-world use of classes

Task:
Make a Person class and compute age.

Example:
For a person born on 2000-05-25 (today is 2025-05-25):

Expected Output:
Alice is 25 years old.
'''
from datetime import date, datetime

class Person:
    def __init__(self):
        print("enter name")
        name = input()
        print("enter DOB")
        dob = input()
        self.name = name
        self.date = datetime.strptime(dob, "%Y-%m-%d").date()
    def get_age(self):
        today = date.today()
        age = today.year - self.date.year
        if (today.month, today.day) < (self.date.month, self.date.day):
            age -= 1
        return age

    def show_info(self):
        age = self.get_age()
        print(f"{self.name} is {age} years old.")

person = Person()
person.show_info()

        