'''
Que:
What is the significance of the id() function when working with variables of immutable and mutable types

id() function is a built-in function that returns the identifier of an object. The identifier is an integer, The id() function is commonly used to check  two variables or objects refer to the same memory location

'''
i =10
j=20
print(id(i))  
print(id(j))

print(id(i) == id(j))
s1 = "abc"
print(id(s1))

# s2 = "def"
s2 = "abc"
print(id(s2))

print(id(s1) == id(s2))