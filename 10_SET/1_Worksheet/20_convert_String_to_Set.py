'''
Story: Find all different letters in your name!
Sample Input:
myname = "samantha"
Sample Output:
{'s', 'a', 'm', 'n', 't', 'h'}
Tip: It's a fast way to spot repeated letters.
'''
print("Enter str")
s=input()
s1=set(s)
print(s1)