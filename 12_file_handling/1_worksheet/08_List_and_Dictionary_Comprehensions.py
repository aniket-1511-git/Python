'''
Concepts: 
Using comprehensions for concise and efficient data transformations.  
Task:  
Write a script that filters out and transforms a list of log entries using list comprehensions (for instance, extracting only error messages).  
Validation: 
Confirm that the resultant list contains only the expected entries. 
'''
with open("mixed_logs.log", "r") as f:
    l = f.readlines()
msg = [line.strip().split(" ", 3)[-1] for line in l if "ERROR" in line]
for m in msg:
    print(m)
print(f"\nTotal ERROR entries found: {len(msg)}")
