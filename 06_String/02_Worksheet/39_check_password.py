'''
Validate a Password String
Explanation: Check if a password meets certain conditions (length, special characters, etc.).
Input: "MyPass123@"
Expected Output: Valid password: Yes
'''
print("Enter pass")
s=input()
cap=0
small=0
spl=0
dig=0
for i in s:
    if i>='A' and i<='Z' or i>='a' and i<='z' or i>='0' and i<='9' or i==' ':
        cap=1
        small=1
        dig=1
    else:
        spl=1
if spl and dig and cap and small:
    print("Valid password: Yes")
else:
    print("Valid password: No")

    
         