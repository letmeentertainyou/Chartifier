#!/bin/python3

'''
This version of the algorithm is more optimal calculating perms for a large 
range of different eighth notes. The main algorithm only runs once ever, but
you do need the .sorter script to polish up the output of this file.

This file is how the strum patterns in js/strumPatterns.js and python/strum_patterns.py
are generated, I spent a long time thinking up this blazingly fast algorithm and am very proud
of it. If you find a use for something like this, please use it!
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
    output = {key: sorted(JSON[str(key)]) for key in keys_sorted if key >= 4}   # 4 here is where the
                                                                                # strum patterns start
    with open('json/newStrumPatterns.json', 'w', encoding='utf-8') as f:
        json.dump(output, f)

    print('JSON sorted.')


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
    times. I took O(N! * M) down to basically O(Nᴹ)
    '''

    upper = size // 2
    
    old    = [[dig] for dig in start]       # It's weird that I need this
    digits = [[dig] for dig in start]       # data twice but I genuinely do

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

# It takes about 90 seconds to generate max=40, and part of that time is writing the json to a file. 
# That file is 200 megs and my computer can't open it. But this algorithm is still very useful 
# because it would have taken days to calculate max=20 with heap's permutation algo.
#
# I use this generator for groupings of eighth notes but it could be applied to quarter notes or 
# whole notes or some kind of subdivision. You can use some basic division/multiplication to mix
# for instance eighth and quarter note patterns. This is left as an exorcise to the reader.
# 
# You would be hard pressed to come up with a human playable rhythm that can't be expressed with max=30. 
# In fact, I'd be very excited to see human playable strum patterns or rhythms not represented 
# by max=30, submit it as a bug or pull request. I'd love to see what I'm missing here.
#
# This work was done with the intention of benefiting human musicians, and their sensibilities. Which
# is why I'm only interested in patterns that a human can play but are not represented by max=30.
# A computer could play any arbitrary pattern size without worrying about feeble human memory.
#
# Side note: [2, 3, 3, 2, 2, 3] is a certified banger, use it in your next track!