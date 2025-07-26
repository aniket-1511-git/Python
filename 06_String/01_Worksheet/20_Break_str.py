'''
Split a String into a List of Characters
Explanation: Break the string into individual characters.
Input: "dog"
Expected Output: ['d', 'o', 'g']
'''
def breakStr(s:str):
    l=list(s)
    print(l)
    
print("Enter data")
s=input()
breakStr(s)