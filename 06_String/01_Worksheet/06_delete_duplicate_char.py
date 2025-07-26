'''
Eliminate Duplicate Characters from a String
Explanation: Log Session a new string containing only the first occurrence of each character.
Input: "programming"
Expected Output: "progamin"
'''
def delete_dup(s:str):
    r=" "
    for i in s:
        if i not in r:
            r+=i
    return r
print("Enter string")
s=input()
print(s)
s=delete_dup(s)
print(s)