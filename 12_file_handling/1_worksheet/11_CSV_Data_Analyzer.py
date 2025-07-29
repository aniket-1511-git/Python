'''
Concepts: 
File I/O, data structures (lists and dictionaries), list comprehensions, and basic data analysis.
Description: 
Develop a script that reads a CSV file containing columns such as "TestCase," "Status," and "ExecutionTime." The script should produce a summary report showing counts for each status (e.g., Passed, Failed) and compute the average execution time.
Validation: 
Use a sample CSV file and compare the output summary with expected statistics.
'''
import csv
def analyze_csv(file_path):
    status_counts = {}
    total_time = 0
    count = 0
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            status = row['Status']
            time = float(row['ExecutionTime'])

            status_counts[status] = status_counts.get(status, 0) + 1
            total_time += time
            count += 1

    avg_time = total_time / count if count else 0
    return status_counts, avg_time
stats, avg = analyze_csv('test_cases.csv')
print("Status Counts:", stats)
print("Average Execution Time:", avg)
