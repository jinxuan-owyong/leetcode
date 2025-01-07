// 1408. String Matching in an Array

package main

import (
	"bufio"
	"encoding/json"
	"fmt"
	"os"
	"strings"

	"github.com/samber/lo"
)

func stringMatching(words []string) []string {
	var result []string

	for i := range words {
		for j := range words {
			if i != j && strings.Contains(words[j], words[i]) {
				result = append(result, words[i])
				break
			}
		}
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
		var words []string
		if err := json.Unmarshal([]byte(test[0]), &words); err != nil {
			panic(err)
		}
		result := stringMatching(words)
		fmt.Println(result)
	}
}
