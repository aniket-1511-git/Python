'''
Using the output from Question 3, write a function that groups log entries by their module.
For each module, output the count of log entries.
Challenge: Use dictionary comprehensions or iterative methods to build the grouped result.

'''
# 04_Group_Logs_by_Module.py

from collections import defaultdict
def parse_log_file_to_dicts(log_file_path):
    parsed_logs = []

    with open(log_file_path, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            try:
                parts = line.strip().split()

                if len(parts) < 5:
                    raise ValueError("Too few parts")

                timestamp = f"{parts[0]} {parts[1]}"
                log_level = parts[2]
                module = parts[3]

                # Join everything after the dash
                dash_index = line.find(" - ")
                if dash_index == -1:
                    raise ValueError("Missing dash separator")

                message = line[dash_index + 3:].strip()

                entry = {
                    "timestamp": timestamp,
                    "log_level": log_level,
                    "module": module,
                    "message": message
                }
                parsed_logs.append(entry)

            except Exception as e:
                print(f"[Warning] Line {line_number} skipped: {e}")

    return parsed_logs

def group_logs_by_module(log_file_path):
    logs = parse_log_file_to_dicts(log_file_path)
    module_counts = defaultdict(int)

    for entry in logs:
        module = entry.get("module", "Unknown")
        module_counts[module] += 1

    return dict(module_counts)

log_file = "data_log.txt"
grouped = group_logs_by_module(log_file)
print("\nLog Count by Module:")
for module, count in grouped.items():
    print(f"{module}: {count}")
