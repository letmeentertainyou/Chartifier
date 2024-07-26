"""
There are some methods and techniques from Python that are not worth reinventing in C so this half
of the module interfaces with the C code in rhythm_utils and puts a pretty Pythonic wrapper on the results.
"""

import rhythm_utils

# These lists should be type hinted by my system python is 3.8 for the moment.
def perms(size: int):
    """Turns a flat array two dimensional and sorts it."""

    perms = rhythm_utils.permutations(size)
    res = []
    tmp = []
    for i in perms:
        if i != 0:
            tmp.append(i)
        else:
            res.append(tmp)
            tmp = []
    del perms
    del tmp    
    return sorted(res)
