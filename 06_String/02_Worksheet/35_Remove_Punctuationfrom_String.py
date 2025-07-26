'''
Remove Punctuation from a String
Explanation: Remove all punctuation marks, keeping only letters, digits, and spaces.
Input: "Hello, world! How are you?"
Expected Output: "Hello world How are you"
'''
def Remove_Punctuation(s:str):
    st=" "
    for i in s:
        if i>='A' and i<='Z' or i>='a' and i<='z' or i>='0' and i<='9' or i==' ':
            st=st+i
    return st
print("Enter string")
s="Hello, world! How are you?"
s=Remove_Punctuation(s)
print(s)
    