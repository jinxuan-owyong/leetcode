// 79. Word Search

package main

import (
	"bufio"
	"encoding/json"
	"fmt"
	"leetcode/utils"
	"os"

	"github.com/samber/lo"
)

func dfs(board [][]byte, word string, i int, j int, curr int) bool {
	if isValidRange := i >= 0 && i < len(board) && j >= 0 && j < len(board[0]); !isValidRange || board[i][j] != word[curr] {
		return false
	}
	if curr == len(word)-1 {
		return true
	}

	temp := board[i][j]
	board[i][j] = ' '

	up := dfs(board, word, i-1, j, curr+1)
	down := dfs(board, word, i+1, j, curr+1)
	left := dfs(board, word, i, j-1, curr+1)
	right := dfs(board, word, i, j+1, curr+1)

	// reset after visiting to allow other DFS paths to visit the same cell
	board[i][j] = temp

	return up || down || left || right
}

func exist(board [][]byte, word string) bool {
	// find the first starting position, then DFS to find if rest of the string matches
	for i := range board {
		for j := range board[i] {
			if board[i][j] == word[0] {
				if dfs(board, word, i, j, 0) {
					return true
				}
			}
		}
	}
	return false
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	var lines []string
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	const testSize int = 2

	for _, test := range lo.Chunk(lines, testSize) {
		var data [][]string
		json.Unmarshal([]byte(test[0]), &data)
		board := utils.To2DByteArray(data)
		word := test[1][1 : len(test[1])-1]
		result := exist(board, word)
		fmt.Println(result)
	}
}
