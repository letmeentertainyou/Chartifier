#!/bin/python3

from random import choice

from music_theory import *
from rhythm import rhythm_permutations

# RHYTHM #


def random_strum_pattern(size=8):
    """
    Strum patterns are defined in the file js/strumPatterns.js, this function randomly
    picks a strum pattern and makes it human readable. If size isn't a valid strumPatterns
    key things will crash.
    """

    def strummer(list_int):
        """
        This replaces ints with slashes for the strum pattern.
        """
        result = []
        for num in list_int:
            result.append("/" * num)
        return " ".join(result)

    return strummer(choice(rhythm_permutations[size]))


# HARMONY #

# String padding function has been omitted from the Python source because it's built into the language.


def chords_from_key(key: str = "C", mode_offset: int = 0, mode=ionian, first_pass=True):
    """
    This function takes a key, a mode_offset(0 to 6) and a mode, and tries to
    load a set of keys. If it fails on the first pass it will try again with
    a diatonic alternative for the key. So it might try Gb maj if F# fails (F# won't fail)]

    With the data in musicTheory.js this function is extremely capable of finding lots of
    weird keys. I don't even know what the modes for melodic/harmonic mind are called but this
    supports most of them.
    """

    def assembler(notes):
        """
        This function takes a give set of notes, and attempts to build some chords out of it
        the outer function confirms that the lenSetFirstChars assembler returns is 7.

        assembler is called until it returns a seven or there are no more note pools to draw from.
        """
        if key not in notes:
            return [], 0

        start: int = notes.index(key)
        shifted_notes = notes[start:] + notes[:start]
        chords = []
        idx: int = 0
        chosen_mode = mode[mode_offset:] + mode[:mode_offset]

        for chord in chosen_mode:
            note = shifted_notes[idx]
            fullname = f"{note} {chord[1]}"

            chords.append(fullname)
            idx += chord[0]

        return chords, len(set(i[0] for i in chords))

    all_notes = [sharps, flats]
    if "b" in key:  # skips sharps
        all_notes = [flats]
    if "#" in key:  # skips flats
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
    """
    Picks a random key and random variation of the ionian mode (harmonic/melodic could be
    used instead), then loads up the chords from that key/mode. If randomKey gets an invalid
    key for some reason (rare), it just keeps trying until a valid key is found.
    """
    key = choice(ionian_keys)
    mode_offset = choice(range(7))
    mode_name = ionian_names[mode_offset]
    chords, key = chords_from_key(key, mode_offset, ionian)

    if not chords:
        return random_key()

    return chords, f"{key} {mode_name}"


# RANDOM CHORD CHART MATH #


def chart_from_numbers(chords):
    """
    This generates some chord numbers and then applies them to a given set of chords.
    """
    numbers = chord_numbers(12)
    progression = []

    for i in numbers:
        progression.append(chords[i - 1])

    return progression


def chord_numbers(count=12):
    """
    This chooses x chords at random, and generates some additional weighting info for those chords too.
    This function also forces the first and last chord of a progression to be the one chord. This is a
    common music theory practice but it can be removed for more random charts.
    """
    result = []
    weights = chord_weights(count=count)

    for i in range(len(weights)):
        if i == 0 or i == count - 1:
            result.append(1)
        else:
            result.append(choice(weights[i]))

    return result


def chord_weights(count=12):
    """
    This generates some random weights for whatever length of chord chart you want.
    This is just my first go at this math and I won't change it until the website is a
    bit nicer so I can freeze this version of the algorithm.

    There are many flaWs with this version, namely that a chord can appear too many times
    in a row. But actually that needs to be solved in the function above.
    """

    def manip(prev):
        """
        Picks a number from the current set of weights and adds two more of that number.
        """
        magic_number = choice(prev)
        tmp = list(prev)
        tmp += 2 * [magic_number]
        tmp.sort()
        return tuple(tmp)

    # These are not zero indexed so that they are readable by human musicians.
    start = (1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, 5, 6, 6, 7)
    result = [start]

    for x in range(count - 1):
        result.append(manip(result[x]))

    return result


####### EXAMPLES #######
strum = random_strum_pattern()
chords, key = random_key()
print([strum, chords, key])
print(chart_from_numbers(chords))
