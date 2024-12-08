// 2054. Two Best Non-Overlapping Events

package main

import (
	"bufio"
	"encoding/json"
	"fmt"
	"os"
	"slices"

	"github.com/emirpasic/gods/trees/binaryheap"
	"github.com/samber/lo"
)

const testSize int = 1

func maxTwoEvents(events [][]int) int {
	slices.SortFunc(events, func(a, b []int) int {
		return a[0] - b[0]
	})

	pq := binaryheap.NewWith(func(_a, _b interface{}) int {
		a, b := _a.([]int), _b.([]int)
		if a[1] != b[1] {
			return a[1] - b[1]
		}
		return a[2] - b[2]
	})

	var result int = 0
	var maxFirstVal int = 0
	for _, interval := range events {
		for !pq.Empty() {
			_curr, _ := pq.Peek()
			curr := _curr.([]int)
			// pop until the start time of the incoming interval is after the end of current
			if curr[1] < interval[0] {
				// find the largest val of the first interval in this group
				maxFirstVal = max(maxFirstVal, curr[2])
				pq.Pop()
			} else {
				break
			}
		}
		result = max(result, interval[2]+maxFirstVal)
		pq.Push(interval)
	}

	return result
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	var lines []string
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}
	inputs := lo.Chunk(lines, testSize)

	for i := range len(inputs) / testSize {
		var events [][]int
		if err := json.Unmarshal([]byte(inputs[i][0]), &events); err != nil {
			panic(err)
		}
		result := maxTwoEvents(events)
		fmt.Println(result)
	}
}
