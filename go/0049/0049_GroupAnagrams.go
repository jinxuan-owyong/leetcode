// 49. Group Anagrams

package main

import (
	"bufio"
	"encoding/json"
	"fmt"
	"os"
	"strings"

	"github.com/samber/lo"
)

func groupAnagrams(strs []string) [][]string {
	groups := make(map[string][]string)
	for _, s := range strs {
		// count frequency of characters
		var freq [26]int
		for _, c := range s {
			freq[int(c)-int('a')] += 1
		}

		// get key for string
		var key strings.Builder
		for i, count := range freq {
			if count > 0 {
				key.WriteString(fmt.Sprintf("%v,%v#", i, count))
			}
		}

		// add string to group
		groups[key.String()] = append(groups[key.String()], s)
	}

	// convert groups to 2d array
	var result [][]string
	for _, group := range groups {
		result = append(result, group)
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
		var strs []string
		if err := json.Unmarshal([]byte(test[0]), &strs); err != nil {
			panic(err)
		}
		result := groupAnagrams(strs)
		fmt.Println(result)
	}
}
