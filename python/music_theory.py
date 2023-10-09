#!/bin/python3

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

# Modify as needed.
__all__ = ["diatonic_notes", "sharps", "flats", "ionian_names", "ionian_keys", "melodic_keys", "harmonic_keys", "ionian", "melodic", "harmonic"]


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


