// 102. Binary Tree Level Order Traversal

package main

import (
	"bufio"
	"fmt"
	"leetcode/structs"
	"leetcode/utils"
	"os"

	"github.com/samber/lo"
)

func levelOrder(root *structs.TreeNode) [][]int {
	queue := []*structs.TreeNode{root}
	values := [][]int{}

	for len(queue) > 0 {
		n := len(queue)
		level := []int{}

		for range n {
			curr := queue[0]
			queue = queue[1:]
			if curr != nil {
				queue = append(queue, curr.Left, curr.Right)
				level = append(level, curr.Val)
			}
		}

		if len(level) > 0 {
			values = append(values, level)
		}
	}

	return values
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	var lines []string
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	const testSize int = 1

	for _, test := range lo.Chunk(lines, testSize) {
		root := utils.ToTree(test[0])
		result := levelOrder(root)
		fmt.Println(result)
	}
}
