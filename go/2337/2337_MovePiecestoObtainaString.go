// 2337. Move Pieces to Obtain a String

package main

import (
	"bufio"
	"fmt"
	"leetcode/utils"
	"os"
)

func canChange(start string, target string) bool {
	/*
		the order of L/R remains unchanged after moving the pieces
		use 2 pointers to compare character by character
		we know that L cannot move right, while R cannot move left
		hence we compare the relative positions of L/R
		"_RL_"
		"L__R"

	*/
	count := map[rune]int{'L': 0, 'R': 0}
	for _, c := range start {
		count[c] += 1
	}
	for _, c := range target {
		count[c] -= 1
	}
	if count['L'] != 0 || count['R'] != 0 {
		return false
	}

	i := 0
	j := 0
	for i < len(start) && j < len(target) {
		if start[i] == '_' {
			i += 1
			continue
		}
		if target[j] == '_' {
			j += 1
			continue
		}
		isValidComp := start[i] == target[j]
		triedToMoveLRight := target[j] == 'L' && j > i
		triedToMoveRLeft := target[j] == 'R' && j < i
		if !isValidComp || triedToMoveLRight || triedToMoveRLeft {
			return false
		}
		i += 1
		j += 1
	}
	return true
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	n := utils.ReadInt(scanner)
	for range n {
		start := utils.ReadString(scanner)
		target := utils.ReadString(scanner)
		result := canChange(start, target)
		fmt.Println(result)
	}
}
