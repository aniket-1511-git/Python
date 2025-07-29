'''
Write a script that converts the log file into a JSON file. Each log entry should be a JSON
object containing the keys: timestamp, log_level, module, and message.
Challenge: Ensure that the JSON output correctly represents all valid log entries while
ignoring or flagging misformatted lines.
'''

import json

def parse_log_line(line):
    """Parse a single log line into a dictionary or return None if malformed."""
    try:
        parts = line.strip().split()
        if len(parts) < 5:
            return None
        timestamp = f"{parts[0]} {parts[1]}"
        log_level = parts[2]
        module = parts[3]

        dash_index = line.find(" - ")
        if dash_index == -1:
            return None
        message = line[dash_index + 3:].strip()

        return {
            "timestamp": timestamp,
            "log_level": log_level,
            "module": module,
            "message": message
        }
    except Exception:
        return None
    
def convert_log_to_json(log_file_path, output_file_path):
    entries = []

    with open(log_file_path, 'r') as infile:
        for line_number, line in enumerate(infile, start=1):
            parsed = parse_log_line(line)
            if parsed:
                entries.append(parsed)
            else:
                print(f" {line_number}")

    with open(output_file_path, 'w') as outfile:
        json.dump(entries, outfile, indent=2)

    print(f"{output_file_path}")


log_file = "data_log.txt"
json_output = "logs_output.json"
convert_log_to_json(log_file, json_output)
