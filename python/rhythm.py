#!/bin/python3

import json 

# This can calculate size=20 in 0m0.103s where as heap_perm would take hours to calculate size=18

# The premise is that I want every permutation before a certain length
# Including duplicate digits. The way to achieve duplicate digits with permutations
# requires input that looks like this [2, 2, 2, 2, 3, 3, 4, 4] and it can only have
# as many copies of any digit as are in your input, and the max length is huge.

# This is a huge waste because we have to count all the permutations for length of the input.
# Where as I only care about the length where the sum of all twos is less than or equal
# to the size. By only using each digit once we have dramatically reduced the amount of work 
# the computer does by two different factors. Both the max length of the
# input can be much smaller and the length of desired output is much smaller.
# Also we are calculating all the different length perms in one go, instead of x different
# times. I took O(N! * length) down to basically O(N)

# This could be recursive but I'm not going to rewrite it.
def rhythm_permutations(start=[2, 3, 4], size=8):
    # If I do upper -1 and then append a list of 2s to the end, we get even more speed.
    # Only if size is even though.

    upper = size // 2
    digits = [[n] for n in start]
    def worker():
        for length in range(1, upper):
            for digit in start:
                for tail in digits:
                    if len(tail) == length:
                        slice = [digit] + tail
                        # This gave a 35x speed up.
                        if sum(slice) <= size:
                            digits.append(slice)

    worker()

    # This could be moved somewhere else if the user wants my perms for some other use.
    return [z for z in digits if sum(z) == size]



# Go back to single json file, and max
# Load json file and if a key exists then don't render it
# Then write to a new file so we don't lose the old.
def write_strums_to_json(max=12, min=4):
    #with open('../json/strumPatterns.json', 'r') as tmp:
    #    old = json.load(tmp)

    all_eighth_notes={}
    for x in range(min, max +1):
        print(f'Finding strum patterns with {x} eighth notes.')
        all_eighth_notes[x] = sorted(rhythm_permutations(size=x))
        #print(all_eighth_notes)
    with open(f'../json/newStrumPatterns.json', 'w', encoding='utf-8') as f:
        json.dump(all_eighth_notes, f)

write_strums_to_json(max=30)


