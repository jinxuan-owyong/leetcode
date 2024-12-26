// 494. Target Sum

package main

import (
	"bufio"
	"encoding/json"
	"fmt"
	"leetcode/utils"
	"os"

	"github.com/samber/lo"
)

func backtrack(total int, i int, nums []int, target int, count *int) {
	if i == len(nums) {
		if total == target {
			*count += 1
		}
		return
	}
	backtrack(total+nums[i], i+1, nums, target, count)
	backtrack(total-nums[i], i+1, nums, target, count)
}

func findTargetSumWays(nums []int, target int) int {
	count := 0
	backtrack(0, 0, nums, target, &count)
	return count
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	var lines []string
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	const testSize int = 2

	for _, test := range lo.Chunk(lines, testSize) {
		var nums []int
		if err := json.Unmarshal([]byte(test[0]), &nums); err != nil {
			panic(err)
		}
		target := utils.ParseInt(test[1])
		result := findTargetSumWays(nums, target)
		fmt.Println(result)
	}
}
