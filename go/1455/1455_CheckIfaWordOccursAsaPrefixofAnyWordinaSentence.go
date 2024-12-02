// 1455. Check If a Word Occurs As a Prefix of Any Word in a Sentence

package main

import (
	"bufio"
	"fmt"
	"leetcode/utils"
	"os"
	"strings"
)

func isPrefixOfWord(sentence string, searchWord string) int {
	words := strings.Split(sentence, " ")

	for i, word := range words {
		j := 0
		for j < len(word) && word[j] == searchWord[j] {
			j += 1
			if j == len(searchWord) {
				return i + 1
			}
		}
		// check next word for substring
	}

	return -1
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	n := utils.ReadInt(scanner)
	for range n {
		arg1 := utils.ReadString(scanner, true)
		arg2 := utils.ReadString(scanner, true)
		result := isPrefixOfWord(arg1, arg2)
		fmt.Println(result)
	}
}
