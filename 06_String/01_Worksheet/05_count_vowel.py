'''
Count Vowels in a String Using Sets
Explanation: Find how many vowels (a, e, i, o, u) are in the string, using sets for efficiency.
Input: "education"
Expected Output: Vowels Count: 5
'''
def countVowel(s:set):
    c=0
    for i in s:
        if i=='a' or i=='e'or i=='i'or i=='o'or i=='u' or i=='A' or i=='E'or i=='I'or i=='O'or i=='U':
            c+=1
    return c
print("enter data")
s="education"
print("Vowels Count: ",countVowel(s))