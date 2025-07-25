'''
Question: Write a recursive function flatten_dict(d, parent_key='', sep='_') that takes a nested dictionary and flattens it, so that the result is a single-level dictionary with keys as the path joined by sep.
Sample data:
flatten_dict({'a': 1, 'b': {'c': 2, 'd': {'e': 3}}})
Expected output:
{'a': 1, 'b_c': 2, 'b_d_e': 3}
'''