'''
Concepts:
Advanced string manipulation, regular expressions, file I/O, and dictionary usage.
Description:
Write a script that reads a log file and filters entries based on custom criteria—such as logs within a specific time range or containing a particular keyword pattern. Employ regex to accurately extract and process these elements. 
Validation:
Run the script on sample log data and confirm that the filtered output matches the specified criteria.
'''
import re
from datetime import datetime
def filter_logs(log_file, keyword=None, time_range=None):
    pattern = r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (INFO|ERROR|WARNING) (.+)"
    results = []
    with open(log_file, 'r') as f:
        for line in f:
            match = re.match(pattern, line)
            if match:
                timestamp, level, message = match.groups()
                if keyword and keyword not in message:
                    continue
                if time_range:
                    log_time = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')
                    if not (time_range[0] <= log_time <= time_range[1]):
                        continue
                results.append(line.strip())
    return results
from datetime import datetime
filtered = filter_logs('app.log', keyword='disk', time_range=(datetime(2024,1,1), datetime(2025,1,1)))
print("\n".join(filtered))
