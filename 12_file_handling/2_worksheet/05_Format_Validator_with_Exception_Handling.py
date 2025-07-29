'''
Create a script that reads the log file and identifies lines that do not match the expected log
format. For each misformatted line, log a warning with its line number while continuing to
process the rest of the file.
Challenge: Ensure that your solution uses try-except blocks to catch and handle exceptions
without crashing.
'''
def validate_log_format(log_file_path):
    with open(log_file_path, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            try:
                parts = line.strip().split()
                if len(parts) < 5:
                    raise ValueError("Too few parts in line")
                if " - " not in line:
                    raise ValueError("Missing ' - ' separator for message")

            except Exception as e:
                print(f"[Warning] Line {line_number} malformed: {e}")
                
log_file = "data_log.txt"
print("Validating log file format...\n")
validate_log_format(log_file)
