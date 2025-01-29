// 1. Two Sum

package main

import (
	"bufio"
	"encoding/json"
	"fmt"
	"leetcode/utils"
	"os"
	"slices"

	"github.com/samber/lo"
)

type El struct {
	value int
	idx   int
}

func twoSum(nums []int, target int) []int {
	candidates := make([]El, len(nums))
	for i, n := range nums {
		candidates[i] = El{n, i}
	}

	slices.SortFunc(candidates, func(a, b El) int {
		return a.value - b.value
	})

	i, j := 0, len(nums)-1
	for i < j {
		if total := candidates[i].value + candidates[j].value; total == target {
			return []int{candidates[i].idx, candidates[j].idx}
		} else if total < target {
			i += 1
		} else {
			j -= 1
		}
	}

	return []int{-1, -1}
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
		var target int = utils.ParseInt(test[1])
		result := twoSum(nums, target)
		fmt.Println(result)
	}
}
