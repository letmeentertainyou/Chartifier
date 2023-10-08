#!/bin/python3

'''
I ended up building out all 7 main modes, and melodic/harmonic minor scales.
I am choosing not to support double flats/sharps and keys with both types of accent.

MUSIC THEORY NOTES FOR DEVELOPERS
order of sharps  f c g d a e b
order of flats   b e a d g c f
                                7   6   5  4  3  2  1  0
7 sharp keys                    C#  F#  B  E  A  D  G  C
7 flat keys   C  F  Bb  Eb  Ab  Db  Gb  Cb 
              0  1  2   3   4   5   6   7


REMOVED KEYS
These keys have all been removed because they use double flats, double sharps
or the sinful sharp + flat combo. Well they are real music keys that can be played
They are impractical for anyone reading a chord chart anyways and so supporting them is
very low priority.

Double Sharps
G# D# A# E# B#

Melodic G, Gb, Cb
      G melodic has 1 flat/1 sharp and my API is not going to allow for that.
      G 2 A 1 Bb 2 C 2 D 2 E 2 F# 1 G

Harmonic Db, D, Gb, G, Cb
'''

from itertools import combinations
from random import choice


def join(iterable, string: str):
    return string.join(iterable)


##############################################################################

############################# HARMONY GENERATOR ##############################

########################################################3#####################

diatonic_notes: dict = { 'C#': 'Db', 'F#': 'Gb', 'B' : 'Cb', 'Db': 'C#', 'Gb': 'F#', 'Cb': 'B' }

primary_sharps   = ('C',  'C#', 'D', 'D#', 'E', 'F',  'F#', 'G', 'G#', 'A', 'A#', 'B' )
secondary_sharps = ('C',  'C#', 'D', 'D#', 'E', 'E#', 'F#', 'G', 'G#', 'A', 'A#', 'B' )
tertiary_sharps  = ('B#', 'C#', 'D', 'D#', 'E', 'E#', 'F#', 'G', 'G#', 'A', 'A#', 'B' )

primary_flats    = ('C',  'Db', 'D', 'Eb', 'E',  'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B' )
secondary_flats  = ('C',  'Db', 'D', 'Eb', 'E',  'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'Cb')
tertiary_flats   = ('C',  'Db', 'D', 'Eb', 'Fb', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'Cb')

sharps           = (primary_sharps, secondary_sharps, tertiary_sharps)
flats            = (primary_flats,  secondary_flats,  tertiary_flats )

ionian_names  = ('Ionian', 'Dorian', 'Phrygian', 'Lydian', 'Mixolydian', 'Aeolian', 'Locrian')

ionian_keys   = ('C', 'C#', 'Db', 'D', 'Eb', 'E', 'F', 'F#', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B', 'Cb')
melodic_keys  = ('C', 'C#', 'Db', 'D', 'Eb', 'E', 'F', 'F#',            'Ab', 'A', 'Bb', 'B',     )
harmonic_keys = ('C', 'C#',            'Eb', 'E', 'F', 'F#',            'Ab', 'A', 'Bb', 'B',     )

ionian    = ((2, 'Maj'), (2, 'Min'), (1, 'Min'), (2, 'Maj'), (2, 'Maj'), (2, 'Min'), (1, 'Dim'))
melodic   = ((2, 'Min'), (1, 'Min'), (2, 'Aug'), (2, 'Maj'), (2, 'Maj'), (2, 'Dim'), (1, 'Dim'))
harmonic  = ((2, 'Min'), (1, 'Dim'), (2, 'Aug'), (2, 'Min'), (1, 'Maj'), (3, 'Maj'), (1, 'Dim'))


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


# Not random yet, just 12 bars. Still rad!
def random_chord_chart(chords):
    twelve_bar  = [1, 1, 1, 1, 4, 4, 1, 1, 4, 1, 4, 5]
    progression = []
    for i in twelve_bar:
        progression.append(chords[i-1])
    print(progression)


##############################################################################

############################## RHYTHM GENERATOR ##############################

########################################################3#####################


# This just does my slashes should be easy enough
def strummer(list_int):
    result = []
    for num in list_int:
        result.append('/' * num)
    return join(iterable=result, string=' ')


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

'''
pattern = random_strum_pattern()
chords, key = random_chords()
print([pattern, chords, key])
random_chord_chart(chords=chords)
'''
