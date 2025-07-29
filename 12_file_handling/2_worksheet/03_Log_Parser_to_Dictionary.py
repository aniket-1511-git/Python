'''
Develop a function that reads each line of the log file and parses it into a dictionary with
keys: timestamp, log_level, module (if available), and message. Return a list of
such dictionaries.
Challenge: Handle lines that deviate from the standard format by either skipping them or
recording an error message.
'''
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
log_file = "data_log.txt"
logs = parse_log_file_to_dicts(log_file)

print("\nParsed Log Entries:")
for entry in logs:
    print(entry)
