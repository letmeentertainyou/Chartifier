#!/bin/python3

from itertools import combinations
from random import choice

from music_theory import *

###############################################################################
############################## HARMONY GENERATOR ##############################
########################################################3######################

# Fixed a bug where B phrygian was labeled d Cb phrygian, now this function returns the key too.
def chords_from_key(key: str='C', mode_offset: int=0, mode=ionian, first_pass=True):
    '''Unsupported keys return an empty list.'''

    def assembler(notes):
        '''This needs a seriously cleanup.'''
        if key not in notes:
            return [], 0

        start: int    = notes.index(key)
        shifted_notes = notes[start:] + notes[:start]
        chords        = []
        idx: int      = 0
                     # This remaps the mode to the offset you picked
        for chord in mode[mode_offset:] + mode[:mode_offset]:
            chords.append(f'{shifted_notes[idx]} {chord[1]}')
            idx += chord[0]

        return chords, len(set(i[0] for i in chords) )

    all_notes  = [sharps, flats]
    if 'b' in key:      # skips sharps
        all_notes.remove(sharps)
    if '#' in key:      # skips flats
        all_notes.remove(flats)

    for index in range(3):
        for notes in all_notes:
            # Can't hint tuple expansion, this is a major design flaw in Python.
            chords, chord_len = assembler(notes[index])
            if chord_len == 7:
                return chords, key

    # check if it's first run, if yes, try to get a diatonic alternate key, is successful recurse,
    # but now bool is false, and we always hit the return on our second loop.
    if first_pass:
        key = diatonic_notes.get(key)
        if key:
            return chords_from_key(key=key, mode_offset=mode_offset, mode=mode, first_pass=False)

    return [], key


def random_chords():
    key         = choice(ionian_keys)
    mode_offset = choice(range(7))
    mode_name   = ionian_names[mode_offset]
    chords, key = chords_from_key(key=key, mode=ionian, mode_offset=mode_offset)

    if not chords:
        return random_chords()

    return chords, f"{key} {mode_name}"


####### CHORD CHART MATH #######


# Not random yet, just 12 bars. Still rad!
def chord_chart(chords):
    numbers = chord_numbers(12)
    progression = []

    for i in numbers:
        progression.append(chords[i -1])

    print(progression)
    return progression

def chord_numbers(count=12):
    result = []
    weights = chord_weights(count=count)
    for i in range(len(weights)):
        if i == 0 or i == count: 
            result.append(1)
        else: 
            result.append(choice(weights[i]))
    return result


# Rename these names
def chord_weights(count=12):
    '''How many times a chord appears in the list can be a primitive for weighing the chords.
    
    Weights should also change based on where in the progression you are and I haven't figured that out yet.'''
    
    def manip(c):
        '''Pick random number and reduce it's appearances unless it only appears once then double it.'''
        magic_number = choice(c)
        tmp = list(c)
        tmp += 2 * [magic_number]
        return tuple(sorted(tmp))

    start = (1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, 5, 6, 6, 7)
    result = [start]
    for x in range(count -1):
         result.append(manip(result[x]))
    return result


##############################################################################
############################## RHYTHM GENERATOR ##############################
########################################################3#####################


# This just does my slashes should be easy enough
def strummer(list_int):
    result = []
    for num in list_int:
        result.append('/' * num)
    return ' '.join(result)


def eighth_note_pool(size: int=8, upper: int = 4):
    pool = []
    for i in range(2, upper + 1):
        pool += size // i * [i]
    return pool


# Converts a pool of eighth notes into a set of combos.
def unique_combos(size: int=8, pool=[]) -> set:
    combos = set()
    for r in range(len(pool), 0, -1):     # What is this weird range?
        # Take every combination for every r=i and loop through each combo
        for combo in combinations(iterable=pool, r=r):
            if sum(combo) == size:
                combos.add(combo)
                # Grab the reverse here real quick
                combos.add(combo[::-1])
    return combos


# Generate random size/upper for more variations on rhythm.
def random_strum_pattern(size: int = 8, upper: int = 4):
    pool = eighth_note_pool(size, upper=upper)
    combos = unique_combos(size=size, pool=pool)
    return choice([strummer(result) for result in combos])


###################################################################################################
###################################################################################################

# EXample uses


pattern = random_strum_pattern()
chords, key = random_chords()
print([pattern, chords, key])
chord_chart(chords=chords)

