'''
Concepts: 
File I/O, directory traversal (using modules such as os or glob), string manipulation, and aggregation using dictionaries. 
Description: 
Write a script that scans a specified directory for all .log files, processes each file, and aggregates counts of different log levels (e.g., INFO, WARNING, ERROR) into a single summary dictionary. 
Validation: 
Place several sample log files in a test directory and verify that the aggregated counts correctly reflect the combined data from all files.
'''
import os
import re
def aggregate_logs(directory):
    log_counts = {'INFO': 0, 'WARNING': 0, 'ERROR': 0}
    for filename in os.listdir(directory):
        if filename.endswith('.log'):
            with open(os.path.join(directory, filename), 'r') as f:
                for line in f:
                    for level in log_counts:
                        if level in line:
                            log_counts[level] += 1
    return log_counts
counts = aggregate_logs('logs/')
print("Aggregated Log Counts:", counts)
