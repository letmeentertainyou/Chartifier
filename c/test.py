#!/bin/python3
""" 
This just imports the two versions of the module and prints their outputs. You have to run pybuild
to build the binaries before this script does anything.
"""

import rhythm_utils
import rhythm

size = 8

print(rhythm_utils.permutations(size))
print(rhythm.perms(size))