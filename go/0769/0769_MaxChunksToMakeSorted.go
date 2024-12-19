// 769. Max Chunks To Make Sorted

package main

import (
	"bufio"
	"encoding/json"
	"fmt"
	"os"
	"slices"

	"github.com/samber/lo"
)

func maxChunksToSorted(arr []int) int {
	// len(arr) <= 10
	sorted := slices.Clone(arr)
	slices.Sort(sorted)

	i, j := 0, 0
	count := 0

	for i < len(arr) {
		for {
			slices.Sort(arr[i : j+1])
			// maximise number of chunks by scanning for the next chunk when the first valid chunk is met
			if slices.Equal(arr[i:j+1], sorted[i:j+1]) {
				break
			}
			j += 1
		}
		i, j = j+1, j+1
		count += 1
	}

	return count
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	var lines []string
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	const testSize int = 1

	for _, test := range lo.Chunk(lines, testSize) {
		var arr []int
		if err := json.Unmarshal([]byte(test[0]), &arr); err != nil {
			panic(err)
		}
		result := maxChunksToSorted(arr)
		fmt.Println(result)
	}
}
