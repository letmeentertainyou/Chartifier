#!/bin/python3

from itertools import permutations
from json import dump
from random import choice


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
def write_strums_to_json(max=12, min=4):

    all_eighth_notes={}
    for x in range(min, max +1):
      
        print(f'Finding strum patterns with {x} eighth notes.')
        pool = eighth_note_pool(size=x, upper=4)
        perms = list(all_unique_perms(pool, size=x, upper=x//2 +1))
        all_eighth_notes[x] = sorted(perms)
    name = f'../json/strumPatterns.json'
    with open(name, 'w', encoding='utf-8') as f:
        dump(all_eighth_notes, f)

write_strums_to_json(max=16)

