'''
Question: Write a function area_of_circle(radius) that returns the area (πr²) of a circle for the given radius.
Sample data:
print(area_of_circle(3))
Expected output:
28.274333882308138
'''
def area_of_circle(s:int):
    return 3.14*s*s
print("Enter radious")
r=int(input())
print(area_of_circle(r))