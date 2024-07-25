/* 
The goal here is to replicate the functions from rhythm.py as a C Python file so I can
build my first Python C extension. I have put a lot of thought into how I can handle multi
dimensional arrays where the size of the inner and outer arrays are dynamic. And I decided to
skip the whole mess by using one single resizable array that uses zeros to mark the end of each
sub array.
*/


#include "rhythm.h"

Array *rhythm_permutations(int size) {
    Array *start = array_init((int[]){2, 3, 4}, 3);
    Array *old = empty_init(10);
    Array *tmp = empty_init(10);
    Array *tail = empty_init(10);
    Array *perm = empty_init(10);
    Array *results = empty_init(10);
    
    int upper = size / 2;
    for (int i = 0; i < start->length; i++) {
        old = append_pad(old, unpack(start, i));
    }

    for (int j = 0; j < upper; j++) {
        for (int dig = 0; dig < start->length; dig ++) {
            int digit = unpack(start, dig);

            for (int k = 0; k < old->length; k ++) {
                int val = unpack(old, k);
                if (val != 0) {
                    tail = append(tail, val);
                } else {
                    clear_array(perm);
                    perm = append(perm, digit);
                    perm = extend(perm, tail);
                    clear_array(tail);

                    int sum_perm = sum_array(perm);
                    if (sum_perm == size) {
                        results = extend_pad(results, perm);
                        continue;
                    }
                    else if (sum_perm == size - 1) {
                        continue;
                    }
                    else if (sum_perm < size) {
                        tmp = extend_pad(tmp, perm);
                    }
                }
            }
            clear_array(tail);
        }
        Array* swap = old;
        old = tmp;
        tmp = swap;
        clear_array(tmp);
    }
    free(start);
    free(old);
    free(tmp);
    free(tail);
    free(perm);
    return results;
}