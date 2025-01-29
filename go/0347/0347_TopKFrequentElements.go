// 347. Top K Frequent Elements

package main

import (
	"bufio"
	"encoding/json"
	"fmt"
	"leetcode/utils"
	"os"
	"slices"

	"github.com/samber/lo"
)

func topKFrequent(nums []int, k int) []int {
	freq := make(map[int]int)
	for _, n := range nums {
		freq[n] += 1
	}

	var freqSorted [][]int
	for k, v := range freq {
		freqSorted = append(freqSorted, []int{k, v})
	}

	slices.SortFunc(freqSorted, func(a, b []int) int {
		return b[1] - a[1]
	})

	result := make([]int, k)
	for i := range k {
		result[i] = freqSorted[i][0]
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
		var nums []int
		if err := json.Unmarshal([]byte(test[0]), &nums); err != nil {
			panic(err)
		}
		var k int = utils.ParseInt(test[1])
		result := topKFrequent(nums, k)
		fmt.Println(result)
	}
}
