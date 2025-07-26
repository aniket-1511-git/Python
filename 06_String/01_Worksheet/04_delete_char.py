'''
Remove the i-th Character from a String
Explanation: Remove the character at a given index in a string (starting from 0).
Input: String = "Python", i = 2
Expected Output: "Pythn"
'''
print("Enter data")
s=input()
print("Enter index")
i=int(input())
s=s[:i]+s[i+1:]
print(s)