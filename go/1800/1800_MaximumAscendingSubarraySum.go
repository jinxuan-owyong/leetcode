// 1800. Maximum Ascending Subarray Sum

package main

import (
	"bufio"
	"encoding/json"
	"fmt"
	"os"

	"github.com/samber/lo"
)

func maxAscendingSum(nums []int) int {
	curr := 0
	largest := 0

	for i := range len(nums) {
		curr += nums[i]
		if i == len(nums)-1 || nums[i] >= nums[i+1] {
			largest = max(largest, curr)
			curr = 0
		}
	}

	return largest
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
		result := maxAscendingSum(nums)
		fmt.Println(result)
	}
}
