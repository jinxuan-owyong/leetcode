// 1014. Best Sightseeing Pair

package main

import (
	"bufio"
	"encoding/json"
	"fmt"
	"os"

	"github.com/samber/lo"
)

func maxScoreSightseeingPair(values []int) int {
	/*
		values[i] + i and values[j] - j are constants, so we can simplify them to v1 and v2 respectively
		then the problem is simplified to finding the maximum value of v1[i] + v2[j] where i < j,
		we want to find max(v1 + max(v2))
		since maxV2 = max(values[j], values[j+1]), it can be determined when iterating from back to front,
		then at every v1, we calculate v1 + maxV2, and take the maximum of this result
	*/
	result := 0
	maxV2 := values[len(values)-1] - (len(values) - 1)

	for i := len(values) - 1 - 1; i >= 0; i -= 1 {
		v1, v2 := values[i]+i, values[i]-i
		result = max(result, v1+maxV2)
		maxV2 = max(maxV2, v2)
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
		var values []int
		if err := json.Unmarshal([]byte(test[0]), &values); err != nil {
			panic(err)
		}
		result := maxScoreSightseeingPair(values)
		fmt.Println(result)
	}
}
