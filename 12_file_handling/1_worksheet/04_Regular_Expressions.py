'''
Concepts: Pattern matching using Python’s re module for search, match, and substitution tasks. 
Task: 
Write a function to extract email addresses or specific patterns from a block of text using regular expressions. 
Validation: 
Provide several test cases to confirm that the function correctly identifies or rejects entries.'''
import re
def file_regEx(file_name:str):
    p = r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}) "
    with open(file_name, 'r') as fs:
        l = fs.readlines()
    for i in l:
        i = i.strip()  
        m = re.match(p, i)
        if m:
            t = m.group(1)
            print(t)
print("Enter file_name")
s=input()
file_regEx(s)
