// 217. Contains Duplicate

package main

import (
	"bufio"
	"encoding/json"
	"fmt"
	"os"

	"github.com/samber/lo"
)

func containsDuplicate(nums []int) bool {
	seen := make(map[int]bool)
	for _, n := range nums {
		if _, exists := seen[n]; exists {
			return true
		}
		seen[n] = true
	}
	return false
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	var lines []string
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	const testSize int = 1

	for _, test := range lo.Chunk(lines, testSize) {
		var nums []int
		if err := json.Unmarshal([]byte(test[0]), &nums); err != nil {
			panic(err)
		}
		result := containsDuplicate(nums)
		fmt.Println(result)
	}
}
