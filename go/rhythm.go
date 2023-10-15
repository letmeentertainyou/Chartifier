/*
The rhythm_permutations function was written in Pyhton by me and translated to Go here:

https://www.codeconvert.ai/python-to-golang-converter

Thank you codeconvert.ai!

This is now a fully working implementation of rhythm.py including the
JSON output, the only issue is that the JSON Go generates sorts the keys differently.
10, 4, 5, 6, 7, 8, 9 etc

Which will make testing if the python and Go generate the same data tricky. My plan is to
write a python script that loads the Go generated JSON object and rewrites it correctly sorted.
It feels weak to need another langauge as a crutch like that but I can't find any other way to
solve the problem in native Go.

I have every intention to time Go and Python on some large inputs and see if it makes
any difference to use a compiled langauge here but I won't be able to diff the outputs
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
    Including duplicate digits. The way to achieve duplicate digits with permutations
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

    // Go is so elegant with int division
    upper := size / 2
    digits := [][]int{}
    
    // This code converter is very clever and I love it a lot.
    for _, dig := range start {
        digits = append(digits, []int{dig})
    }

    for length := 1; length < upper; length++ {
        for _, digit := range start {
            for _, tail := range digits {
                if len(tail) == length {
                    slice := append([]int{digit}, tail...)
                    sum_slice := sum(slice)

                    if size%2 == 0 && sum_slice == size-1 {
                        continue
                    }

                    if sum_slice <= size {
                        digits = append(digits, slice)
                    }
                }
            }
        }
    }

    // This could be a func called getSums.
    result := [][]int{}
    for _, z := range digits {
        if sum(z) == size {
            result = append(result, z)
        }
    }

    return result
}


// I used the the same ai to convert this too!
func writeStrumsToJSON(max, min int) {
    start := []int{2, 3, 4}

    // The ai did great here!
    allEighthNotes := make(map[int][][]int)
    
    for size := min; size <= max; size++ {
        fmt.Printf("Finding strum patterns with %d eighth notes.\n", size)
        allEighthNotes[size] = rhythmPermutations(start, size)
    }

    // The AI randomly used MarshalIndent but close enough
    file, err := json.Marshal(allEighthNotes)
    if err != nil {
        fmt.Println(err)
        return
    }

    // The ai tried to use io/ioutil but didn't import it.
    // After I imported io/ioutil VScode told me to use os instead.
    err = os.WriteFile("json/newStrumPatterns.json", file, 0644)
    if err != nil {
        fmt.Println(err)
        return
    }
}

func main() {
    writeStrumsToJSON(10, 4)
}


/*
It takes about 90 seconds to generate max=40, and part of that time is writing the json to a file. 
That file is 200 megs and my computer can't open it. But this algorithm is still very useful 
because it would have taken days to calculate max=20 with heap's permutation algo.

I use this generator for groupings of eighth notes but it could be applied to quarter notes or 
whole notes or some kind of subdivision. You can use some basic division/multiplication to mix
for instance eighth and quarter note patterns. This is left as an exorcise to the reader.

You would be hard pressed to come up with a human playable rhythm that can't be expressed with max=30. 
In fact, I'd be very excited to see human playable strum patterns or rhythms not represented 
by max=30, submit it as a bug or pull request. I'd love to see what I'm missing here.

This work was done with the intention of benefiting human musicians, and their sensibilities. Which
is why I'm only interested in patterns that a human can play but are not represented by max=30.
A computer could play any arbitrary pattern size without worrying about feeble human memory.

Side note: [2, 3, 3, 2, 2, 3] is a certified banger, use it in your next track!

*/