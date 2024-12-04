// 2825. Make String a Subsequence Using Cyclic Increments

package main

import (
	"bufio"
	"fmt"
	"leetcode/utils"
	"os"
)

func canMakeSubsequence(str1 string, str2 string) bool {
	/*
		suppose str1 contains a subsequence of str2 without any increments
		then we can use sliding window to check if str2 is a subsequence
		similarly, when comparing str1[i] to str2[j], we accept str2[j]
		if it is at most one increment away
		- to consider either both characters are equal
		- or str1[i] == 'z' and str2[j] == 'a'
	*/
	j := 0

	for i := 0; i < len(str1); i += 1 {
		isSame := str1[i] == str2[j]
		isOneAway := str1[i]+1 == str2[j] || str1[i] == 'z' && str2[j] == 'a'
		if isSame || isOneAway {
			j += 1
		}
		if j == len(str2) {
			return true
		}
	}

	return false
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	n := utils.ReadInt(scanner)
	for range n {
		s1 := utils.ReadString(scanner, true)
		s2 := utils.ReadString(scanner, true)
		result := canMakeSubsequence(s1, s2)
		fmt.Println(result)
	}
}
