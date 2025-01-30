// 424. Longest Repeating Character Replacement

package main

import (
	"bufio"
	"fmt"
	"leetcode/utils"
	"os"

	"github.com/samber/lo"
)

func characterReplacement(s string, k int) int {
	// window needs to be shrunk if num characters except the most frequent > k
	// ignore the most frequent since we want the longest substring

	i := 0
	window := make(map[rune]int, 26)
	result := 0
	for j := range s {
		// expand window
		window[rune(s[j])] += 1

		// find the most common
		var most = 0
		for _, v := range window {
			most = max(most, v)
		}

		// shrink until we get a valid k
		// we group the characters other than the most frequent together since they can all be replaced
		for i < j && (j-i+1)-most > k {
			window[rune(s[i])] -= 1
			i += 1
		}
		result = max(result, j-i+1)
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
		s := test[0][1 : len(test[0])-1]
		k := utils.ParseInt(test[1])
		result := characterReplacement(s, k)
		fmt.Println(result)
	}
}
