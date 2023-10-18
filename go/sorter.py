#!/bin/python3

'''
Go writes JSON to a file in a weird sort order, and doesn't seem to have a 
built in sort method in general, so Python is doing the heavy lifting here.
Running this script + the go binary is faster than running rhythm.py.
'''

import json


with open(f'json/unsortedStrumPatterns.json', 'r', encoding='utf-8') as f:
    JSON = json.load(f)

# Can't sort strings so we convert the keys to ints
keys_sorted = sorted({int(key) for key in JSON.keys()})

# Now we need the keys to be strings again to get the JSON
output = {key: sorted(JSON[str(key)]) for key in keys_sorted}

with open(f'json/newStrumPatterns.json', 'w', encoding='utf-8') as f:
    json.dump(output, f)

print('JSON sorted.')