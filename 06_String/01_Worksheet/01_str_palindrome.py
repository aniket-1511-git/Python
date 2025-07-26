'''
Check if a String is a Palindrome or Symmetrical
Explanation: A palindrome reads the same forwards and backwards (e.g., "madam"). A symmetrical string has matching halves.
Input: "madam"
Expected Output:
Palindrome: Yes
Symmetrical: Yes
'''
def isPalindrom(s:str,l:int):
    i=0
    for i in range(i<l):
        if s[i]!=s[l]:
            print("Non Palindrome")
            return
        i+=1
        l-=1
    print("Palindrome")
print("Entre string")
s=input()
l=len(s)
isPalindrom(s,l-1)



    