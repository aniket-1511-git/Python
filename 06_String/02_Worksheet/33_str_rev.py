'''
Mirror Image of a String
Explanation: Reverse the string as if viewing in a mirror.
Input: "abcd"
Expected Output: "dcba"
'''
print("Enter string")
s=input()
r=" "
for i in s:
    r=i+r
s=r
print(s)