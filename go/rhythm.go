/*
The rhythm_permutations function was written in Pyhton by me and translated to Go here:

https://www.codeconvert.ai/python-to-golang-converter

Thank you codeconvert.ai!

This is now a fully working implementation of rhythm.py including the
JSON output, the only issue is that the JSON Go generates sorts the keys differently.
10, 4, 5, 6, 7, 8, 9 etc

Which will make testing if the python and Go generate the same data tricky. My plan is to
write a python script that loads the Go generated JSON object and rewrites it correctly sorted.
It feels weak to need another language as a crutch like that but I can't find any other way to
solve the problem in native Go.

I have every intention to time Go and Python on some large inputs and see if it makes
any difference to use a compiled language here but I won't be able to diff the outputs
without dealing with the above sorting issue. I can tell you the Go output is correct for
size=8 though and that is lovely.
*/

package main

import (
	"encoding/json"
	"fmt"
	"os"
)

// The ai basically wrote this function twice, I just extracted it.
func sum(iterable[]int) int {
    result := 0
    for _, num := range iterable {
        result += num
    }
    return result
}


func rhythmPermutations(start[]int, size int) [][]int {
    /*
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

    upper  := size / 2
	old    := [][]int{}
    results := [][]int{}
    
    for _, i := range start {
		old    = append(old,    []int{i})
		if i == size {
        	results = append(results, []int{i})
		}
    }

    for length := 1; length < upper; length++ {
		tmp := [][]int{}
        for _, digit := range start {
            for _, tail := range old {
				// This piece of code is the most different in every language.
				perm := append([]int{digit}, tail...)
				sum_perm := sum(perm)

				if sum_perm == size {
					results = append(results, perm)
					continue
				}

				if sum_perm == size -1 {
					continue
				}

				if sum_perm < size {
					tmp = append(tmp, perm)
				}
            }
        }
		old = tmp
    }
    return results
}


// I used the the same ai to convert this too!
func writeStrumsToJSON(max, min int) {
    start := []int{2, 3, 4}
    allEighthNotes := make(map[int][][]int)
    
    for size := min; size <= max; size++ {
        fmt.Printf("Finding strum patterns with %d eighth notes.\n", size)
        allEighthNotes[size] = rhythmPermutations(start, size)
    }

    file, err := json.Marshal(allEighthNotes)
    if err != nil {
        fmt.Println(err)
        return
    }

    err = os.WriteFile("json/unsortedStrumPatterns.json", file, 0644)
    if err != nil {
        fmt.Println(err)
        return
    }
}

// UTILS
func printf(message any) {
	fmt.Println(message)
}

func main() {
	start := []int{2, 3, 4}
	printf(rhythmPermutations(start, 16))
	//writeStrumsToJSON(20, 4)
}
