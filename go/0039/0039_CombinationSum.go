// 39. Combination Sum

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

func backtrack(candidates []int, target int, i int, total int, result *[][]int, path *[]int) {
	// either add the current value or skip to the next
	// we do not need to consider add and take next since it happens in the next recursion
	if total == target {
		*result = append(*result, slices.Clone(*path))
	}
	if total >= target || i == len(candidates) {
		return
	}

	backtrack(candidates, target, i+1, total, result, path) // skip current
	*path = append(*path, candidates[i])
	backtrack(candidates, target, i, total+candidates[i], result, path) // add current value
	*path = (*path)[:len(*path)-1]
}

func combinationSum(candidates []int, target int) [][]int {
	var result [][]int
	var path []int

	slices.Sort(candidates)
	backtrack(candidates, target, 0, 0, &result, &path)

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
		var candidates []int
		json.Unmarshal([]byte(test[0]), &candidates)
		target := utils.ParseInt(test[1])
		result := combinationSum(candidates, target)
		fmt.Println(result)
	}
}
