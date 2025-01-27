// 11. Container With Most Water

package main

import (
	"bufio"
	"encoding/json"
	"fmt"
	"os"

	"github.com/samber/lo"
)

func maxArea(height []int) int {
	result := 0
	i, j := 0, len(height)-1

	for i < j {
		area := (j - i) * min(height[i], height[j])
		result = max(area, result)
		if height[i] < height[j] {
			i += 1
		} else {
			j -= 1
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
		var height []int
		if err := json.Unmarshal([]byte(test[0]), &height); err != nil {
			panic(err)
		}
		result := maxArea(height)
		fmt.Println(result)
	}
}
