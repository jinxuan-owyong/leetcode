// 1790. Check if One String Swap Can Make Strings Equal

package main

import (
	"bufio"
	"fmt"
	"os"

	"github.com/samber/lo"
)

func areAlmostEqual(s1 string, s2 string) bool {
	/*
		almost equal = same characters && (s1 == s2 || 1 swap required)
		if 1 swap happens, there must be 2 out of place characters
		so s1 and s2 are almost equal if one of the has 0 or 2 out of place characters
	*/
	count := [26]int{}
	outOfPlace := 0
	for i := range s1 {
		count[int(s1[i])-int('a')] += 1
		count[int(s2[i])-int('a')] -= 1
		if s1[i] != s2[i] {
			outOfPlace += 1
		}
	}
	// compare character count
	for i := range 26 {
		if count[i] != 0 {
			return false
		}
	}
	return outOfPlace == 0 || outOfPlace == 2
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	var lines []string
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	const testSize int = 2

	for _, test := range lo.Chunk(lines, testSize) {
		s1 := test[0][1 : len(test[0])-1]
		s2 := test[1][1 : len(test[1])-1]
		result := areAlmostEqual(s1, s2)
		fmt.Println(result)
	}
}
