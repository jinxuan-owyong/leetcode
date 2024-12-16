// 3264. Final Array State After K Multiplication Operations I

package main

import (
	"bufio"
	"encoding/json"
	"fmt"
	"leetcode/utils"
	"os"

	"github.com/emirpasic/gods/trees/binaryheap"
	"github.com/samber/lo"
)

func getFinalState(nums []int, k int, multiplier int) []int {
	pq := binaryheap.NewWith(func(_a, _b interface{}) int {
		a, b := _a.([]int), _b.([]int)
		// if there are multiple occurrences of the minimum value, select the one that appears first
		if a[0] == b[0] {
			return a[1] - b[1]
		}
		// find the minimum value x in nums
		return a[0] - b[0]
	})

	for i, num := range nums {
		pq.Push([]int{num, i})
	}

	for range k {
		_curr, _ := pq.Pop()
		curr := _curr.([]int)
		curr[0] *= multiplier
		nums[curr[1]] = curr[0]
		pq.Push(curr)
	}

	return nums
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	var lines []string
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	const testSize int = 3

	for _, test := range lo.Chunk(lines, testSize) {
		var nums []int
		if err := json.Unmarshal([]byte(test[0]), &nums); err != nil {
			panic(err)
		}
		k := utils.ParseInt(test[1])
		multiplier := utils.ParseInt(test[2])
		result := getFinalState(nums, k, multiplier)
		fmt.Println(result)
	}
}
