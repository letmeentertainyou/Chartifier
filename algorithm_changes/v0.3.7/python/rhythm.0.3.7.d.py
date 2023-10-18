#!/bin/python3

import json 


def rhythm_permutations(start=[2, 3, 4], size=8):

    upper = size // 2
    old     = []
    results = []

    for i in start:
        old.append([i])
        if i == size:
            results.append([i])

    for _ in range(1, upper):
        tmp = []
        for digit in start:
            for tail in old:
                perm = [digit] + tail
                sum_perm = sum(perm)

                if sum_perm == size:
                    results.append(perm)
                    continue

                if sum_perm == size -1:
                    continue

                if sum_perm < size:
                    tmp.append(perm)

        old = tmp

    return results


def write_strums_to_json(max=12, min=4):

    all_eighth_notes={}

    for size in range(min, max +1):
        print(f'Finding strum patterns with {size} eighth notes.')
        all_eighth_notes[size] = sorted(rhythm_permutations(size=size))

    with open('json/newStrumPatterns2.json', 'w', encoding='utf-8') as f:
        json.dump(all_eighth_notes, f)

write_strums_to_json(max=20)
