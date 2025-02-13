// 3066. Minimum Operations to Exceed Threshold Value II

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

func minOperations(nums []int, k int) int {
	pq := binaryheap.NewWithIntComparator()
	for _, n := range nums {
		pq.Push(n)
	}

	count := 0

	for pq.Size() > 1 {
		if top, _ := pq.Peek(); top.(int) >= k {
			break
		}
		_x, _ := pq.Pop()
		_y, _ := pq.Pop()
		x, y := _x.(int), _y.(int)
		count += 1
		pq.Push(min(x, y)*2 + max(x, y))
	}

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
		json.Unmarshal([]byte(test[0]), &nums)
		k := utils.ParseInt(test[1])
		result := minOperations(nums, k)
		fmt.Println(result)
	}
}
