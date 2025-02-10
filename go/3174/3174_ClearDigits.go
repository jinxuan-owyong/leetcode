// 3174. Clear Digits

package main

import (
	"bufio"
	"fmt"
	"os"
	"unicode"

	"github.com/samber/lo"
)

func clearDigits(s string) string {
	var stack = []rune{}
	i := 0

	for i < len(s) {
		if unicode.IsLetter(rune(s[i])) {
			stack = append(stack, rune(s[i]))
		} else if len(stack) > 0 && unicode.IsDigit(rune(s[i])) {
			stack = stack[:len(stack)-1]
		}
		i += 1
	}

	return string(stack)
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	var lines []string
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	const testSize int = 1

	for _, test := range lo.Chunk(lines, testSize) {
		s := test[0][1 : len(test[0])-1]
		result := clearDigits(s)
		fmt.Println(result)
	}
}
