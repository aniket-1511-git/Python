'''
Task: Write a Python function to check if a given list is a palindrome (reads the same forwards and backwards).
Sample input: [1, 2, 3, 2, 1]
Output: True
'''
l1=[1, 2, 3, 2, 1]
l=len(l1)
i=0
l-=1
while i<l:
    if l1[i]!=l1[l]:
        break
    i+=1
    l-=1
if i==l:
    print("Palindrome")
else:
    print("Not Palindrome")
    
    