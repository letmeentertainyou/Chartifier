#!/bin/python3

import json 


def rhythm_permutations(start=[2, 3, 4], size=8):

    upper = size // 2
    old     = [[dig] for dig in start]
    results = [[dig] for dig in start]

    for _ in range(1, upper):
        tmp = []
        for digit in start:
            for tail in old:
                slice = [digit] + tail
                sum_slice = sum(slice)

                if (size % 2 == 0 and sum_slice == size -1):
                    continue

                if sum_slice <= size:
                    tmp.append(slice)

        old = tmp
        results += old

    return [z for z in results if sum(z) == size]


def write_strums_to_json(max=12, min=4):
    all_eighth_notes={}
    for size in range(min, max +1):
        print(f'Finding strum patterns with {size} eighth notes.')
        all_eighth_notes[size] = sorted(rhythm_permutations(size=size))

    with open('json/newStrumPatterns.json', 'w', encoding='utf-8') as f:
        json.dump(all_eighth_notes, f)

write_strums_to_json(max=20)
