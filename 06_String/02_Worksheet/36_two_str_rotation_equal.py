'''
Check if Two Strings are Rotationally Equivalent
Explanation: Check if one string can be rotated (circularly shifted) to match the other.
Input: "abcde", "cdeab"
Expected Output: Rotationally equivalent: Yes
'''
print("Enter str 1")
s=input()
print("Enter str 2")
t=input()
s=s+t
if s.find(t):
    print("Rotationally equivalent: Yes")
else:
    print("Rotationally equivalent: No")
    
    