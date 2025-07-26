'''
Explanation: Count the total characters (including spaces) in a string.
Input: "hello world"
Expected Output: Length: 11
'''
def strLen(s:str):
    l=0
    for i in s:
        l+=1
    return l
print("Enter string")
s=input()
print("Length :",strLen(s))