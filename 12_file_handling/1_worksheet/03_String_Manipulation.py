'''
Concepts: String methods, slicing, formatting, and parsing. 
Task: • Develop a script that processes log entries by extracting the timestamp, severity, and message from each line. 
• Validation: Ensure that the parsed elements match the expected values for sample log entries.
'''
   
import re
with open('applicaiton_logs.txt', 'r') as fs:
    l = fs.readlines()
p = r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}) ([A-Z]+) .* - (.*)"
for i in l:
    i = i.strip()  
    match = re.match(p, i)
    if match:
        t = match.group(1)
        s= match.group(2)
        m = match.group(3)
        print("Timestamp:", t, "Severity:", s, "Message:", m)
    else:
        print("Err: Could not parse line ->", i)


