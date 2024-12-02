package main

import (
	"bufio"
	"fmt"
	"leetcode/utils"
	"os"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	n := utils.ReadInt(scanner)
	for range n {
		result := 0
		fmt.Println(result)
	}
}
