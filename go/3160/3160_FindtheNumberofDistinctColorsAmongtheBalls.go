// 3160. Find the Number of Distinct Colors Among the Balls

package main

import (
	"bufio"
	"encoding/json"
	"fmt"
	"leetcode/utils"
	"os"

	"github.com/samber/lo"
)

func queryResults(limit int, queries [][]int) []int {
	var freq = make(map[int]int)
	var colours = make(map[int]int)
	var result []int

	for _, q := range queries {
		ball, col := q[0], q[1]
		// we need to delete the existing key in freq when adding a different colour
		// to a ball with an existing colour, for len(freq) to return the correct value
		if curr, exists := colours[ball]; exists {
			if curr != col {
				if freq[curr] == 1 {
					delete(freq, curr)
					freq[col] += 1
					colours[ball] = col
				} else {
					freq[curr] -= 1
					freq[col] += 1
					colours[ball] = col
				}
			}
			// do not increment if no change in ball colour (curr == col)
		} else {
			colours[ball] = col
			freq[col] += 1
		}
		result = append(result, len(freq))
	}

	return result
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	var lines []string
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	const testSize int = 2

	for _, test := range lo.Chunk(lines, testSize) {
		limit := utils.ParseInt(test[0])
		var queries [][]int
		json.Unmarshal([]byte(test[1]), &queries)
		result := queryResults(limit, queries)
		fmt.Println(result)
	}
}
