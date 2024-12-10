// 2981. Find Longest Special Substring That Occurs Thrice I

package main

import (
	"bufio"
	"fmt"
	"os"

	"github.com/samber/lo"
)

const testSize int = 1

func isSpecial(s string) bool {
	for i := 1; i < len(s); i += 1 {
		if s[i-1] != s[i] {
			return false
		}
	}
	return true
}

func maximumLength(s string) int {
	freq := make(map[string]int)
	longest := 0

	for size := 1; size <= len(s); size += 1 {
		for i := 0; i <= len(s)-size; i += 1 {
			curr := s[i : i+size]
			count, ok := freq[curr]
			// map only contains special strings
			if ok {
				freq[curr] = count + 1
				if count+1 >= 3 {
					longest = size
				}
			} else if isSpecial(curr) {
				freq[curr] = 1
			}
		}
	}

	if longest == 0 {
		return -1
	}

	return longest
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	var lines []string
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	for _, test := range lo.Chunk(lines, testSize) {
		result := maximumLength(test[0][1 : len(test[0])-1])
		fmt.Println(result)
	}
}
