'''
Scenario:
You’re building a plugin system and want to know if a new class is a valid type of plugin.
What you’ll learn:
The use of issubclass()
Class relationships in Python

Task:
Check if Bus is a subclass of Vehicle.

Example:
You use issubclass() with Bus and Vehicle.

Expected Output:
True
'''
class Vehicle:
    pass
class Bus(Vehicle):
    pass

print(issubclass(Bus,Vehicle))