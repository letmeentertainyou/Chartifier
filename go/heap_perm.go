package main

// I started this file because I though heap's permutations might
// be faster than the python code but since itertools is written in C
// I don't think that is the case. No matter how you slice it permutations
// takes a lot of power and time. I see no way around using permutations because
// there is no way to know if a strum pattern is viable without rendering every possibility.

import (
	"fmt"
)

// UTILS
func print(message any) {
	fmt.Println(message)
}


func generate(k int, A[]int) {
	if k == 1 {
		print(A)
		//result.append(tuple(A))
	} else {
		generate(k-1, A)
		for i := 0; i < k-1; i++ {
			if k % 2 == 0 {
				A[i], A[k-1] = A[k-1], A[i]
			} else {
				A[0], A[k-1] = A[k-1], A[0]
			}
			generate(k - 1, A)
		}	
	}
}


// Nested funcs are illegal in go
func heap_perm(k int, A[]int) [][]int {

	result := [][]int{}
    generate(k, A)
    return result
}


func main() {
	data := [8]int{2, 2, 2, 2, 3, 3, 4, 4}
	heap_perm(8, data[:])
}







// Broken PPAs live in /etc/apt/sources.list.d
/* They can be deleted from there. Fuck Ubuntu.*/
