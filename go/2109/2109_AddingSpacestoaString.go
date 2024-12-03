// 2109. Adding Spaces to a String

package main

import (
	"bufio"
	"fmt"
	"leetcode/utils"
	"os"
	"strings"
)

func addSpaces(s string, spaces []int) string {
	/*
		use 2 pointers, one to keep track of the last position where a space was inserted
		another to keep track of the next space to be inserted
	*/
	var builder strings.Builder

	i := 0
	j := 0
	for i < len(s) && j < len(spaces) {
		// write string until the next space is encountered
		for i < spaces[j] {
			builder.WriteByte(s[i])
			i += 1
		}
		// write space except if all spaces are written
		if j < len(spaces) {
			builder.WriteRune(' ')
			j += 1
		}
	}
	builder.WriteString(s[i:])
	return builder.String()
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	n := utils.ReadInt(scanner)
	for range n {
		s := utils.ReadString(scanner, true)
		spaces := utils.ParseArrInt(utils.ReadString(scanner, true), ",")
		result := addSpaces(s, spaces)
		fmt.Println(result)
	}
}
