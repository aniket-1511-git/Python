'''
Concepts: 
Handling nested dictionaries/lists, recursion or iterative approaches, and data transformation using comprehensions. 
Description: 
Create a script that accepts a nested dictionary (for example, loaded from a JSON file) and flattens it into a single-level dictionary. Use a separator (like an underscore) to concatenate nested keys into new single keys. 
Validation: 
Use a sample nested structure to verify that the output dictionary correctly maps all nested values to single-level keys. 
'''
def flatten_dict(d, parent_key='', sep='_'):
    items = {}
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.update(flatten_dict(v, new_key, sep))
        else:
            items[new_key] = v
    return items
nested = {'a': 1, 'b': {'c': 2, 'd': {'e': 3}}}
print(flatten_dict(nested))
