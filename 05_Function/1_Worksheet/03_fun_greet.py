'''
Question: Write a function greet_person(name, greeting) that prints a personalized message like "Hello, John!" using the arguments.
Sample data:
greet_person("John", "Hi")
Expected output:
Hi, John!
'''
def greet_person(name:str,msg:str):
    print(name,msg)
print("Enter name")
name=input()
print("Enter Message")
msg=input()
greet_person(name,msg)
