'''
Take an error code (integer). Print "Critical" if code ≥1000, "Warning" if 100–999, and "Info" if <100.
Input: 230
Output: Warning
'''
print("Enter voltage")
err_code=int(input())
if err_code>=1000:
    print("Critical")
elif err_code>=100:
    print("Warning")
else :
    print("Info")
   