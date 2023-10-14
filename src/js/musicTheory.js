/*
I ended up building out all 7 main modes, and melodic/harmonic minor scales.
I am choosing not to support double flats/sharps and keys with both types of accent.

MUSIC THEORY NOTES FOR DEVELOPERS:
order of sharps  F C G D A E B
order of flats   B E A D G C F
                                7   6   5  4  3  2  1  0
7 sharp keys                    C♯  F♯  B  E  A  D  G  C
7 flat keys   C  F  B♭  E♭  A♭  D♭  G♭  C♭ 
              0  1  2   3   4   5   6   7                  

REMOVED KEYS:
These keys have all been removed because they use double flats, double sharps
or the sinful sharp + flat combo. Well they are real music keys that can be played
They are impractical for anyone reading a chord chart anyways and so supporting them is
very low priority.

Dou♭le Sharps
G♯ D♯ A♯ E♯ B♯

Melodic G, G♭, C♭
      G melodic has 1 flat/1 sharp and my API is not going to allow for that.
      G 2 A 1 B♭ 2 C 2 D 2 E 2 F♯ 1 G

Harmonic D♭, D, G♭, G, C♭
*/

'use strict'


var diatonic_notes = { 'C♯': 'D♭', 'F♯': 'G♭', 'B': 'C♭', 'D♭': 'C♯', 'G♭': 'F♯', 'C♭': 'B' };

var primary_sharps   = ['C',  'C♯', 'D', 'D♯', 'E', 'F',  'F♯', 'G', 'G♯', 'A', 'A♯', 'B'];
var secondary_sharps = ['C',  'C♯', 'D', 'D♯', 'E', 'E♯', 'F♯', 'G', 'G♯', 'A', 'A♯', 'B'];
var tertiary_sharps  = ['B♯', 'C♯', 'D', 'D♯', 'E', 'E♯', 'F♯', 'G', 'G♯', 'A', 'A♯', 'B'];

var primary_flats    = ['C', 'D♭', 'D', 'E♭', 'E',  'F', 'G♭', 'G', 'A♭', 'A', 'B♭', 'B' ];
var secondary_flats  = ['C', 'D♭', 'D', 'E♭', 'E',  'F', 'G♭', 'G', 'A♭', 'A', 'B♭', 'C♭'];
var tertiary_flats   = ['C', 'D♭', 'D', 'E♭', 'F♭', 'F', 'G♭', 'G', 'A♭', 'A', 'B♭', 'C♭'];

var sharps           = [primary_sharps, secondary_sharps, tertiary_sharps];
var flats            = [primary_flats, secondary_flats, tertiary_flats];

var ionian_names     = ['Ionian', 'Dorian', 'Phrygian', 'Lydian', 'Mixolydian', 'Aeolian', 'Locrian'];

var ionian_keys   = ['C', 'C♯', 'D♭', 'D', 'E♭', 'E', 'F', 'F♯', 'G♭', 'G', 'A♭', 'A', 'B♭', 'B', 'C♭'];
var melodic_keys  = ['C', 'C♯', 'D♭', 'D', 'E♭', 'E', 'F', 'F♯',            'A♭', 'A', 'B♭', 'B'      ];
var harmonic_keys = ['C', 'C♯',            'E♭', 'E', 'F', 'F♯',            'A♭', 'A', 'B♭', 'B'      ];

var ionian   = [[2, 'Maj'], [2, 'Min'], [1, 'Min'], [2, 'Maj'], [2, 'Maj'], [2, 'Min'], [1, 'Dim']];
var melodic  = [[2, 'Min'], [1, 'Min'], [2, 'Aug'], [2, 'Maj'], [2, 'Maj'], [2, 'Dim'], [1, 'Dim']];
var harmonic = [[2, 'Min'], [1, 'Dim'], [2, 'Aug'], [2, 'Min'], [1, 'Maj'], [3, 'Maj'], [1, 'Dim']];

