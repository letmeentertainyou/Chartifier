
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
					perm := append([]int{digit}, tail...)
					sum_perm := sum(perm)

					if sum_perm == size {
						results = append(results, perm)
						continue
					}

					if sum_perm == size-1 {
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

