'''
 Concepts: 
 File I/O, JSON processing, dictionary manipulation, and exception handling. 
 Description: 
 Create a script that loads a JSON configuration file, updates specific keys based on given conditions (for example, updating a version number or toggling a feature flag), and writes the modified configuration back to disk.
 Validation: 
 Test the script with a sample JSON file and ensure only the intended keys are modified while the rest of the configuration remains intact
'''
import json
def update_config(file_path, updates):
    try:
        with open(file_path, 'r') as f:
            config = json.load(f)

        for key, value in updates.items():
            if key in config:
                config[key] = value

        with open(file_path, 'w') as f:
            json.dump(config, f, indent=4)

    except Exception as e:
        print("Error:", e)
update_config('config.json', {'version': '2.0', 'feature_enabled': True})
