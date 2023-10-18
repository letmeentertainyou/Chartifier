#!/bin/python3
'''
This change was particularly bad and resulted in unsorted json, so I had to implement sorter.py
as a function.
'''

import json 


def sort_strum_patterns():
    '''
    Sorts a JSON file, hand when JSON data comes in the unsorted flavor.
    '''

    with open('json/unsortedStrumPatterns.json', 'r', encoding='utf-8') as f:
        JSON = json.load(f)

    # Can't sort strings so we convert the keys to ints
    keys_sorted = sorted({int(key) for key in JSON.keys()})

    # Now we need the keys to be strings again to get the JSON
    output = {key: sorted(JSON[str(key)]) for key in keys_sorted if key >= 4}
                                                                     
    with open('json/newStrumPatterns.json', 'w', encoding='utf-8') as f:
        json.dump(output, f)

    print('JSON sorted.')


def rhythm_permutations(start=[2, 3, 4], size=8):

    upper = size // 2
    old    = [[dig] for dig in start] 
    digits = [[dig] for dig in start]

    for _ in range(1, upper):
        tmp = []
        for digit in start:
            for tail in old:
                slice = [digit] + tail
                sum_slice = sum(slice)

                if sum_slice <= size:
                    tmp.append(slice)

        old = tmp
        digits += old
    return digits


def write_strums_to_json(max=12):
    '''This algo is a bit different in 0.3.7c.'''
    print(f"Calculating all perms for max={max}")

    all_eighth_notes = rhythm_permutations(size=max)
    res = {}
    for i in all_eighth_notes:
        key = sum(i)
        tmp = res.get(key)
        if tmp != None:
            tmp.append(i)
        else:
            res[key] = [i]

    with open('json/unsortedStrumPatterns.json', 'w', encoding='utf-8') as f:
        json.dump(res, f)

    sort_strum_patterns()

write_strums_to_json(max=20)
