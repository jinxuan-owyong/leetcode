// 57. Insert Interval

package main

import (
	"bufio"
	"encoding/json"
	"fmt"
	"os"

	"github.com/samber/lo"
)

func insert(intervals [][]int, newInterval []int) [][]int {
	var result [][]int
	i := 0
	// insert until first interval that needs to be merged
	for i < len(intervals) && intervals[i][1] < newInterval[0] {
		result = append(result, intervals[i])
		i += 1
	}

	curr := newInterval
	for i < len(intervals) && curr[1] >= intervals[i][0] {
		// merge intervals
		curr[0], curr[1] = min(intervals[i][0], curr[0]), max(intervals[i][1], curr[1])
		i += 1
	}

	result = append(result, curr)

	// remaining is in sorted order
	return append(result, intervals[i:]...)
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	var lines []string
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	const testSize int = 2

	for _, test := range lo.Chunk(lines, testSize) {
		var intervals [][]int
		var newInterval []int
		json.Unmarshal([]byte(test[0]), &intervals)
		json.Unmarshal([]byte(test[1]), &newInterval)
		result := insert(intervals, newInterval)
		fmt.Println(result)
	}
}
