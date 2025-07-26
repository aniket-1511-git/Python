'''
Pad a String with Characters
Explanation: Add extra characters (like *, space, or 0) to the left or right of a string to reach a desired length.
Input: "cat", Length = 6, Pad char = "*"
Expected Output: "***cat"
'''
print("Enter string")
s=input()
print("Enter len")
l=int(input())
print("Enter pad char")
ch=input()
st=" "
st_l=len(s)
for i in range(0,l):
    if i<st_l:
        st=st+ch
    i+=1
st=st+s
print(st)