// 1752. Check if Array Is Sorted and Rotated

package main

import (
	"bufio"
	"encoding/json"
	"fmt"
	"os"

	"github.com/samber/lo"
)

func check(nums []int) bool {
	if len(nums) == 1 {
		return true
	}
	// if array is sorted, then we can start from the smallest element (i) and check len(nums)-1 pairs
	i := 0
	for curr := range len(nums) {
		// use < instead of <= since we want the leftmost of the same element [3,1,1,1,2]
		if nums[curr] < nums[i] {
			i = curr
		}
	}

	// edge case smallest element wraps around: [1,2,1], i = 0 but we want to start from i = 2
	if i == 0 && nums[len(nums)-1] == nums[0] {
		i = len(nums) - 1
		// find the starting position in the rotated array
		for i > 0 && nums[i-1] == nums[i] {
			i -= 1
		}
	}

	for range len(nums) - 1 {
		// compare sorted and rotated using %
		j := (i + 1) % len(nums)
		if nums[i] > nums[j] { // if no duplicates then use >=
			return false
		}
		i = j
	}

	return true
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	var lines []string
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	const testSize int = 1

	for _, test := range lo.Chunk(lines, testSize) {
		var nums []int
		json.Unmarshal([]byte(test[0]), &nums)
		result := check(nums)
		fmt.Println(result)
	}
}
