'''
Check if a String Contains Special Characters
Explanation: Check if the string contains characters other than letters or numbers.
Input: "Hello@123"
Expected Output: Contains special character: Yes
'''
def find_spl(s:str):
    l=len(s)
    for i in range( l+1):
        if (s[i]>='0'and s[i]<='9') or (s[i]>='A'and s[i]<='Z') or (s[i]>='a' and s[i]<='z'):
            i+=1
        else:
            return "Yes"
print("Enter string")
s=input()
print(find_spl(s))