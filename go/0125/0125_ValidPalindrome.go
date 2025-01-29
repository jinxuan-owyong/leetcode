// 125. Valid Palindrome

package main

import (
	"bufio"
	"fmt"
	"os"
	"unicode"

	"github.com/samber/lo"
)

func isPalindrome(s string) bool {
	i, j := 0, len(s)-1
	for i < j {
		for i < j && !unicode.IsLetter(rune(s[i])) && !unicode.IsDigit(rune(s[i])) {
			i += 1
		}
		for i < j && !unicode.IsLetter(rune(s[j])) && !unicode.IsDigit(rune(s[j])) {
			j -= 1
		}
		if unicode.ToLower(rune(s[i])) != unicode.ToLower(rune(s[j])) {
			return false
		}
		i += 1
		j -= 1
	}
	return true
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
		result := isPalindrome(s)
		fmt.Println(result)
	}
}
