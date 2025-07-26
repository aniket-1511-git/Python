'''
Print the Middle Character of a String
Explanation: Display the character(s) at the center of the string.
Input: "python"
Expected Output: Middle character: 't' and 'h'
'''
def print_midChar(s:str):
    l=len(s)
    if l%2==0:
        print(s[int(l/2)-1]," ",s[int(l/2)])
    else:
        print(s[int(l/2)])
print("Enter string")
s=input()
print_midChar(s)

        