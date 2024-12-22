// 2940. Find Building Where Alice and Bob Can Meet

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

type Query struct {
	val int // height to be greater than
	i   int // queries
}

func leftmostBuildingQueries(heights []int, queries [][]int) []int {
	result := make([]int, len(queries))
	for i := range result {
		result[i] = -1
	}

	pq := binaryheap.NewWith(func(_a, _b interface{}) int {
		a, b := _a.(Query), _b.(Query)
		return a.val - b.val // min-heap
	})

	// group queries by the higher index since it is the leftmost position for an answer
	queryAt := make(map[int][]Query)
	for i := range queries {
		slices.Sort(queries[i])
		a, b := queries[i][0], queries[i][1]
		if a == b || heights[a] < heights[b] {
			// if a and b are in the same building, then no need to move (a or b)
			// a can move to b's building if heights[a] < heights[b]
			result[i] = b
		} else {
			// otherwise a and b find a common building j > b > a, where heights[j] > heights[a] >= heights[b] (negation of condition above)
			queryAt[b] = append(queryAt[b], Query{heights[a], i})
		}
	}

	for i, height := range heights {
		// we only push the queries (up to j) since we can answer them at this point, but not the future values
		for _, query := range queryAt[i] {
			pq.Push(query)
		}

		// attempt to find the next taller building
		// we pop until the top of the pq will result in an invalid jump
		for !pq.Empty() {
			top, _ := pq.Peek()
			query := top.(Query)
			if height <= query.val {
				break
			}
			result[query.i] = i
			pq.Pop()
		}
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
		var heights []int
		if err := json.Unmarshal([]byte(test[0]), &heights); err != nil {
			panic(err)
		}

		var queries [][]int
		if err := json.Unmarshal([]byte(test[1]), &queries); err != nil {
			panic(err)
		}

		result := leftmostBuildingQueries(heights, queries)
		fmt.Println(result)
	}
}
