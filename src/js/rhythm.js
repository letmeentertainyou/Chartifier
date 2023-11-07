/*  
    I don't know why but 'use strict' breaks this file entirely.

    This can calculate size=20 in 0m0.103s where as heap_perm would take hours to calculate size=18

    The premise is that I want every permutation before a certain length
    Including duplicate results. The way to achieve duplicate results with permutations
    requires input that looks like this [2, 2, 2, 2, 3, 3, 4, 4] and it can only have
    as many copies of any digit as are in your input, and the max length is huge.

    This is a huge waste because we have to count all the permutations for length of the input.
    Where as I only care about the length where the sum of all twos is less than or equal
    to the size. By only using each digit once we have dramatically reduced the amount of work
    the computer does by two different factors. Both the max length of the
    input can be much smaller and the length of desired output is much smaller.
    Also we are calculating all the different length perms in one go, instead of x different
    times. I took O(N! * M) down to basically O(Nᴹ)
*/

function rhythmPermutations(size = 8, start = [2, 3, 4]) {
    var upper = intDiv(size, 2);
    var old = [];
    var results = [];

    // This is easier to translate to Go than comprehensions.
    for (let i of start) {
        old.push([i]);
        if (i == size) {
            results.push([i]);
        }
    }

    // gonna need xrange
    for (_ in xrange(upper, 1)) {
        var tmp = [];
        for (let digit of start) {
            for (let tail of old) {
                // This piece of code is the most different in every language.
                var perm = [digit, ...tail];
                var sum_perm = sum(perm);

                if (sum_perm == size) {
                    results.push(perm);
                    continue;
                }

                if (sum_perm == size - 1) {
                    continue;
                }

                if (sum_perm < size) {
                    tmp.push(perm);
                }
            }
        }
        old = tmp;
    }
    return results;
}

// write_strums_to_json(max=20)
//rhythm_permutations(16)
