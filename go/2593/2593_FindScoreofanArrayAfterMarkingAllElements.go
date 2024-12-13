// 2593. Find Score of an Array After Marking All Elements

package main

import (
	"bufio"
	"encoding/json"
	"fmt"
	"os"

	"github.com/emirpasic/gods/trees/binaryheap"
	"github.com/samber/lo"
)

const testSize int = 1

func findScore(nums []int) int64 {
	score := int64(0)

	// keep track of indices of nums
	marked := make([]bool, len(nums))
	pq := binaryheap.NewWith(func(_a, _b interface{}) int {
		a, b := _a.(int), _b.(int)
		if nums[a] == nums[b] {
			return a - b
		}
		return nums[a] - nums[b]
	})

	// populate pq
	for i := range nums {
		pq.Push(i)
	}

	for !pq.Empty() {
		_i, _ := pq.Pop()
		i := _i.(int)

		if !marked[i] {
			score += int64(nums[i])
			marked[i] = true
			if i > 0 {
				marked[i-1] = true
			}
			if i < len(nums)-1 {
				marked[i+1] = true
			}
		}
	}

	return score
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	var lines []string
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	for _, test := range lo.Chunk(lines, testSize) {
		var nums []int
		if err := json.Unmarshal([]byte(test[0]), &nums); err != nil {
			panic(err)
		}
		result := findScore(nums)
		fmt.Println(result)
	}
}
