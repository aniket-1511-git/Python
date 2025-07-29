'''
Write a script that reads the provided log file and counts the number of occurrences of each
log level (INFO, DEBUG, WARNING, ERROR) using file I/O and dictionaries. Avoid using
regular expressions for this task.
Challenge: Ensure your code gracefully handles lines that do not follow the expected
format.
'''
def count_log_levels(log_file_path):
    log_counts = {"INFO": 0, "DEBUG": 0, "WARNING": 0, "ERROR": 0}
    with open(log_file_path, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            parts = line.strip().split()
            if len(parts) >= 3:
                log_level = parts[2]
                if log_level in log_counts:
                    log_counts[log_level] += 1
                else:
                    print(f"[Warning] Unknown log level at line {line_number}: '{log_level}'")
            else:
                print(f"[Warning] Malformed line at {line_number}: '{line.strip()}'")

    return log_counts

log_file = "data_log.txt"  
counts = count_log_levels(log_file)
for level, count in counts.items():
    print(f"{level}: {count}")
