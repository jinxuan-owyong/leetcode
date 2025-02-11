// 1910. Remove All Occurrences of a Substring

package main

import (
	"bufio"
	"fmt"
	"os"

	"github.com/samber/lo"
)

func removeOccurrences(s string, part string) string {
	var stack []rune

	for _, c := range s {
		stack = append(stack, c)

		if len(stack) >= len(part) {
			match := true
			for i := range part {
				j := len(stack) - len(part) + i
				match = match && rune(part[i]) == stack[j]
			}

			if match {
				stack = stack[:len(stack)-len(part)]
			}
		}
	}

	return string(stack)
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
		part := test[1][1 : len(test[1])-1]
		result := removeOccurrences(s, part)
		fmt.Println(result)
	}
}
