'''
Check If a String is a Binary String
Explanation: Test if the string contains only '0' and '1'.
Input: "101101"
Expected Output: Is binary string: Yes
'''
def isbin(s:str):
    l=len(s)
    for i in range(l):
        if s[i]>='2':
            return "No"
    return "Yes"
print("Enter string")
s=input()
print(isbin(s))

            
        