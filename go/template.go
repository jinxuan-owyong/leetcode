package main

import (
	"bufio"
	"fmt"
	"os"

	"github.com/samber/lo"
)

const testSize int = 1

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	var lines []string
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}
	inputs := lo.Chunk(lines, testSize)

	for i := range len(inputs) / testSize {
		result := 0
		fmt.Println(result)
	}
}
