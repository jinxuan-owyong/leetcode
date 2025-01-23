// 3. Longest Substring Without Repeating Characters

package main

import (
	"bufio"
	"fmt"
	"os"

	"github.com/samber/lo"
)

func lengthOfLongestSubstring(s string) int {
	exists := make(map[rune]bool)
	result, curr := 0, 0
	i := 0

	for j := range s {
		// shrink window so that adding s[j] will still be valid (until s[i-1]==s[j])
		for {
			if i < j && exists[rune(s[j])] {
				exists[rune(s[i])] = false
				curr -= 1
				i += 1
			} else {
				break
			}
		}
		curr += 1
		result = max(result, curr)
		exists[rune(s[j])] = true
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
		result := lengthOfLongestSubstring(test[0][1 : len(test[0])-1])
		fmt.Println(result)
	}
}
