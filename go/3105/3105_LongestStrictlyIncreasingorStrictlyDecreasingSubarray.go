// 3105. Longest Strictly Increasing or Strictly Decreasing Subarray

package main

import (
	"bufio"
	"encoding/json"
	"fmt"
	"os"

	"github.com/samber/lo"
)

func longestMonotonicSubarray(nums []int) int {
	result := 0

	// longest strictly increasing
	i, j := 0, 0
	for j < len(nums) {
		if j == len(nums)-1 || nums[j] >= nums[j+1] {
			result = max(result, j-i+1)
			i = j + 1
		}
		j += 1
	}

	// longest strictly decreasing
	i, j = 0, 0
	for j < len(nums) {
		if j == len(nums)-1 || nums[j] <= nums[j+1] {
			result = max(result, j-i+1)
			i = j + 1
		}
		j += 1
	}

	return result
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
		result := longestMonotonicSubarray(nums)
		fmt.Println(result)
	}
}
