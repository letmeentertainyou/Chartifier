#!/bin/python3

import json 

from itertools import permutations


def eighth_note_pool(size: int=8, upper: int=4):
    pool = []
    for i in range(2, upper+1):
        pool += size // i * [i]
    return pool

# This is the actual function I want, so I need permutations not combos.
def all_unique_perms(array, size=8, upper=4):
    result = []
    for i in range(1, upper+1):
        for x in permutations(array, i):
            if sum(x) == size:
                result.append(tuple(x))
            
    return set(tuple(result))


# Go back to single json file, and max
# Load json file and if a key exists then don't render it
# Then write to a new file so we don't lose the old.
def write_strums_to_json(max=12, min=4):
    with open('../json/strumPatterns.json', 'r') as tmp:
        old = json.load(tmp)

    all_eighth_notes={}
    for x in range(min, max +1):
        if str(x) not in old:
            print(f'Finding strum patterns with {x} eighth notes.')
            pool = eighth_note_pool(size=x, upper=4)
            perms = list(all_unique_perms(pool, size=x, upper=x//2 +1))
            all_eighth_notes[x] = sorted(perms)
    
            with open(f'../json/newStrumPatterns{x}.json', 'w', encoding='utf-8') as f:
                json.dump(all_eighth_notes[x], f)

write_strums_to_json(max=20)

