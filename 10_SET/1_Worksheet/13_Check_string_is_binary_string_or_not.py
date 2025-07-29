'''
Story: Is your note just 0s and 1s?
Sample Input:
note = "101010"
Sample Output:
Yes
Sample Input:
note = "1201"
Sample Output:
No
Tip: What does set(note) show you?'''
print("Enter str")
s=input()
s1=set(s)
c=0
for i in s1:
    if i>='2':
        c=1
        break
if c==1:
    print("No")
else:
    print("Yes")
    