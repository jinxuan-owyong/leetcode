// 1267. Count Servers that Communicate

package main

import (
	"bufio"
	"encoding/json"
	"fmt"
	"os"

	"github.com/samber/lo"
)

func countServers(grid [][]int) int {
	/*
		a server can communicate with another if they are on the same row or column
		first count the number of servers in each row and column
		if the server lies on a row or column with more than one server, we increment the count
	*/
	rowCount := []int{}
	for range grid {
		rowCount = append(rowCount, 0)
	}
	colCount := []int{}
	for range grid[0] {
		colCount = append(colCount, 0)
	}

	for i, row := range grid {
		for j, server := range row {
			if server == 1 {
				rowCount[i] += 1
				colCount[j] += 1
			}
		}
	}

	total := 0
	for i, row := range grid {
		for j, server := range row {
			if server == 1 && (rowCount[i] > 1 || colCount[j] > 1) {
				total += 1
			}
		}
	}

	return total
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	var lines []string
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	const testSize int = 1

	for _, test := range lo.Chunk(lines, testSize) {
		var grid [][]int
		if err := json.Unmarshal([]byte(test[0]), &grid); err != nil {
			panic(err)
		}
		result := countServers(grid)
		fmt.Println(result)
	}
}
