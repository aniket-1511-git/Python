'''
Question: Write a function string_stats(s) that returns the number of vowels, consonants, and digits in the string s.
Sample data:
print(string_stats("Hello123"))
Expected output:
(2, 5, 3)
'''
def strStats(s:str):
    v=0
    c=0
    d=0
    for i in s:
        if i=='A' or i=='E'or i=='I' or i=='O' or i=='U' or i=='a' or i=='e'or i=='i' or i=='o' or i=='u':
            v+=1
        elif i>='0' and i<='9':
            d+=1
        else:
            c+=1
    
    return v,c,d