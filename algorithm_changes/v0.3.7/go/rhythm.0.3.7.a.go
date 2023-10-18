
package main


import (
    "encoding/json"
    "fmt"
    "os"
)


func sum(iterable[]int) int {
    result := 0
    for _, num := range iterable {
        result += num
    }
    return result
}


func rhythmPermutations(start[]int, size int) [][]int {

    upper  := size / 2
	old    := [][]int{}
    digits := [][]int{}
    
    for _, i := range start {
		old    = append(old,    []int{i})
        digits = append(digits, []int{i})
    }

    for length := 1; length < upper; length++ {
		tmp := [][]int{}
        for _, digit := range start {
            for _, tail := range old {
					slice := append([]int{digit}, tail...)
					sum_slice := sum(slice)

					if size % 2 == 0 && sum_slice == size-1 {
						continue
					}

					if sum_slice <= size {
						tmp = append(tmp, slice)
					}
            }
        }
		old = tmp
		digits = append(digits, old...)
    }

    result := [][]int{}
    for _, z := range digits {
        if sum(z) == size {
            result = append(result, z)
        }
    }
    return result
}


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

func main() {
	writeStrumsToJSON(20, 4)
}
