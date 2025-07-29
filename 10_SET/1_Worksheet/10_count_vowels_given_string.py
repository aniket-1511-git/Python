'''
Story: You want to count the vowels in your secret code message.
Sample Input:
msg = "hello world"
Sample Output:
3
Tip: Vowels can be put in a set for quick checking!
'''
msg = "hello world"
s=set(msg)
print(s)
c=0
for i in s:
    if i=='A' or i=='E'or i=='I'or i=='U'or i=='O'or i=='a' or i=='e'or i=='i'or i=='u'or i=='o':
        c+=1
print(c)