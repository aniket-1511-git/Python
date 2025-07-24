'''
Enter two analog readings. Print "Match" if they are within 5 units of each other, "No Match" otherwise.
Input: 98, 101
Output: Match
'''
print("Enter no1")
a=int(input())
print("Enter no2")
b=int(input())

if abs(a-b)<=5:
    print("Match")
else:
    print("No Match")
    
    