'''
Concepts: 
File I/O, CSV and JSON modules, data transformation, and list comprehensions. 
Description: 
Develop a script that reads data from a CSV file and converts each row into a JSON object. The final output should be a JSON file containing an array of these objects. 
Validation: 
Provide a sample CSV file and confirm that the output JSON file accurately represents the CSV content structure.
'''
import csv
import json
def csv_to_json(csv_file, json_file):
    with open(csv_file, newline='') as f:
        reader = csv.DictReader(f)
        data = list(reader)

    with open(json_file, 'w') as f:
        json.dump(data, f, indent=4)

csv_to_json('data.csv', 'output.json')
