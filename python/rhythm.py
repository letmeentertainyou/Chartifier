#!/bin/python3

'''This file is how the strum patterns in js/strumPatterns.js and python/strum_patterns.py
are generated, I spent a long time thinking up this blazingly fast algorithm and am very proud
of it. If you find a use for something like this, please use it!'''

import json 

                      # start can be any list of unique ints.
def rhythm_permutations(start=[2, 3, 4], size=8):
    '''
    This can calculate size=20 in 0m0.103s where as heap_perm would take hours to calculate size=18

    The premise is that I want every permutation before a certain length
    Including duplicate digits. The way to achieve duplicate digits with permutations
    requires input that looks like this [2, 2, 2, 2, 3, 3, 4, 4] and it can only have
    as many copies of any digit as are in your input, and the max length is huge.

    This is a huge waste because we have to count all the permutations for length of the input.
    Where as I only care about the length where the sum of all twos is less than or equal
    to the size. By only using each digit once we have dramatically reduced the amount of work 
    the computer does by two different factors. Both the max length of the
    input can be much smaller and the length of desired output is much smaller.
    Also we are calculating all the different length perms in one go, instead of x different
    times. I took O(N! * length) down to basically O(N)

    This could be recursive but I'm not going to rewrite it.
    I tried to use upper -1 so that the list that only contains 2s doesn't need to be calculated
    but it didn't improve the time at all, and it made the code uglier, so I removed it.'''

    upper = size // 2
    digits = [[dig] for dig in start]
    
    for length in range(1, upper):
        for digit in start:
            for tail in digits:
                if len(tail) == length:
                    slice = [digit] + tail

                    # This gave an additional 35x speed up.
                    if sum(slice) <= size:
                        digits.append(slice)

    return [z for z in digits if sum(z) == size]


def write_strums_to_json(max=12, min=4):
    all_eighth_notes={}
    for x in range(min, max +1):
        print(f'Finding strum patterns with {x} eighth notes.')
        all_eighth_notes[x] = sorted(rhythm_permutations(size=x))

    with open(f'../json/newStrumPatterns.json', 'w', encoding='utf-8') as f:
        json.dump(all_eighth_notes, f)

write_strums_to_json(max=30)


