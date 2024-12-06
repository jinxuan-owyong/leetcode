// 2554. Maximum Number of Integers to Choose From a Range I

package main

import (
	"bufio"
	"fmt"
	"leetcode/utils"
	"os"

	"github.com/emirpasic/gods/sets/hashset"
)

func maxCount(banned []int, n int, maxSum int) int {
	/*
		using a hashset, we can quickly identify if a number is banned
		greedily take in as much numbers as possible for 1..n until maxSum is reached
	*/
	set := hashset.New()
	for _, el := range banned {
		set.Add(el)
	}

	total, count := 0, 0
	for i := 1; i < n+1; i += 1 {
		if !set.Contains(i) && total+i <= maxSum {
			count += 1
			total += i
		}
	}
	return count
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	n := utils.ReadInt(scanner)
	for range n {
		result := 0
		banned := utils.ParseArrInt(utils.ReadString(scanner), ",")
		n := utils.ReadInt(scanner)
		maxSum := utils.ReadInt(scanner)
		result += maxCount(banned, n, maxSum)
		fmt.Println(result)
	}
}
