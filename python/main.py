#!/bin/python3

from random import choice

from music_theory import *
from strum_patterns import *

########## RHYTHM ##########

# These are defined in the file python/strum_patterns.py
def random_strum_pattern(size=8):
    # This just does my slashes for the strum pattern
    def strummer(list_int):
        result = []
        for num in list_int:
            result.append('/' * num)
        return ' '.join(result)

    return strummer(choice(strum_patterns[size]))


########## HARMONY ##########

# String padding function has been omitted from the Python source because it's built into the language.


def chords_from_key(key: str='C', mode_offset: int=0, mode=ionian, first_pass=True):

    def assembler(notes):
        if key not in notes:
            return [], 0

        start: int    = notes.index(key)
        shifted_notes = notes[start:] + notes[:start]
        chords        = []
        idx: int      = 0
        chosen_mode = mode[mode_offset:] + mode[:mode_offset]

        # This part is less involved than the JS because there is no padding.
        for chord in chosen_mode:
            note = shifted_notes[idx]
            fullname = f'{note} {chord[1]}'

            chords.append(fullname)
            idx += chord[0]

        return chords, len(set(i[0] for i in chords))

    all_notes  = [sharps, flats]
    if 'b' in key:      # skips sharps
        all_notes = [flats]
    if '#' in key:      # skips flats
        all_notes = [sharps]

    for index in range(3):
        for notes in all_notes:
            chords, chords_length = assembler(notes[index])

            if chords_length == 7:
                return chords, key

    if first_pass:
        key = diatonic_notes.get(key)
        if key:
            return chords_from_key(key, mode_offset, mode, False)

    return [], key


def random_key():
    key         = choice(ionian_keys)
    mode_offset = choice(range(7))
    mode_name   = ionian_names[mode_offset]
    chords, key = chords_from_key(key, mode_offset, ionian)

    if not chords:
        return random_key()

    return chords, f"{key} {mode_name}"


####### CHORD CHART MATH #######

def chart_from_numbers(chords):
    numbers = chord_numbers(12)
    progression = []

    for i in numbers:
        progression.append(chords[i -1])

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
        tmp.sort()
        return tuple(tmp)

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
print(chart_from_numbers(chords))

