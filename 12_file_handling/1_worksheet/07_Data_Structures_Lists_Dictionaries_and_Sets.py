'''
  Task: 
  Concepts: Efficient use of lists, dictionaries, tuples, and sets to store and manipulate data. 
  Given a list of log lines, group them by severity (e.g., INFO, WARNING, ERROR) using a dictionary. 
  Validation: Verify that the dictionary keys and counts correctly reflect the distribution of log entries. 
  '''
from collections import defaultdict
log_dict = defaultdict(list)
with open('mixed_logs.log', 'r') as file:
    for line in file:
        parts = line.strip().split(' ', 2) 
        if len(parts) < 3:
            continue  
        _, severity, message = parts
        log_dict[severity].append(message)
for severity, messages in log_dict.items():
    print(f"{severity} ({len(messages)} entries):")
    for msg in messages:
        print(f"  - {msg}")
for severity in sorted(log_dict.keys()):
    print(f"{severity}: {len(log_dict[severity])}")
