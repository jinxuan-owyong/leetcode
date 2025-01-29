// 242. Valid Anagram

package main

import (
	"bufio"
	"fmt"
	"os"
	"slices"

	"github.com/samber/lo"
)

func count(s string) []int {
	freq := make([]int, 26)
	for _, c := range s {
		freq[int(c)-int('a')] += 1
	}
	return freq
}

func isAnagram(s string, t string) bool {
	return slices.Equal(count(s), count(t))
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
		t := test[1][1 : len(test[1])-1]
		result := isAnagram(s, t)
		fmt.Println(result)
	}
}
