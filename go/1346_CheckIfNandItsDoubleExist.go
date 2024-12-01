// 1346. Check If N and Its Double Exist

package main

import (
	"fmt"

	"github.com/emirpasic/gods/maps/hashmap"
)

func checkIfExist(arr []int) bool {
	freq := hashmap.New()

	for _, el := range arr {
		curr, ok := freq.Get(el)

		if ok {
			if count, ok := curr.(int); ok {
				freq.Put(el, count+1)
			}
		} else {
			freq.Put(el, 1)
		}
	}

	for i := range arr {
		var curr = arr[i]
		if curr == 0 {
			count, _ := freq.Get(curr)
			if count, ok := count.(int); ok && count > 1 {
				return true
			}
		} else {
			_, multiplyOk := freq.Get(curr * 2)
			_, divideOk := freq.Get(curr / 2) // floor division
			if multiplyOk || (curr%2 == 0 && divideOk) {
				return true
			}
		}
	}

	return false
}

func main() {
	result1 := checkIfExist([]int{10, 2, 5, 3})
	fmt.Println(result1)

	result2 := checkIfExist([]int{3, 1, 7, 11})
	fmt.Println(result2)

	result3 := checkIfExist([]int{0})
	fmt.Println(result3)

	result4 := checkIfExist([]int{0, 1, 2, 0})
	fmt.Println(result4)

	result5 := checkIfExist([]int{0, 0})
	fmt.Println(result5)
}
