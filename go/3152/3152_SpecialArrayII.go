// 3152. Special Array II

package main

import (
	"bufio"
	"encoding/json"
	"fmt"
	"os"

	"github.com/samber/lo"
)

const testSize int = 2

func isArraySpecial(nums []int, queries [][]int) []bool {
	/*
		precompute the longest consecutive special range for each starting position
		a query is valid if its ending index is <= the value calculated above
	*/
	right := 0
	valid := []int{}

	for left := range nums {
		// special window shrinks to zero, then we find the next window using left as the new starting position
		/*
		* * [     ] * * *
		* * * [   ] * * *
		* * * * [ ] * * *
		* * * * * [ ] * *
		 */
		if left > right {
			right = left
		}
		// increment end until before it results in an invalid range
		for right < len(nums)-1 && nums[right]%2 != nums[right+1]%2 {
			right += 1
		}
		valid = append(valid, right)
	}

	result := []bool{}

	for _, q := range queries {
		left, right := q[0], q[1]
		result = append(result, right <= valid[left])
	}

	return result
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	var lines []string
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	for _, test := range lo.Chunk(lines, testSize) {
		var nums []int
		if err1 := json.Unmarshal([]byte(test[0]), &nums); err1 != nil {
			panic(err1)
		}
		var queries [][]int
		if err2 := json.Unmarshal([]byte(test[1]), &queries); err2 != nil {
			panic(err2)
		}
		result := isArraySpecial(nums, queries)
		fmt.Println(result)
	}
}
