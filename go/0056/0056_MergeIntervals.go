// 56. Merge Intervals

package main

import (
	"bufio"
	"encoding/json"
	"fmt"
	"os"
	"slices"

	"github.com/samber/lo"
)

func merge(intervals [][]int) [][]int {
	if len(intervals) == 0 {
		return [][]int{}
	}

	slices.SortFunc(intervals, func(a, b []int) int {
		return slices.Compare(a, b)
	})

	var result [][]int
	curr := intervals[0]
	for _, next := range intervals[1:] {
		if curr[1] < next[0] {
			result = append(result, curr)
			curr = next
		} else {
			curr[0], curr[1] = min(curr[0], next[0]), max(curr[1], next[1])
		}
	}

	return append(result, curr)
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	var lines []string
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	const testSize int = 1

	for _, test := range lo.Chunk(lines, testSize) {
		var intervals [][]int
		json.Unmarshal([]byte(test[0]), &intervals)
		result := merge(intervals)
		fmt.Println(result)
	}
}
