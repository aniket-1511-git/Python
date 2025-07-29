'''
Using basic string manipulation (without regex), write a script that filters and prints all log
entries containing the word “ERROR”.
Challenge: Verify that only well-formed error lines are extracted while ignoring
misformatted lines.
'''
def extract_error_logs(log_file_path):
    with open(log_file_path, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            parts = line.strip().split()
            if len(parts) >= 4 and parts[2] == "ERROR":
                print(line.strip())
            else:  
                continue

log_file = "data_log.txt"  
extract_error_logs(log_file)
