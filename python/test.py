#!/bin/python3

# I added two more vars to this which feels sloppy, but should
# dramatically reduce the number of permutations.
# Going to test this against the old algo.

def rhythm_permutations2(start=[2, 3, 4], size=8):

    upper = size // 2
    old = [[dig] for dig in start]
    digits = []
    for length in range(1, upper):

        tmp = []
        for digit in start:
            
            for tail in old:
                if len(tail) == length:
                    slice = [digit] + tail
                    sum_slice = sum(slice)
                    # If the size is even, and sum_slice == size -1, and two is the smallest int
                    # in start then we can continue here.
                    if (size % 2 == 0 and sum_slice == size -1):
                        continue

                    # This gave an additional 35x speed up.
                    if sum_slice <= size:
                        tmp.append(slice)
        old = tmp
        digits += old
        
    return [z for z in digits if sum(z) == size]

print(rhythm_permutations())