/* 
    An implementation of the code I originally wrote in Python/Go/Javascript. It's striking me now
    how little the doc strings in those languages actually explain what the function does. I will
    write that in great detail later.
*/


#include "rhythm_utils.h"

Array *rhythm_permutations(int size) {
    Array *start = array_from_array((int[]){2, 3, 4}, 3);
    Array *old = empty_array(10);
    Array *tmp = empty_array(10);
    Array *tail = empty_array(10);
    Array *perm = empty_array(10);
    Array *results = empty_array(10);
    
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