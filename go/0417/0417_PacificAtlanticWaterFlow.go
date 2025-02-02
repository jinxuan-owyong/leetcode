// 417. Pacific Atlantic Water Flow

package main

import (
	"bufio"
	"encoding/json"
	"fmt"
	"os"

	"github.com/samber/lo"
)

var DIRS = [][]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}

func isWithinRange(heights [][]int, i int, j int) bool {
	return i >= 0 && i < len(heights) && j >= 0 && j < len(heights[0])
}

func bfs(heights [][]int, i int, j int, visited *[][]bool) {
	var queue = [][]int{{i, j}}
	(*visited)[i][j] = true

	for len(queue) > 0 {
		curr := queue[0]
		queue = queue[1:]

		currY, currX := curr[0], curr[1]

		for _, d := range DIRS {
			// where the water should come from
			newY, newX := currY+d[0], currX+d[1]
			// water can "move up" if current cell height <= next cell height
			if isWithinRange(heights, newY, newX) && !(*visited)[newY][newX] && heights[currY][currX] <= heights[newY][newX] {
				queue = append(queue, []int{newY, newX})
				(*visited)[newY][newX] = true
			}
		}
	}
}

func pacificAtlantic(heights [][]int) [][]int {
	// from each ocean mark land cells reachable
	// then compare reachable land cells to get result
	// this is faster than checking from every land cell since we only check ~2n+2m vs n*m starting cells
	var canPacific = make([][]bool, len(heights))
	var canAtlantic = make([][]bool, len(heights))
	for i := range heights {
		canPacific[i] = make([]bool, len(heights[0]))
		canAtlantic[i] = make([]bool, len(heights[0]))
	}

	// ignore the 4 corners since it does not affect 4-directional search
	// from each ocean, start from the nearest land cell
	for j := range len(heights[0]) {
		// pacific top
		bfs(heights, 0, j, &canPacific)
		// atlantic bottom
		bfs(heights, len(heights)-1, j, &canAtlantic)
	}
	for i := range len(heights) {
		// pacific left
		bfs(heights, i, 0, &canPacific)
		// atlantic right
		bfs(heights, i, len(heights[0])-1, &canAtlantic)
	}

	var result [][]int
	for i := range heights {
		for j := range heights[i] {
			if canPacific[i][j] && canAtlantic[i][j] {
				result = append(result, []int{i, j})
			}
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

	const testSize int = 1

	for _, test := range lo.Chunk(lines, testSize) {
		var heights [][]int
		json.Unmarshal([]byte(test[0]), &heights)
		result := pacificAtlantic(heights)
		fmt.Println(result)
	}
}
