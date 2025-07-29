'''
Story: Does your word have only different letters, no repeats?
Sample Input:
word = "lamp"
Sample Output:
Yes
Sample Input:
word = "hello"
Sample Output:
No
Tip: Compare len(set(word)) and len(word).
'''
print("Enter str")
s=input()
if len(set(s)) == len(s):
    print("Yes")
else:
    print("No")
    