#!/bin/python3

"""
I spent a long time thinking up this blazingly fast algorithm and am very proud
of it. If you find a use for something like this, please use it!
"""

import json


# start can be any list of unique ints.
def rhythm_permutations(start=[2, 3, 4], size=8):
    """
    This can calculate size=20 in 0m0.103s where as heap_perm would take hours to calculate size=18

    The premise is that I want every permutation before a certain length
    Including duplicate results. The way to achieve duplicate results with permutations
    requires input that looks like this [2, 2, 2, 2, 3, 3, 4, 4] and it can only have
    as many copies of any digit as are in your input, and the max length is huge.

    This is a huge waste because we have to count all the permutations for length of the input.
    Where as I only care about the length where the sum of all twos is less than or equal
    to the size. By only using each digit once we have dramatically reduced the amount of work
    the computer does by two different factors. Both the max length of the
    input can be much smaller and the length of desired output is much smaller.
    Also we are calculating all the different length perms in one go, instead of x different
    times. I took O(N! * M) down to basically O(Nᴹ)
    """

    upper = size // 2
    old = []
    results = []

    # This is easier to translate to Go than comprehensions.
    for i in start:
        old.append([i])
        if i == size:
            results.append([i])

    for _ in range(1, upper):
        tmp = []
        for digit in start:
            for tail in old:
                # This piece of code is the most different in every language.
                perm = [digit] + tail
                sum_perm = sum(perm)

                if sum_perm == size:
                    results.append(perm)
                    continue

                if sum_perm == size - 1:
                    continue

                if sum_perm < size:
                    tmp.append(perm)

        old = tmp

    return results


def write_strums_to_json(max=12, min=4):
    all_eighth_notes = {}

    for size in range(min, max + 1):
        print(f"Finding strum patterns with {size} eighth notes.")
        all_eighth_notes[size] = sorted(rhythm_permutations(size=size))

    with open("json/newStrumPatterns2.json", "w", encoding="utf-8") as f:
        json.dump(all_eighth_notes, f)


# write_strums_to_json(max=20)
print(sorted(rhythm_permutations(size=16)))
