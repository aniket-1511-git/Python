'''
Question: Write a recursive function reverse_string(s) that returns the reversed string.
Sample data:
print(reverse_string("python"))
Expected output:
nohtyp
'''
def strRev(s:str):
    return s[::-1]
print("Enter data")
s=input()
print(s)
s=strRev(s)
print(s)