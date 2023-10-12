#!/bin/python3

from json import load
from random import choice

from music_theory import *

########## RHYTHM ##########

# These are defined in the file json/strumPatterns.js
def random_strum_pattern(size=8):
    # This just does my slashes for the strum pattern
    def strummer(list_int):
        result = []
        for num in list_int:
            result.append('/' * num)
        return ' '.join(result)
    
    with open(f'../json/strumPatterns.json', 'r', encoding='utf-8') as f:
        strum_patterns = load(f)

    # Cause json doesn't have ints but the whole API uses ints.
    size = str(size)
    pick = strummer(choice(strum_patterns[size]))
    return pick



########## HARMONY ##########

# String padding function has been omitted from the Python source because it's built into the language.


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
        chosen_mode = mode[mode_offset:] + mode[:mode_offset]

        # This part is less involved than the JS because there is no padding.
        for chord in chosen_mode:
            chords.append(f'{shifted_notes[idx]} {chord[1]}')
            idx += chord[0]

        return chords, len(set(i[0] for i in chords))

    all_notes  = [sharps, flats]
    if 'b' in key:      # skips sharps
        all_notes.remove(sharps)
    if '#' in key:      # skips flats
        all_notes.remove(flats)

    for index in range(3):
        for notes in all_notes:
            chords, chord_len = assembler(notes[index])
            if chord_len == 7:
                return chords, key

    if first_pass:
        key = diatonic_notes.get(key)
        if key:
            return chords_from_key(key=key, mode_offset=mode_offset, mode=mode, first_pass=False)

    return [], key


def random_key():
    key         = choice(ionian_keys)
    mode_offset = choice(range(7))
    mode_name   = ionian_names[mode_offset]
    chords, key = chords_from_key(key=key, mode=ionian, mode_offset=mode_offset)

    if not chords:
        return random_key()

    return chords, f"{key} {mode_name}"


####### CHORD CHART MATH #######

def chart_from_numbers(chords):
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
        if i == 0 or i == count -1: 
            result.append(1)
        else: 
            result.append(choice(weights[i]))
    return result


# Rework these names
def chord_weights(count=12):
    '''How many times a chord appears in the list can be a primitive for weighing the chords.
    
    Weights should also change based on where in the progression you are and I haven't figured that out yet.
    
    Also if a chord appears x times in a row it shouldn't appear again.'''
    
    def manip(c):
        '''Pick random number and double it's appearances.'''
        magic_number = choice(c)
        tmp = list(c)
        tmp += 2 * [magic_number]
        return tuple(sorted(tmp))

    # These are not zero indexed so that they are readable by human musicians.
    start = (1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, 5, 6, 6, 7)
    result = [start]

    for x in range(count -1):
         result.append(manip(result[x]))
    return result




####### EXAMPLES #######
strum = random_strum_pattern()
chords, key = random_key()
print([strum, chords, key])
chart_from_numbers(chords=chords)

